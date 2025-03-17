# Copyright (C) 2023 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause
from __future__ import annotations
"""PySide6 port of the QtMultiMedia camera example from Qt v6.x"""
import os
import sys
import re
import time
from pathlib import Path
from datetime import datetime
import json
from PySide6.QtMultimedia import (QCamera, QCameraDevice, QImageCapture, QMediaCaptureSession, QMediaDevices)
from PySide6.QtWidgets import QMainWindow, QMessageBox, QPushButton
from PySide6.QtGui import QAction, QActionGroup, QImage, QPixmap
from PySide6.QtCore import (QDir, QTimer, Qt, Slot, Signal, QObject, QThread)
from imagesettings import ImageSettings
from has_camera_ui import Ui_Camera
from styles import buttonStyle, mboxStyle

from ocr import GeminiOCR
from evaluation import Evaluation
from render_latex import MathJaxSOL, MathJaxRes, ClearHTML, LoadHTML
from database import Session, StudentHAS
from ak_dialog import AK_Dialog

class OCRWorker(QObject):
    finished = Signal(str, float)
    error = Signal(str)

    def __init__(self, file):
        super().__init__()
        self.file = file

    def run(self):
        try:
            start_ocr_timer = time.time()
            
            has_latex = GeminiOCR(self.file)  # Run OCR

            ocr_time = time.time() - start_ocr_timer

            self.finished.emit(has_latex, ocr_time)  # Send the result back
            
        except Exception as e:
            self.error.emit(str(e))


class HAS_Camera(QMainWindow):
    finishedImageProcessing = Signal(str)
        
    def __init__(self, session_window, id, fa_weight, ak_latex):
        super().__init__()

        self.session_window = session_window

        # Attribute from AnswerKey table 
        self.answer_key_id = id
        self.fa_weight = fa_weight
        self.ak_latex = ak_latex

        # Attribute for StudentHAS table
        self.eval = Evaluation()
        self.result = None

        self.eval.ask_asm_signal.connect(self.ASMConfirmation)
        self.eval.asm_response_signal.connect(self.eval.handleASM1)  
        self.eval.evaluation_done_signal.connect(self.ResumeEval)

        self._video_devices_group = None
        self.m_devices = QMediaDevices()
        self.m_imageCapture = None
        self.m_captureSession = QMediaCaptureSession()
        self.m_camera = None
        self.m_mediaRecorder = None

        self.m_isCapturingImage = False
        self.m_applicationExiting = False
        self.m_doImageCapture = True

        self.viewfinderDone = False
        self.imageSavedDone = False
        self.savedFileName = None

        self._ui = Ui_Camera()
        self._ui.setupUi(self)

        for button in self.findChildren(QPushButton):
            button.setStyleSheet(buttonStyle)

        self.clearhtml = ClearHTML()
        self.loadhtml = LoadHTML()
        
        
        self._ui.web_latex.setHtml(self.clearhtml)
        self._ui.web_result.setHtml(self.clearhtml) 


        self.image_folder = os.path.join(os.getcwd(), "images", "has")
        os.makedirs(self.image_folder, exist_ok=True)  # Ensure the folder exists

        self._ui.actionAbout_Qt.triggered.connect(qApp.aboutQt)  # noqa: F821
        self.finishedImageProcessing.connect(self.OCRProcessing)
        self._ui.push_save.clicked.connect(self.saveToDatabase)
        self._ui.push_view_ak.clicked.connect(self.viewAnswerKey)
        self._ui.push_back.clicked.connect(self.backToSession)

        # disable all buttons by default
        self.updateCameraActive(False)
        self.readyForCapture(False)
        self._ui.push_save.setEnabled(False)

        self.fetchStats()
        # try to actually initialize camera & mic
        self.initialize()


    ################################################################################
    # Initializing Camera

    @Slot()
    def initialize(self):
        # Camera devices
        self._video_devices_group = QActionGroup(self)
        self._video_devices_group.setExclusive(True)
        self.updateCameras()
        self.m_devices.videoInputsChanged.connect(self.updateCameras)
        self._video_devices_group.triggered.connect(self.updateCameraDevice)
        self._ui.exposureCompensation.valueChanged.connect(self.setExposureCompensation)

        self.setCamera(QMediaDevices.defaultVideoInput())


    @Slot(QCameraDevice)
    def setCamera(self, cameraDevice):
        self.m_camera = QCamera(cameraDevice)
        self.m_captureSession.setCamera(self.m_camera)

        self.m_camera.activeChanged.connect(self.updateCameraActive)
        self.m_camera.errorOccurred.connect(self.displayCameraError)

        if not self.m_imageCapture:
            self.m_imageCapture = QImageCapture()
            self.m_captureSession.setImageCapture(self.m_imageCapture)
            self.m_imageCapture.readyForCaptureChanged.connect(self.readyForCapture)
            self.m_imageCapture.imageCaptured.connect(self.processCapturedImage)
            self.m_imageCapture.imageSaved.connect(self.imageSaved)
            self.m_imageCapture.errorOccurred.connect(self.displayCaptureError)

        self.m_captureSession.setVideoOutput(self._ui.viewfinder)

        self.updateCameraActive(self.m_camera.isActive())
        self.readyForCapture(self.m_imageCapture.isReadyForCapture())

        self.m_camera.start()


    @Slot()
    def displayCameraError(self):
        if self.m_camera.error() != QCamera.NoError:
            mboxStyle.warning(self, "Camera Error",
                                self.m_camera.errorString())


    @Slot(QAction)
    def updateCameraDevice(self, action):
        self.setCamera(QCameraDevice(action))


    @Slot(int)
    def setExposureCompensation(self, index):
        self.m_camera.setExposureCompensation(index * 0.5)


    ################################################################################
    # Camera Settings

    @Slot()
    def configureCaptureSettings(self):
        if self.m_doImageCapture:
            self.configureImageSettings()
    
    @Slot()
    def configureImageSettings(self):
        settings_dialog = ImageSettings(self.m_imageCapture)

        if settings_dialog.exec():
            settings_dialog.apply_image_settings()

    ################################################################################
    # Menu Bar Functions

    @Slot()
    def startCamera(self):
        self.m_camera.start()

    @Slot()
    def stopCamera(self):
        self.m_camera.stop()

    @Slot()
    def updateCameras(self):
        self._ui.menuDevices.clear()
        available_cameras = QMediaDevices.videoInputs()
        for cameraDevice in available_cameras:
            video_device_action = QAction(cameraDevice.description(),
                                          self._video_devices_group)
            video_device_action.setCheckable(True)
            video_device_action.setData(cameraDevice)
            if cameraDevice == QMediaDevices.defaultVideoInput():
                video_device_action.setChecked(True)

            self._ui.menuDevices.addAction(video_device_action)

    @Slot(bool)
    def updateCameraActive(self, active):
        if active:
            self._ui.actionStartCamera.setEnabled(False)
            self._ui.actionStopCamera.setEnabled(True)
            self._ui.actionSettings.setEnabled(True)
        else:
            self._ui.actionStartCamera.setEnabled(True)
            self._ui.actionStopCamera.setEnabled(False)
            self._ui.actionSettings.setEnabled(False)


    ################################################################################
    # Capture Functions
    def keyPressEvent(self, event):
            if event.isAutoRepeat():
                return
            key = event.key()
            if key == Qt.Key.Key_CameraFocus:
                self.displayViewfinder()
                event.accept()
            elif key == Qt.Key.Key_Camera:
                if self.m_doImageCapture:
                    self.takeImage()
                event.accept()
            else:
                super().keyPressEvent(event)


    @Slot(bool)
    def readyForCapture(self, ready):
        self._ui.takeImageButton.setEnabled(ready)


    @Slot()
    def takeImage(self):
        self._ui.takeImageButton.setEnabled(False)

        self.start_total_timer = time.time()
        self.m_isCapturingImage = True

        # Ensure directory exists before saving
        if not os.path.exists(self.image_folder):
            os.makedirs(self.image_folder, exist_ok=True)

        # Generate dynamic file path
        file_path = os.path.join(self.image_folder, f"{datetime.now().strftime("%Y%m%d%H%M%S")}.jpg")

        # Capture image to specified path
        self.m_imageCapture.captureToFile(QDir.toNativeSeparators(file_path)) 


    @Slot(int, QImageCapture.Error, str)
    def displayCaptureError(self, id, error, errorString):
        mboxStyle.warning(self, "Image Capture Error", errorString)
        self.m_isCapturingImage = False
    
    @Slot(int, QImage)
    def processCapturedImage(self, requestId, img):
        scaled_image = img.scaled(self._ui.viewfinder.size(),
                                  Qt.AspectRatioMode.KeepAspectRatio,
                                  Qt.TransformationMode.SmoothTransformation)

        self._ui.lastImagePreviewLabel.setPixmap(QPixmap.fromImage(scaled_image))

        # Display captured image for 1.5 seconds.
        self.displayCapturedImage()
        QTimer.singleShot(1000, self.displayViewfinder)
       

    @Slot()
    def displayCapturedImage(self):
        self._ui.stackedWidget.setCurrentIndex(1)


    @Slot()
    def displayViewfinder(self):
        self._ui.stackedWidget.setCurrentIndex(0)



    @Slot(int, str)
    def imageSaved(self, id, fileName):
        f = QDir.toNativeSeparators(fileName)
        self._ui.statusbar.showMessage(f"Captured \"{f}\"")

        self.m_isCapturingImage = False
        if self.m_applicationExiting:
            self.close()
        
        self._ui.web_latex.setHtml(self.loadhtml)
        self._ui.web_result.setHtml(self.loadhtml)
        self.finishedImageProcessing.emit(fileName)


        # Start background threads for processing after image is saved

    ################################################################################
    # OCR and AI Threads

    def OCRProcessing(self, file):
        print("OCR Processing Started.")

        self.ocr_thread = QThread()
        self.ocr_worker = OCRWorker(file)

        self.ocr_worker.moveToThread(self.ocr_thread)

        # Connect signals
        self.ocr_thread.started.connect(self.ocr_worker.run)
        self.ocr_worker.finished.connect(self.handleOCRSuccess)
        self.ocr_worker.error.connect(self.handleOCRError)

        # Ensure proper cleanup
        self.ocr_worker.finished.connect(self.cleanUpOCRThread)
        self.ocr_worker.error.connect(self.cleanUpOCRThread)

        # Start the OCR thread
        self.ocr_thread.start()

    def handleOCRSuccess(self, has_latex, ocr_time):
        self.has_latex = has_latex
        print(self.has_latex)

        if "The image does not contain any mathematical expression" not in self.has_latex:
            html_content = MathJaxSOL(self.has_latex)
            self._ui.web_latex.setHtml(html_content)
            self.GPTEvaluation()
        else:
            self._ui.web_latex.setHtml(self.clearhtml)
            self._ui.web_result.setHtml(self.clearhtml)
            mboxStyle.warning(self, "Solution Error", "The image does not contain any mathematical expression. Please try again")
            self._ui.label_check_time.setText("Solution checking runtime:\n 0.00s")
            self._ui.label_total_time.setText("Total runtime from capture to\nresult display:\n 0.00s")
            


        self._ui.label_ocr_time.setText(f"OCR processing runtime:\n{ocr_time: .2f}s")


    def handleOCRError(self, error_message):
        self._ui.web_latex.setHtml(self.clearhtml)
        self._ui.web_result.setHtml(self.clearhtml)
        
        mboxStyle.warning(self, "OCR Error", error_message)
        self._ui.takeImageButton.setEnabled(True)
        self._ui.takeImageButton.setText("Retake capture")

        self._ui.label_ocr_time.setText("OCR processing runtime:\n 0.00s")
        self._ui.label_check_time.setText("Solution checking runtime:\n 0.00s")
        self._ui.label_total_time.setText("Total runtime from capture to\nresult display:\n 0.00s")


    def cleanUpOCRThread(self):
        """Safely clean up the OCR thread"""
        if self.ocr_thread.isRunning():
            self.ocr_thread.quit()
            self.ocr_thread.wait()  # Ensure thread exits before deletion


    def GPTEvaluation(self):
        try:
            self.start_check_timer = time.time()
            result = self.eval.evaluate(self.fa_weight, self.ak_latex, self.has_latex)
            if result == None:
                print("resumed result")
                return  # Exit function until response comes
            else:
                self.result = result
                self.DisplayEval()
            
        except Exception as e:
            self._ui.web_result.setHtml(self.clearhtml)
            mboxStyle.warning(self, "Checking Error", str(e))


        self._ui.takeImageButton.setEnabled(True)
        self._ui.takeImageButton.setText("Retake capture")

    def ASMConfirmation(self):
        """ Executed in the main GUI thread when ASM is encountered. """
        response = mboxStyle.question(
            self,
            "Alternative Method Detected",
            "The solution has an Alternative Method used. Do you want to allow it?",
        )

        # Send the user’s response back to the worker thread
        if response == QMessageBox.Yes:
            print("User allowed ASM.")
            self.eval.asm_response_signal.emit("Yes, allow it.")  # Signal back to Evaluation
        else:
            print("User forbids ASM.")
            self.eval.asm_response_signal.emit("No, forbid it.")


    def ResumeEval(self, result):
        """ Continues the evaluation process after receiving ASM user response. """
        self.result = result  # Update result after ASM choice
        print("got the result!")
        # Now display results
        self.DisplayEval()


    def DisplayEval(self):

        html_content = MathJaxRes(str(self.result.display_full_result_or_ask_if_asm))
        self._ui.web_result.setHtml(html_content)
        self._ui.label_sol_grade.setText(f"Solution:\n{self.result.only_correct_over_total_values_from_sol_formula} = {self.result.sol_grade_integer}%")
        self._ui.label_fa_grade.setText(f"Final Answer:\n{self.result.fa_grade_integer}%")
        self._ui.label_overall_grade.setText(f"Overall:\n{self.result.overall_grade_integer}%")
        
        check_time = time.time() - self.start_check_timer
        self._ui.label_check_time.setText(f"Solution checking runtime:\n{check_time: .2f}s")

        total_time = time.time() - self.start_total_timer
        self._ui.label_total_time.setText(f"Total runtime from capture to\nresult display:\n{total_time: .2f}s")
        print("\n Total runtime: ", total_time)

        self._ui.push_save.setEnabled(True)


    ################################################################################
    # Save and Close window

    def saveToDatabase(self):
        self._ui.push_save.setEnabled(False)
        has_name = self._ui.edit_student_name.text().strip() or "Anonymous"

        session = Session()
        try:

            # Extract values safely
            result = self.result.display_full_result_or_ask_if_asm
            employed_asm = self.result.employed_asm
            sol_fraction = self.result.only_correct_over_total_values_from_sol_formula
            sol_grade = self.result.sol_grade_integer
            fa_grade = self.result.fa_grade_integer
            overall_grade = self.result.overall_grade_integer
            
            
            # Create a new StudentHAS entry
            student_has = StudentHAS(
                answer_key_id=self.answer_key_id,
                has_name = has_name,
                has_latex=self.has_latex,
                result=result,
                sol_fraction=sol_fraction,
                sol_grade=sol_grade,
                fa_grade=fa_grade,
                overall_grade=overall_grade,
                used_asm=employed_asm
            )

            # Add and commit the new entry
            session.add(student_has)
            session.commit()

            self.counter = session.query(StudentHAS).filter_by(answer_key_id=self.answer_key_id).count()

            #UI notifs
            self._ui.statusbar.showMessage("Handwritten solution record saved!")
            self._ui.takeImageButton.setText("Capture image")
            self._ui.label_counter.setText(f"No. of solution checked:\n {self.counter}")
            self._ui.label_last_name.setText(f"Last checked from:\n {has_name}")
            self._ui.edit_student_name.setText("")


        except Exception as e:
            # Rollback session if error occurs
            session.rollback()
            mboxStyle.critical(self, "Databas Error", f" Error saving StudentHAS: {str(e)}")
            self._ui.push_save.setEnabled(True)
            print(e)
        finally:
            # Close the session
            session.close()

    
    def backToSession(self):
        self.stopCamera()
        self.close()
        self.session_window.show()



    def closeEvent(self, event):
        if self.m_isCapturingImage:
            self.setEnabled(False)
            self.m_applicationExiting = True
            event.ignore()
        else:
            event.accept()


    ################################################################################
    # Miscellaneous

    def viewAnswerKey(self):
        dialog = AK_Dialog(self.answer_key_id, self.fa_weight, self.ak_latex)
        dialog.exec()  # Opens the dialog modally (blocks input to main window)

    def fetchStats(self):
        session = Session()
        try:
            self.counter = session.query(StudentHAS).filter_by(answer_key_id=self.answer_key_id).count()

            # Fetch the latest student's name based on the most recent submission
            latest_student = session.query(StudentHAS.has_name) \
                .filter_by(answer_key_id=self.answer_key_id) \
                .order_by(StudentHAS.created_at.desc()) \
                .first()
            
            self.last_checked_name = latest_student[0] if latest_student else "None"
        
        except SQLAlchemyError as e:
            print(f"🔴 Database Error: {e}")
            self.counter = 0
            self.last_checked_name = "None"
        
        finally:
            session.close()
            self._ui.label_counter.setText(f"No. of solution checked:\n {self.counter}")
            self._ui.label_last_name.setText(f"Last checked from:\n {self.last_checked_name}")

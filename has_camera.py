# Copyright (C) 2023 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause
from __future__ import annotations
"""PySide6 port of the QtMultiMedia camera example from Qt v6.x"""
import os
import sys
import re
from pathlib import Path
from datetime import datetime
import json
from PySide6.QtMultimedia import (QAudioInput, QCamera, QCameraDevice,
                                  QImageCapture, QMediaCaptureSession,
                                  QMediaDevices, QMediaMetaData,
                                  QMediaRecorder)
from PySide6.QtWidgets import QDialog, QMainWindow, QMessageBox, QApplication
from PySide6.QtGui import QAction, QActionGroup, QIcon, QImage, QPixmap
from PySide6.QtCore import (QDateTime, QDir, QTimer, Qt, Slot, qWarning, 
                            Signal, QObject, QRunnable, QThreadPool)
from imagesettings import ImageSettings
from has_camera_ui import Ui_Camera
from ocr import GeminiOCR
from evaluation import Evaluation, Response_for_HAS
from render_latex import MathJaxHTML
from database import engine


# ThreadPool instance for managing background tasks
threadpool = QThreadPool.globalInstance()

# Worker for LaTeX rendering
class LatexWorker(QRunnable):
    """Worker class to process LaTeX rendering using QRunnable in a thread pool."""
    def __init__(self, has_latex: str, callback):
        super().__init__()
        self.has_latex = has_latex
        self.callback = callback  # Callback function to update UI
    
    def __init__(self, has_latex:str):
        super().__init__()
        self.has_latex = has_latex  # path to the captured image to process
    
    @Slot()  # This slot will run in the worker thread
    def run(self):
        html_content = MathJaxHTML(self.has_latex)
        self.callback(html_content)  # Send result back to UI safely


class OutputWorker(QRunnable):
    """Worker class to evaluate student answers in a background thread."""
    def __init__(self, fa_weight, ak_latex, has_latex, callback):
        super().__init__()
        self.fa_weight = fa_weight
        self.ak_latex = ak_latex
        self.has_latex = has_latex
        self.callback = callback  # Callback function for UI update

    @Slot()
    def run(self):        
        try:
            # Call fine-tuned GPT-4o model
            result = Evaluation.evaluate(self.fa_weight, self.ak_latex, self.has_latex)

            html_content = MathJaxHTML(str(result.display_result_or_ask_if_asm))
            result_json = result.json()

            self.callback(html_content, result_json)

        except Exception as e:
            print(f"Error in OutputWorker: {str(e)}")  # Debugging
            self.callback("<html><body>Error: Could not process HAS.</body></html>", "{}")


class SaveStudentHASWorker(QRunnable):
    """Worker class for saving StudentHAS results to PostgreSQL asynchronously."""

    finished = Signal(bool)  # Signal to notify success or failure

    def __init__(self, answer_key_id, has_latex, result_json):
        super().__init__()
        self.answer_key_id = answer_key_id
        self.result_json = result_json  # Save data as a dictionary
        self.has_latex = has_latex
    def run(self):
        """Handles the database save operation in a background thread."""
        try:
            # Convert result JSON to dictionary
            result_dict = json.loads(self.result_json)

            # Extract values safely
            result = result_dict.get("display_result_or_ask_if_asm", "N/A")
            employed_asm = result_dict.get("employed_asm", False)
            sol_fraction = result_dict.get("sol_substituted_formula", "--")
            sol_grade = result_dict.get("sol_grade_integer", 0)
            fa_grade = result_dict.get("fa_grade_integer", 0)
            overall_grade = result_dict.get("overall_grade_integer", 0)

            # Get persistent database connection
            conn = engine()
            if conn:
                cursor = conn.cursor()

                # Insert data into StudentHAS table
                cursor.execute("""
                    INSERT INTO StudentHAS (answer_key_id, has_latex, result, sol_fraction, sol_grade, fa_grade, overall_grade, used_asm)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (self.answer_key_id, self.has_latex, result, sol_grade, fa_grade, overall_grade, employed_asm))

                conn.commit()  # Commit the transaction
                cursor.close()  # Close cursor
                self.finished.emit(True)

        except Exception as e:
            print(f"❌ Error saving StudentHAS: {str(e)}")
            self.finished.emit(False)


class HAS_Camera(QMainWindow):
    def __init__(self, id, fa_weight, ak_latex):
        super().__init__()

        # Attribute from AnswerKey table 
        self.answer_key_id = id
        self.fa_weight = fa_weight
        self.ak_latex = ak_latex

        self._video_devices_group = None
        self.m_devices = QMediaDevices()
        self.m_imageCapture = None
        self.m_captureSession = QMediaCaptureSession()
        self.m_camera = None
        self.m_mediaRecorder = None

        self.m_isCapturingImage = False
        self.m_applicationExiting = False
        self.m_doImageCapture = True

        self._ui = Ui_Camera()
        self._ui.setupUi(self)

        self.image_folder = os.path.join(os.getcwd(), "images", "has")
        os.makedirs(self.image_folder, exist_ok=True)  # Ensure the folder exists

        self._ui.actionAbout_Qt.triggered.connect(qApp.aboutQt)  # noqa: F821

        # disable all buttons by default
        self.updateCameraActive(False)
        self.readyForCapture(False)
        self.saveToDatabase(False)
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
            QMessageBox.warning(self, "Camera Error",
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
        QMessageBox.warning(self, "Image Capture Error", errorString)
        self.m_isCapturingImage = False
    
    @Slot(int, QImage)
    def processCapturedImage(self, requestId, img):
        scaled_image = img.scaled(self._ui.viewfinder.size(),
                                  Qt.AspectRatioMode.KeepAspectRatio,
                                  Qt.TransformationMode.SmoothTransformation)

        self._ui.lastImagePreviewLabel.setPixmap(QPixmap.fromImage(scaled_image))

        # Display captured image for 4 seconds.
        self.displayCapturedImage()
        QTimer.singleShot(4000, self.displayViewfinder)


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

        # Start background threads for processing after image is saved
        self.OCRProcessing(f)


    ################################################################################
    # OCR and AI Threads

    def OCRProcessing(self, file):         
        self.has_latex = GeminiOCR(file)
        print(self.has_latex)
        self.startLatexThread(self.has_latex)
        self.startOutputThread(self.fa_weight, self.ak_latex, self.has_latex)

    def startLatexThread(self, has_latex):
        """Launch LaTeX processing thread efficiently."""
        worker = LatexWorker(has_latex, self.onLatexResult)
        threadpool.start(worker)  # Use thread pool

    @Slot(str)
    def onLatexResult(self, html_content):
        self._ui.web_latex.setHtml(html_content)

    def startOutputThread(self, fa_weight, ak_latex, has_latex):
        worker = OutputWorker(fa_weight, ak_latex, has_latex, self.onFrameResult)
        threadpool.start(worker)  # Use thread pool

    @Slot(str, str)
    def onFrameResult(self, html_content, result_json: str):
        #Slot to receive LaTeX result from LatexWorker (executed in main thread).
        self._ui.web_result.setHtml(html_content)

        self.result_json = result_json
        result_dict = json.loads(result_json)  # Convert JSON string back to dictionary
        sol_fraction = result_dict.get("sol_substituted_formula", "--")
        sol_grade = result_dict.get("sol_grade_integer", 0)
        fa_grade = result_dict.get("fa_grade_integer", 0)
        overall_grade = result_dict.get("overall_grade_integer", 0)

        self._ui.label_sol_grade.setText(f"Solution:\n&nbsp;{sol_fraction} = {sol_grade}%")
        self._ui.label_fa_grade.setText(f"Final Answer:\n&nbsp;&nbsp;{fa_grade}% (/{self.fa_weight}%)")
        self._ui.label_overall_grade.setText(f"Overall:\n&nbsp;&nbsp;{overall_grade}%")

        self._ui.takeImageButton.setEnabled(True)
        self._ui.push_save.setEnabled(True)


    ################################################################################
    # Save and Close window

    def saveToDatabase(self):
        self._ui.push_save.setEnabled(False)
        """Runs a worker thread to save StudentHAS data when 'Save' is clicked."""
        worker = SaveStudentHASWorker(self.answer_key_id, self.result_json)
        worker.finished.connect(self.onSaveCompleted)  # Handle completion feedback
        threadpool.start(worker)

    @Slot(bool)
    def onSaveCompleted(self, success):
        """Handles UI updates after the save operation."""
        if success:
            self._ui.statusbar.showMessage("Handwritten solution record saved!")
        else:
            self._ui.statusbar.showMessage("Error: Failed to save StudentHAS record.")
        
        self._ui.push_save.setEnabled(True)

    
    def backToSession(self):
        print("This function is curently under maintenance")


    def closeEvent(self, event):
        if self.m_isCapturingImage:
            self.setEnabled(False)
            self.m_applicationExiting = True
            event.ignore()
        else:
            event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    camera = HAS_Camera()
    camera.show()
    sys.exit(app.exec())
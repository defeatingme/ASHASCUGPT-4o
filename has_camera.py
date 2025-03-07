# Copyright (C) 2023 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause
from __future__ import annotations
"""PySide6 port of the QtMultiMedia camera example from Qt v6.x"""
import os
import sys
from pathlib import Path
from PySide6.QtMultimedia import (QAudioInput, QCamera, QCameraDevice,
                                  QImageCapture, QMediaCaptureSession,
                                  QMediaDevices, QMediaMetaData,
                                  QMediaRecorder)
from PySide6.QtWidgets import QDialog, QMainWindow, QMessageBox, QApplication
from PySide6.QtGui import QAction, QActionGroup, QIcon, QImage, QPixmap
from PySide6.QtCore import (QDateTime, QDir, QTimer, Qt, Slot, qWarning, 
                            Signal, QObject, QThread)
from imagesettings import ImageSettings
from has_camera_ui import Ui_Camera
from database import engine
from ocr import GeminiOCR
from latex_render import MathJaxApp
import time

# Worker for LaTeX rendering
class LatexWorker(QObject):
    """Worker object to perform LaTeX rendering on a background thread."""
    # Define signals to communicate with the main thread
    resultReady = Signal(str)        # will emit the LaTeX string or image path
    finished   = Signal()           # emits when work is done (to clean up thread)
    
    def __init__(self, raw_latex:str):
        super().__init__()
        self.raw_latex = raw_latex  # path to the captured image to process
    
    @Slot()  # This slot will run in the worker thread
    def run(self):
        # Heavy operation: process the image to extract or render LaTeX
        # (For example, OCR or compute LaTeX. Here we simulate with placeholder text.)
        html_content = f"""
        <html>
            <head><script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script></head>
            <body style="background-color: #333; color: #eee;">
                <h3>Rendered LaTeX:</h3>
                $$ {self.raw_latex} $$
            </body>
        </html>"""
        self.resultReady.emit(html_content)
        self.finished.emit()
    
        latex_result = f"\\(Processed: {self.raw_latex}\\)"  # placeholder LaTeX string
        # Emit the result to the main thread
        self.resultReady.emit(latex_result)
        # Emit finished signal to indicate the thread can stop
        self.finished.emit()


class WebWorker(QObject):
    resultReady = Signal(str)
    finished = Signal()

    def __init__(self, raw_latex):
        super().__init__()
        self.raw_latex = raw_latex

    @Slot()
    def run(self):
        html_content = f"""
        <html>
            <head><script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script></head>
            <body style="background-color: #333; color: #eee;">
                <h3>Rendered LaTeX:</h3>
                $$ {self.latex_str} $$
            </body>
        </html>"""
        self.resultReady.emit(html_content)
        self.finished.emit()


class HAS_Camera(QMainWindow):
    def __init__(self, id):
        super().__init__()

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

        self.image_counter = 1  # Start image counter
        self.image_folder = os.path.join(os.getcwd(), "images", "answerkey")
        os.makedirs(self.image_folder, exist_ok=True)  # Ensure the folder exists
        self._ui.actionAbout_Qt.triggered.connect(qApp.aboutQt)  # noqa: F821

        # disable all buttons by default
        self.updateCameraActive(False)
        self.readyForCapture(False)

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
            #self._ui.captureFrame.setEnabled(True)
            self._ui.actionSettings.setEnabled(True)
        else:
            self._ui.actionStartCamera.setEnabled(True)
            self._ui.actionStopCamera.setEnabled(False)
            #self._ui.captureFrame.setEnabled(False)
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
        self.m_isCapturingImage = True
        
        # Ensure directory exists before saving
        if not os.path.exists(self.image_folder):
            os.makedirs(self.image_folder, exist_ok=True)

        # Generate dynamic file path
        file_path = os.path.join(self.image_folder, f"image{self.image_counter}.jpg")
        self.image_counter += 1  # Increment image number for next capture
        
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

    def OCRProcessing(self, file):
        raw_latex = GeminiOCR(file)
        print(raw_latex)
        self.startLatexThread(raw_latex)
        self.startWebThread(raw_latex)

    ################################################################################
    # Threads


    def startLatexThread(self, raw_latex):
        """Launch a thread to process LaTeX rendering for the given image."""
        # Create worker and thread for LaTeX processing
        self.latexWorker = LatexWorker(raw_latex)
        self.latexThread = QThread(self)  # make thread a child of main window (for automatic cleanup)
        self.latexWorker.moveToThread(self.latexThread)
        # When thread starts, call worker.run
        self.latexThread.started.connect(self.latexWorker.run)
        # Connect worker signals back to main UI slots
        self.latexWorker.resultReady.connect(self.onLatexResult)     # handle result in main thread
        self.latexWorker.finished.connect(self.latexThread.quit)
        self.latexWorker.finished.connect(self.latexWorker.deleteLater)
        self.latexThread.finished.connect(self.latexThread.deleteLater)
        # Start the thread (will emit started, triggering worker.run)
        self.latexThread.start()

    @Slot(str)
    def onLatexResult(self, latex_str:str):
        """Slot to receive LaTeX result from LatexWorker (executed in main thread)."""
        # Update the QLabel (solution) in the UI with the LaTeX output
        self._ui.label_latex.setText(latex_str)
        # Optionally, if latex_str is raw LaTeX, we could format it or display an image.
        # Ensure this update happens in main thread (which it does, because this is a Qt slot).

        # After getting LaTeX, start the other threads for web rendering and DB operations
        #self.startDbThread(self.currentImagePath, latex_str)  # using stored current image path

    def startWebThread(self, latex_str):
        self.webWorker = WebWorker(latex_str)
        self.webThread = QThread(self)
        self.webWorker.moveToThread(self.webThread)
        self.webThread.started.connect(self.webWorker.run)
        self.webWorker.resultReady.connect(self.onWebResult)
        self.webWorker.finished.connect(self.webThread.quit)
        self.webWorker.finished.connect(self.webWorker.deleteLater)
        self.webThread.finished.connect(self.webThread.deleteLater)
        self.webThread.start()

    @Slot(str)
    def onWebResult(self, html_content):
        self._ui.web_result.setHtml(html_content)


    ################################################################################
    # Close window

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

import sys
import cv2
import os
import time
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QPixmap, QImage

class CameraThread(QThread):
    """Thread to capture video frames from the camera."""
    frame_signal = pyqtSignal(QImage)

    def __init__(self):
        super().__init__()
        self.running = True
        self.cap = cv2.VideoCapture(0)

    def run(self):
        """Continuously capture frames from the webcam."""
        while self.running and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = frame.shape
                bytes_per_line = ch * w
                q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
                self.frame_signal.emit(q_img)

    def stop(self):
        """Stop the camera thread and release the webcam."""
        self.running = False
        self.cap.release()
        self.quit()

class AK_Camera(QWidget):
    def __init__(self, session_window):
        super().__init__()

        self.session_window = session_window
        self.image_path = None
        self.latex_code = ""

        # Window settings
        self.setWindowTitle("Capture Answer Key")
        self.setGeometry(200, 100, 1080, 720)
        self.setStyleSheet("background-color: #8c818a;")

        # Camera Feed (Left Side)
        self.camera_label = QLabel(self)
        self.camera_label.setFixedSize(600, 600)
        self.camera_label.setStyleSheet("border: 2px solid #6A0DAD; background-color: black;")

        # LaTeX Rendered Image (Right Side)
        self.latex_label = QLabel("Answer Key in LaTeX", self)
        self.latex_label.setStyleSheet("font-size: 18px; color: #6A0DAD; font-weight: bold;")
        self.latex_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.latex_image_label = QLabel(self)
        self.latex_image_label.setFixedSize(360, 480)  # Corrected Size
        self.latex_image_label.setStyleSheet("border: 2px solid black; background-color: white;")

        # Buttons
        self.btn_back = QPushButton("Back", self)
        self.btn_back.setFixedSize(180, 48)
        self.btn_back.setStyleSheet("background-color: #333; color: white; font-size: 14px; font-weight: bold;")
        self.btn_back.clicked.connect(self.go_back)

        self.btn_capture = QPushButton("Capture", self)
        self.btn_capture.setFixedSize(180, 48)
        self.btn_capture.setStyleSheet("background-color: #333; color: white; font-size: 14px; font-weight: bold;")
        self.btn_capture.clicked.connect(self.capture_image)

        self.btn_retake = QPushButton("Retake", self)
        self.btn_retake.setFixedSize(180, 48)
        self.btn_retake.setEnabled(False)
        self.btn_retake.setStyleSheet("background-color: #333; color: white; font-size: 14px; font-weight: bold;")
        self.btn_retake.clicked.connect(self.retake_image)

        self.btn_submit = QPushButton("Submit", self)
        self.btn_submit.setFixedSize(240, 48)
        self.btn_submit.setEnabled(False)
        self.btn_submit.setStyleSheet("background-color: #333; color: white; font-size: 14px; font-weight: bold;")
        self.btn_submit.clicked.connect(self.submit_image)

        # Layout Setup
        layout_main = QHBoxLayout()
        layout_main.addWidget(self.camera_label)
        
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.latex_label)
        right_layout.addWidget(self.latex_image_label)
        layout_main.addLayout(right_layout)

        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.btn_back)
        layout_buttons.addWidget(self.btn_capture)
        layout_buttons.addWidget(self.btn_retake)
        layout_buttons.addWidget(self.btn_submit)

        layout = QVBoxLayout()
        layout.addLayout(layout_main)
        layout.addLayout(layout_buttons)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

        # Start Camera Thread
        self.camera_thread = CameraThread()
        self.camera_thread.frame_signal.connect(self.update_camera_frame)
        self.camera_thread.start()

    def update_camera_frame(self, q_img):
        """Updates the camera display."""
        pixmap = QPixmap.fromImage(q_img)
        self.camera_label.setPixmap(pixmap.scaled(600, 600, Qt.AspectRatioMode.KeepAspectRatio))

    def capture_image(self):
        """Captures an image, shows loading, and displays the saved image."""
        self.btn_capture.setEnabled(False)

        # Show loading animation
        self.camera_label.setText("📷 Saving Image...")
        QApplication.processEvents()
        time.sleep(1)

        # Capture Image
        ret, frame = self.camera_thread.cap.read()
        if ret:
            self.image_path = "images/answerkey/captured_ak.jpg"
            os.makedirs(os.path.dirname(self.image_path), exist_ok=True)
            cv2.imwrite(self.image_path, frame)

            # Display saved image
            pixmap = QPixmap(self.image_path)
            self.camera_label.setPixmap(pixmap.scaled(600, 600, Qt.AspectRatioMode.KeepAspectRatio))

            # Generate LaTeX Rendering
            self.generate_latex_image()

            # Enable Retake & Submit
            self.btn_retake.setEnabled(True)
            self.btn_submit.setEnabled(True)

    def generate_latex_image(self):
        """Generates a LaTeX rendered image using Matplotlib."""
        latex_code = r"360 \times 480 \text{frame for rendered LaTeX}"
        self.latex_code = latex_code

        fig, ax = plt.subplots(figsize=(4, 5))  # Corrected aspect ratio
        ax.text(0.5, 0.5, latex_code, fontsize=20, ha='center', va='center')
        ax.set_axis_off()
        plt.savefig("images/answerkey/latex_render.png", dpi=200, bbox_inches='tight', transparent=True)
        plt.close()

        # Display the rendered image
        pixmap = QPixmap("images/answerkey/latex_render.png")
        self.latex_image_label.setPixmap(pixmap.scaled(360, 480, Qt.AspectRatioMode.KeepAspectRatio))

    def retake_image(self):
        """Deletes captured image and returns to camera view."""
        if self.image_path and os.path.exists(self.image_path):
            os.remove(self.image_path)

        self.camera_label.setText("")
        self.latex_image_label.clear()
        self.btn_capture.setEnabled(True)
        self.btn_retake.setEnabled(False)
        self.btn_submit.setEnabled(False)

    def submit_image(self):
        """Sends the image and LaTeX to SessionWindow, then closes."""
        if self.session_window:
            self.session_window.update_answer_key(self.image_path, self.latex_code)
        self.camera_thread.stop()
        self.close()

    def go_back(self):
        """Returns to previous window."""
        self.camera_thread.stop()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AK_Camera(None)
    window.show()
    sys.exit(app.exec())

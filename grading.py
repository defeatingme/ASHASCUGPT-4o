import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QFileDialog, QLineEdit, QMessageBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from grading_ui import Ui_Session
from database import engine, setup_AnswerKey, setup_StudentHAS
#from home import HomeWindow

class SessionWindow(QWidget):
    def __init__(self, session_id, instructor_name):
        super().__init__()

        # Setup database on startup
        setup_AnswerKey()
        setup_StudentHAS()

        self.session_id = session_id
        self.instructor_name = instructor_name
        self.image_path = None
        self.ak_latex = ""

        self._ui = Ui_Session()
        self._ui.setupUi(self)

        self.setWindowTitle(f"Session {session_id} - Algeval")
        self._ui.label_session.setText(f"Session: {session_id}")
        self._ui.label_instructor.setText(f"by: {instructor_name}")

        self._ui.push_camera.clicked.connect(self.open_camera)
        self._ui.push_computer.clicked.connect(self.upload_from_computer)
        self._ui.push_save.clicked.connect(self.save_answer_key)
        self._ui.push_start.clicked.connect(self.start_has_checking)
        self._ui.push_back.clicked.connect(self.go_back)
        
    def open_camera(self):
        """Opens the Camera Window."""
        from camera_test import Camera
        self.camera_window = Camera()
        self.camera_window.show()

    def upload_from_computer(self):
        """Opens file explorer to upload an image."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Answer Key Image", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            self.image_path = file_path
            self.display_image(file_path)
            self.ak_latex = r"\frac{a}{b} + c"
            self._ui.label_latex.setText(f"Rendered LaTeX Code:\n{self.ak_latex}")

    def display_image(self, file_path):
        """Displays the selected image in QLabel."""
        pixmap = QPixmap(file_path)
        self._ui.label_image.setPixmap(pixmap.scaled(180, 180, Qt.AspectRatioMode.KeepAspectRatio))

    def save_answer_key(self):
        """Saves the answer key to the database."""
        print("Answer key saved!")

    def start_has_checking(self):
        print("Opening HAS Checking Window...")

    def go_back(self):
        pass
        # Open Home Window
        #self.home_window = HomeWindow(instructor_name)
        #self.home_window.show()
        #self.close()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SessionWindow("sess_001", "Dr. Smith")
    window.show()
    sys.exit(app.exec())

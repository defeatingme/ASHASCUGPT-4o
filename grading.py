import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QFileDialog, QLineEdit, QMessageBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QDoubleValidator
from grading_ui import Ui_Session
from database import engine, setup_AnswerKey, setup_StudentHAS
from ak_camera import AK_Camera
from has_camera import HAS_Camera
from ocr import GeminiOCR

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

        validator = QDoubleValidator(1.0, 100.0, 2)  # Min: 1.0, Max: 100.0, 2 decimal places
        validator.setNotation(QDoubleValidator.StandardNotation)  # Normal float format

        # Apply validator to the input field
        self._ui.edit_fa_weight.setValidator(validator)

        self._ui.push_camera.clicked.connect(self.open_camera)
        self._ui.push_computer.clicked.connect(self.upload_from_computer)
        self._ui.push_save.clicked.connect(self.save_answer_key)
        self._ui.push_start.clicked.connect(self.start_has_checking)
        self._ui.push_back.clicked.connect(self.go_back)
        

    def open_camera(self):
        """Opens the Camera Window."""
        #self.AK_camera = AK_Camera()
        #self.AK_camera.show()
        print("This function is curently under maintenance")


    def upload_from_computer(self):
        """Opens file explorer to upload an image."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Answer Key Image", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            self.image_path = file_path
            self.display_image(file_path)
            self.ak_latex = GeminiOCR(file_path)
            print(self.ak_latex)           
            #self._ui.label_latex.setText(f"Rendered LaTeX Code:\n{self.ak_latex}")


    def display_image(self, file_path):
        """Displays the selected image in QLabel."""
        pixmap = QPixmap(file_path)
        self._ui.label_image.setPixmap(pixmap.scaled(180, 180, Qt.AspectRatioMode.KeepAspectRatio))


    def save_answer_key(self):
        """Saves the answer key to the database."""
        self.fa_weight = self._ui.edit_fa_weight.text().strip() or 20
        self.fa_weight = float(self.fa_weight)
        
        if "ak_latex" == ("" or "The image does not contain any mathematical expression."):
            QMessageBox.warning(self, "Error", "No LaTeX code detected. Please upload an answer key image first.")
            return
        
        sol_weight = 100 - self.fa_weight
        conn = engine()
        if conn:
            try:
                cursor = conn.cursor()
                # Insert new session
                cursor.execute("""
                    INSERT INTO AnswerKey (session_id, sol_weight, fa_weight, ak_latex)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id;
                """, (self.session_id, sol_weight, self.fa_weight, self.ak_latex))

                self.answer_key_id = cursor.fetchone()["id"]

                # Commit changes and close the connection
                conn.commit()
                conn.close()

                QMessageBox.information(self, "Success", f"Answer key saved successfully! ID: {self.answer_key_id}")

            except Exception as e:
                QMessageBox.critical(self, "Database Error", f"Failed to save answer key: {e}")

        print("Answer key saved!")


    def start_has_checking(self):
        """Starts the HAS checking window using the latest answer key ID."""        
        if not hasattr(self, "answer_key_id"):
            QMessageBox.warning(self, "Error", "No answer key has been saved. Please save one first.")
            return

        # Open HAS_Camera with the new answer key ID
        self.has_camera = HAS_Camera(self.answer_key_id, self.fa_weight, self.ak_latex)
        self.has_camera.show()
        self.hide()


    def go_back(self):
        print("This function is curently under maintenance")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SessionWindow("sess_001", "Dr. Smith")
    window.show()
    sys.exit(app.exec())

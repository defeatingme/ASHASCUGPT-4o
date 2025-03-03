import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QFileDialog, QLineEdit, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from database import engine, setup_AnswerKey, setup_StudentHAS

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

        # Window settings
        self.setWindowTitle(f"Session - {session_id}")
        self.setGeometry(100, 100, 1080, 720)
        self.setStyleSheet("background-color: #6e656a;")

        # --- Session Info (Top-Left) ---
        session_info_layout = QVBoxLayout()
        self.label_session = QLabel(f"Session ID: {self.session_id}", self)
        self.label_session.setStyleSheet("font-size: 32px; color: white; font-weight: bold;")

        self.label_instructor = QLabel(f"by: {self.instructor_name}", self)
        self.label_instructor.setStyleSheet("font-size: 16px; color: white; font-style: italic;")

        session_info_layout.addWidget(self.label_session)
        session_info_layout.addWidget(self.label_instructor)
        session_info_layout.addSpacing(20)

        # --- Submit Answer Key Section (Center) ---
        self.label_submit = QLabel("Submit Answer Key File", self)
        self.label_submit.setStyleSheet("font-size: 24px; color: white; font-weight: bold; text-decoration: underline;")
        self.label_submit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.btn_camera = QPushButton("📷 Open Camera", self)
        self.btn_camera.setFixedSize(180, 48)
        self.btn_camera.setStyleSheet("background-color: black; color: white; font-size: 14px;")
        self.btn_camera.clicked.connect(self.open_camera)

        self.btn_upload = QPushButton("🖥 From Computer", self)
        self.btn_upload.setFixedSize(180, 48)
        self.btn_upload.setStyleSheet("background-color: black; color: white; font-size: 14px;")
        self.btn_upload.clicked.connect(self.upload_from_computer)

        submit_btn_layout = QVBoxLayout()
        submit_btn_layout.addWidget(self.label_submit)
        submit_btn_layout.addWidget(self.btn_camera, alignment=Qt.AlignmentFlag.AlignCenter)
        submit_btn_layout.addWidget(self.btn_upload, alignment=Qt.AlignmentFlag.AlignCenter)

        # --- Final Answer Weight Input (Below Submission) ---
        self.label_fa_weight = QLabel("Final Answer Weight (%)\ndefault: 80", self)
        self.label_fa_weight.setStyleSheet("font-size: 16px; color: white; text-align: center;")

        self.fa_weight_input = QLineEdit(self)
        self.fa_weight_input.setFixedSize(80, 30)
        self.fa_weight_input.setStyleSheet("border: 1px solid black; font-size: 16px; background-color: white;")
        self.fa_weight_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fa_weight_input.setText("80")  # Default value

        weight_layout = QVBoxLayout()
        weight_layout.addWidget(self.label_fa_weight, alignment=Qt.AlignmentFlag.AlignCenter)
        weight_layout.addWidget(self.fa_weight_input, alignment=Qt.AlignmentFlag.AlignCenter)

        # --- Image Preview (Top-Right) ---
        self.image_label = QLabel("Image Preview\n180x180", self)
        self.image_label.setFixedSize(180, 180)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("border: 2px solid #A020F0; background-color: #AAA; color: black;")

        # --- LaTeX Preview (Below Image Preview) ---
        self.latex_label = QLabel(" text{rendered LaTeX Preview}\n180 times 240", self)
        self.latex_label.setFixedSize(180, 240)
        self.latex_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.latex_label.setStyleSheet("border: 2px solid black; background-color: white; color: black;")

        preview_layout = QVBoxLayout()
        preview_layout.addWidget(self.image_label, alignment=Qt.AlignmentFlag.AlignCenter)
        preview_layout.addWidget(self.latex_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # --- Bottom Buttons (Save, Start Checking, Back to Home) ---
        self.btn_save = QPushButton("💾 Save", self)
        self.btn_save.setFixedSize(180, 48)
        self.btn_save.setStyleSheet("background-color: black; color: white; font-size: 14px;")
        self.btn_save.clicked.connect(self.save_answer_key)

        self.btn_start_has = QPushButton("🚀 Start Checking", self)
        self.btn_start_has.setFixedSize(240, 48)
        self.btn_start_has.setStyleSheet("background-color: black; color: white; font-size: 14px;")
        self.btn_start_has.clicked.connect(self.start_has_checking)

        self.btn_back = QPushButton("⬅ Back to Home", self)
        self.btn_back.setFixedSize(180, 48)
        self.btn_back.setStyleSheet("background-color: black; color: white; font-size: 14px;")
        self.btn_back.clicked.connect(self.go_back)

        btn_bottom_layout = QHBoxLayout()
        btn_bottom_layout.addWidget(self.btn_back)
        btn_bottom_layout.addWidget(self.btn_save)
        btn_bottom_layout.addWidget(self.btn_start_has)

        # --- Main Layout (Aligning All Sections) ---
        main_layout = QHBoxLayout()

        left_layout = QVBoxLayout()
        left_layout.addLayout(session_info_layout)
        left_layout.addSpacing(30)
        left_layout.addLayout(submit_btn_layout)
        left_layout.addSpacing(15)
        left_layout.addLayout(weight_layout)

        right_layout = QVBoxLayout()
        right_layout.addLayout(preview_layout)

        center_layout = QVBoxLayout()

        main_layout.addLayout(left_layout)
        main_layout.addLayout(center_layout)
        main_layout.addLayout(right_layout)

        final_layout = QVBoxLayout()
        final_layout.addLayout(main_layout)
        final_layout.addSpacing(30)
        final_layout.addLayout(btn_bottom_layout)

        self.setLayout(final_layout)

    def open_camera(self):
        """Opens the Camera Window."""
        from ak_camera import CameraWindow
        self.camera_window = CameraWindow(self)
        self.camera_window.show()

    def upload_from_computer(self):
        """Opens file explorer to upload an image."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Answer Key Image", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            self.image_path = file_path
            self.display_image(file_path)
            self.ak_latex = r"\frac{a}{b} + c"
            self.latex_label.setText(f"Rendered LaTeX Code:\n{self.ak_latex}")

    def display_image(self, file_path):
        """Displays the selected image in QLabel."""
        pixmap = QPixmap(file_path)
        self.image_label.setPixmap(pixmap.scaled(180, 180, Qt.AspectRatioMode.KeepAspectRatio))

    def save_answer_key(self):
        """Saves the answer key to the database."""
        print("Answer key saved!")

    def start_has_checking(self):
        print("Opening HAS Checking Window...")

    def go_back(self):
        print("Returning to Home Screen...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SessionWindow("sess_001", "Dr. Smith")
    window.show()
    sys.exit(app.exec())

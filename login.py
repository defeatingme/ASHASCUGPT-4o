import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QListWidget
from PyQt6.QtCore import Qt
from database import engine, setup_Instructor, setup_Sessions

class WelcomeWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Setup database on startup
        setup_Instructor()
        setup_Sessions()

        # Window settings
        self.setWindowTitle("ALGEVAL - Welcome")
        self.setGeometry(100, 100, 720, 480)
        self.setFixedSize(720, 480)
        self.setStyleSheet("background-color: #9A9298;")

        # UI Elements (Now Centered)
        self.label_title = QLabel("Welcome to", self)
        self.label_title.setStyleSheet("font-size: 24px; color: #6A0DAD;")
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_logo = QLabel("A  L  G  E  V  A  L", self)
        self.label_logo.setStyleSheet("font-size: 64px; font-weight: bold; color: #4B0082;")
        self.label_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_desc = QLabel("A Step-by-step Handwritten Algebraic Solution Checker\nusing GPT-4o.", self)
        self.label_desc.setStyleSheet("font-size: 12px; color: white;")
        self.label_desc.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Input Fields
        self.input_name = QLineEdit(self)
        self.input_name.setPlaceholderText("Enter your name (Anonymous by default)")
        self.input_name.setStyleSheet("padding: 8px; border-radius: 5px; border: 1px solid #999; background-color: white")

        self.input_email = QLineEdit(self)
        self.input_email.setPlaceholderText("Enter your email (Optional)")
        self.input_email.setStyleSheet("padding: 8px; border-radius: 5px; border: 1px solid #999; background-color: white")

        self.input_department = QLineEdit(self)
        self.input_department.setPlaceholderText("Enter your department (Optional)")
        self.input_department.setStyleSheet("padding: 8px; border-radius: 5px; border: 1px solid #999; background-color: white")

        # Start Button
        self.btn_start = QPushButton("START", self)
        self.btn_start.setStyleSheet("background-color: #6A0DAD; color: white; font-size: 14px; padding: 8px; ")
        self.btn_start.clicked.connect(self.start_application)

        # Layout (Now Centralized)
        layout = QVBoxLayout()
        layout.addWidget(self.label_title)
        layout.addWidget(self.label_logo)
        layout.addWidget(self.label_desc)
        layout.addSpacing(64)
        layout.addWidget(self.input_name)
        layout.addWidget(self.input_email)
        layout.addWidget(self.input_department)
        layout.addWidget(self.btn_start)

        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

    def start_application(self):
        """Store instructor details and open the Home Window."""
        instructor_name = self.input_name.text().strip() or "Anonymous"
        instructor_email = self.input_email.text().strip() or None
        instructor_department = self.input_department.text().strip() or None

        # Store instructor in database
        self.store_instructor(instructor_name, instructor_email, instructor_department)

        # Open Home Window
        from home import HomeWindow
        self.home_window = HomeWindow(instructor_name)
        self.home_window.show()
        self.close()

        print(f"Instructor: {instructor_name} | Email: {instructor_email} | Department: {instructor_department}")

    def store_instructor(self, name, email, department):
        """Insert instructor details into PostgreSQL."""
        conn = engine()
        if conn:
            try:
                cursor = conn.cursor()

                # Insert instructor only if not exists
                cursor.execute("""
                    INSERT INTO Instructor (instructor_name, email, department)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (instructor_name) DO NOTHING
                """, (name, email, department))

                conn.commit()
                conn.close()
            except Exception as e:
                print(f"Database Error (Instructor): {e}")

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WelcomeWindow()
    window.show()
    sys.exit(app.exec())

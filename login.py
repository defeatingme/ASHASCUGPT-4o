import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt
from login_ui import Ui_Login
from database import engine, setup_Instructor, setup_Sessions
from home import HomeWindow

class Login(QWidget):
    def __init__(self):
        super().__init__()

        # Setup database on startup
        setup_Instructor()
        setup_Sessions()

        self._ui = Ui_Login()
        self._ui.setupUi(self)
        
        #enter function
        self._ui.push_enter.clicked.connect(self.start_application)

    def start_application(self):
        """Store instructor details and open the Home Window."""
        instructor_name = self._ui.edit_name.text().strip() or "Anonymous"
        instructor_email = self._ui.edit_email.text().strip() or None
        instructor_department = self._ui.edit_dept.text().strip() or None

        # Store instructor in database
        self.store_instructor(instructor_name, instructor_email, instructor_department)

        # Open Home Window
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
    window = Login()
    window.show()
    sys.exit(app.exec())

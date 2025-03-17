import sys
from PySide6.QtWidgets import QWidget, QPushButton
#from PySide6.QtGui import QPixmap
#from PySide6.QtCore import Qt
from login_ui import Ui_Login
from styles import buttonStyle, mboxStyle
from database import Session, Instructor
from home import HomeWindow

class Login(QWidget):
    def __init__(self):
        super().__init__()

        self._ui = Ui_Login()
        self._ui.setupUi(self)

        for button in self.findChildren(QPushButton):
            button.setStyleSheet(buttonStyle)

        # Connect button to function
        self._ui.push_enter.clicked.connect(self.start_application)

    def start_application(self):
        """Store instructor details and open the Home Window."""
        instructor_name = self._ui.edit_name.text().strip() or "Anonymous"
        email = self._ui.edit_email.text().strip() or None
        department = self._ui.edit_dept.text().strip() or None

        # Store instructor using SQLAlchemy ORM
        self.store_instructor(instructor_name, email, department)

        # Open Home Window
        self.home_window = HomeWindow(self,instructor_name)
        self.home_window.show()
        self.close()

        print(f"Instructor: {instructor_name} | Email: {email} | Department: {department}")

    def store_instructor(self, name, email, department):
        """Insert instructor details using SQLAlchemy."""
        session = Session()  # Create a new SQLAlchemy session
        try:
            # Check if instructor already exists
            existing_instructor = session.query(Instructor).filter_by(instructor_name=name).first()
            if not existing_instructor:
                new_instructor = Instructor(
                    instructor_name=name,
                    email=email,
                    department=department
                )
                session.add(new_instructor)
                session.commit()
                print("Instructor added successfully.")
            else:
                print("Instructor already exists. Skipping insertion.")

        except Exception as e:
            session.rollback()  # Rollback in case of error
            mboxStyle.critical(self, "Database Error (Instructor)", str(e))
        finally:
            session.close()  # Always close the session

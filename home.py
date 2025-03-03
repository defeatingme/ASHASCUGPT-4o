import sys
import uuid
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QListWidget
from PyQt6.QtCore import Qt
from database import engine
from grading import SessionWindow  # Import SessionWindow

class HomeWindow(QWidget):
    def __init__(self, instructor_name):
        super().__init__()

        self.instructor_name = instructor_name

        # Window settings
        self.setWindowTitle("ALGEVAL - Home")
        self.setGeometry(100, 100, 1080, 720)
        #self.setStyleSheet("background-color: #6e656a;")  # Keep main color

        # UI Elements
        self.label_title = QLabel(f"Welcome, {self.instructor_name}!", self)
        self.label_title.setStyleSheet("font-size: 24px; color: #6A0DAD; font-weight: bold;")
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_sessions = QLabel("Your Sessions", self)
        self.label_sessions.setStyleSheet("font-size: 18px; color: #4B0082; font-weight: bold;")
        self.label_sessions.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # List of existing sessions
        self.session_list = QListWidget(self)
        self.load_sessions()

        # Create New Session Button
        self.btn_new_session = QPushButton("Create New Session", self)
        self.btn_new_session.setFixedSize(240, 48)
        self.btn_new_session.setStyleSheet("background-color: black; color: white; font-size: 14px;")
        self.btn_new_session.clicked.connect(self.create_new_session)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_title)
        layout.addWidget(self.label_sessions)
        layout.addWidget(self.session_list)
        layout.addWidget(self.btn_new_session, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

    def load_sessions(self):
        """Load existing sessions from the database."""
        conn = engine()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT session_id FROM Sessions WHERE instructor_name = %s", (self.instructor_name,))
                sessions = cursor.fetchall()

                for session in sessions:
                    self.session_list.addItem(session[0])

                conn.close()
            except Exception as e:
                print(f"Database Error (Load Sessions): {e}")

    def create_new_session(self):
        """Create a new session and switch to the SessionWindow."""
        conn = engine()
        if conn:
            try:
                cursor = conn.cursor()

                # Generate a unique session ID
                session_id = str(uuid.uuid4())[:8]

                # Insert new session
                cursor.execute("""
                    INSERT INTO Sessions (session_id, instructor_name)
                    VALUES (%s, %s)
                """, (session_id, self.instructor_name))

                conn.commit()
                conn.close()

                # Add session to the list
                self.session_list.addItem(session_id)
                print(f"New Session Created: {session_id}")

                # Switch to SessionWindow
                self.session_window = SessionWindow(session_id, self.instructor_name)
                self.session_window.show()
                self.close()  # Close HomeWindow

            except Exception as e:
                print(f"Database Error (Create new Session): {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HomeWindow("Anonymous")
    window.show()
    sys.exit(app.exec())

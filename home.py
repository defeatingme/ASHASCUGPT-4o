import sys
import uuid
from PySide6.QtWidgets import QWidget, QPushButton, QTableWidgetItem, QAbstractItemView, QMessageBox
from PySide6.QtCore import Qt
from home_ui import Ui_Home
from database import Session, Sessions, AnswerKey, StudentHAS, database_func
from styles import buttonStyle, buttonStyle2, tableStyle, mboxStyle
from grading import SessionWindow  # Import SessionWindow

class HomeWindow(QWidget):
    def __init__(self, login_window, instructor_name):
        super().__init__()

        self.login_window = login_window
        self.instructor_name = instructor_name

        self.previous_value = ""  # Initialize previous_value to avoid AttributeError
        self.is_editing = False   # Flag to track if we're in editing mode

        self._ui = Ui_Home()
        self._ui.setupUi(self)

        # Window settings
        self.setWindowTitle("Home - Algeval")

        for button in self.findChildren(QPushButton):
            button.setStyleSheet(buttonStyle)
        self._ui.push_create.setStyleSheet(buttonStyle2)
        
        self._ui.table_sessions.setStyleSheet(tableStyle)
        self._ui.table_sessions.setAlternatingRowColors(True)
        self._ui.table_sessions.setSelectionMode(QAbstractItemView.ExtendedSelection)  # Enables Shift & Ctrl selection
        
        # Disconnect any existing connections to avoid multiple triggers
        try:
            self._ui.table_sessions.itemChanged.disconnect()
        except:
            pass
            
        # Set up table editing behavior
        self._ui.table_sessions.setEditTriggers(QAbstractItemView.DoubleClicked)
        self._ui.table_sessions.itemDoubleClicked.connect(self.prepare_for_editing)
        self._ui.table_sessions.itemChanged.connect(self.update_session_name)

        # List of existing sessions
        self.load_sessions()

        self._ui.push_create.clicked.connect(self.create_new)
        self._ui.push_continue.clicked.connect(self.continue_selected)
        self._ui.push_reload.clicked.connect(self.load_sessions)
        self._ui.push_delete.clicked.connect(self.delete_selected)
        self._ui.push_logout.clicked.connect(self.go_back)
        self._ui.push_exit.clicked.connect(self.go_exit)

    ################################################################################
    # INITIALIZE
    def load_sessions(self):
        # Temporarily disconnect itemChanged to prevent triggering during loading
        try:
            self._ui.table_sessions.itemChanged.disconnect()
        except:
            pass
            
        session = Session()
        try:
            # Query for sessions related to the instructor, sorted by latest created session
            sessions = session.query(Sessions).filter(Sessions.instructor_name == self.instructor_name) \
                                            .order_by(Sessions.created_at.desc()).all()

            # Set table row & column count
            self._ui.table_sessions.setRowCount(len(sessions))
            self._ui.table_sessions.setColumnCount(4)  # Four columns (Session ID, Session Name, Answer Keys, Checked solutions)
            self._ui.table_sessions.setHorizontalHeaderLabels(["Session ID", "Session Name", "No. of Answer Keys", "Checked Solutions"])  # Column headers

            for row, session_record in enumerate(sessions):
                # Count all answer keys associated with this session
                answer_key_count = session.query(database_func.count(AnswerKey.id)) \
                                        .filter(AnswerKey.session_id == session_record.session_id).scalar()

                # Count total number of HAS solutions linked to any answer key within the session
                total_has_count = session.query(database_func.count(StudentHAS.id)) \
                                        .join(AnswerKey, StudentHAS.answer_key_id == AnswerKey.id) \
                                        .filter(AnswerKey.session_id == session_record.session_id).scalar()

                # Create table items with proper flags
                session_id_item = QTableWidgetItem(session_record.session_id)
                session_id_item.setFlags(session_id_item.flags() & ~Qt.ItemIsEditable)  # Make session ID non-editable
                
                session_name_item = QTableWidgetItem(session_record.session_name if session_record.session_name else "N/A")
                session_name_item.setData(Qt.UserRole, session_record.session_id)  # Store session_id as user data
                
                answer_key_item = QTableWidgetItem(str(answer_key_count))
                answer_key_item.setFlags(answer_key_item.flags() & ~Qt.ItemIsEditable)  # Make count non-editable
                
                has_count_item = QTableWidgetItem(str(total_has_count))
                has_count_item.setFlags(has_count_item.flags() & ~Qt.ItemIsEditable)  # Make count non-editable

                # Populate table
                self._ui.table_sessions.setItem(row, 0, session_id_item)    # Session ID (non-editable)
                self._ui.table_sessions.setItem(row, 1, session_name_item)  # Session Name (editable)
                self._ui.table_sessions.setItem(row, 2, answer_key_item)    # No. of Answer Keys (non-editable)
                self._ui.table_sessions.setItem(row, 3, has_count_item)     # Total HAS Count (non-editable)

            # 💡 Auto-resize settings
            self._ui.table_sessions.horizontalHeader().setStretchLastSection(True)
            self._ui.table_sessions.resizeColumnsToContents()
            self._ui.table_sessions.resizeRowsToContents()
            total_width = self._ui.table_sessions.viewport().width()  # Get total table width

            # Set column widths
            self._ui.table_sessions.setColumnWidth(0, int(total_width * (1/7)))  # Session ID
            self._ui.table_sessions.setColumnWidth(1, int(total_width * (3/7)))  # Session Name
            self._ui.table_sessions.setColumnWidth(2, int(total_width * (1/7)))  # No. of Answer Keys
            self._ui.table_sessions.setColumnWidth(3, int(total_width * (1/7)))  # No. of Checked

            # 💡 Selection behavior
            self._ui.table_sessions.setSelectionBehavior(QAbstractItemView.SelectRows)

            self._ui.table_sessions.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
            self._ui.table_sessions.verticalScrollBar().setSingleStep(5)  # Default is 20

            # Fetch the latest session based on created_at
            last_session = session.query(Sessions).filter(Sessions.instructor_name == self.instructor_name) \
                            .order_by(Sessions.created_at.desc()).first()

            # Update label with the latest session details
            if last_session:
                self._ui.label_note.setText(f"*Latest Session: {last_session.session_id} ({last_session.session_name if last_session.session_name else 'N/A'}) | Created At: {last_session.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                self._ui.label_note.setText("No sessions available.")

        except Exception as e:
            print(f"Database Error (Load Sessions): {e}")
            self._ui.label_note.setText("Error fetching sessions.")

        finally:
            session.close()
            # Reconnect itemChanged after loading is complete
            self._ui.table_sessions.itemChanged.connect(self.update_session_name)

    def prepare_for_editing(self, item):
        """
        Called when an item is double-clicked.
        Store the previous value and allow editing only for session name column.
        """
        column = item.column()
        
        if column == 1:  # Session Name column
            self.is_editing = True
            self.previous_value = item.text()
            self._ui.table_sessions.editItem(item)
        else:
            # Prevent editing other columns
            self._ui.table_sessions.setEditTriggers(QAbstractItemView.NoEditTriggers)


    def update_session_name(self, item):
        """Update session_name in the database when a user edits it."""
        if not self.is_editing:
            return  # Skip if not in editing mode (prevents triggers during loading)

        column = item.column()
        
        if column != 1:  # Only process changes in the Session Name column
            return
            
        session = Session()
        try:
            # Get row index and session ID
            row = item.row()
            new_session_name = item.text().strip()[:31]
            
            # Retrieve the session_id from column 0
            session_id = self._ui.table_sessions.item(row, 0).text()
            
            if not new_session_name:
                QMessageBox.warning(self, "Invalid Input", "Session Name cannot be empty.")
                item.setText(self.previous_value)  # Revert back
                return

            # Find and update session by session_id
            session_record = session.query(Sessions).filter_by(session_id=session_id).first()

            if session_record:
                old_session_name = session_record.session_name if session_record.session_name else "N/A"  
                session_record.session_name = new_session_name
                session.commit()
                self._ui.label_note.setText(f"Session Name updated: {old_session_name} → {new_session_name}")
            else:
                QMessageBox.warning(self, "Not Found", "Session not found in database.")
                item.setText(self.previous_value)  # Revert back

        except Exception as e:
            session.rollback()
            QMessageBox.critical(self, "Database Error", f"Failed to update session name: {e}")
            item.setText(self.previous_value)  # Revert back

        finally:
            session.close()
            self.is_editing = False  # Reset editing flag



    def create_new(self):
        """Create a new session and switch to the SessionWindow."""
        session = Session()
        try:
            # Generate a unique session ID
            session_id = str(uuid.uuid4())[:8]

            # Create a new session object
            new_session = Sessions(session_id=session_id, instructor_name=self.instructor_name)

            # Add the new session to the session and commit
            session.add(new_session)
            session.commit()

            # Add the session ID to the first column of the new row
            row_count = self._ui.table_sessions.rowCount()
            self._ui.table_sessions.insertRow(row_count)
            self._ui.table_sessions.setItem(row_count, -1, QTableWidgetItem(session_id))
            self.load_sessions()
            print(f"New Session Created: {session_id}")

            # Switch to SessionWindow
            self.session_window = SessionWindow(self, session_id, self.instructor_name)
            self.session_window.show()
            self.close()  # Close HomeWindow

        except Exception as e:
            session.rollback()  # Rollback in case of error
            mboxStyle.critical(self, "Database Error", f"Failed to create session: {e}")
            print(e)

        finally:
            session.close()

    def continue_selected(self):
        """Warns the user if multiple sessions are selected and proceeds with only one."""
        selected_rows = self._ui.table_sessions.selectionModel().selectedRows()

        if not selected_rows:
            mboxStyle.warning(self, "No Selection", "Please select a session to continue.")
            return

        if len(selected_rows) > 1:
            mboxStyle.warning(self, "Multiple Selections", "Please select only one session to proceed.")
            return

        # Fetch the selected session ID
        selected_row = selected_rows[0].row()
        session_id = self._ui.table_sessions.item(selected_row, 0).text()

        # Proceed with the session
        self.session_window = SessionWindow(self, session_id, self.instructor_name)
        self.session_window.show()
        self.close()  # Close HomeWindow


    def delete_selected(self):
        """Deletes multiple selected sessions from the database and removes them from the table."""
        selected_rows = sorted(set(index.row() for index in self._ui.table_sessions.selectionModel().selectedRows()), reverse=True)

        if not selected_rows:
            mboxStyle.warning(self, "No Selection", "Please select at least one session to delete.")
            return

        # Collect session IDs to delete
        session_ids = [self._ui.table_sessions.item(row, 0).text() for row in selected_rows]

        # Confirm deletion
        confirmation = mboxStyle.question(
            self,
            "Confirm Deletion",
            f"Are you sure you want to delete {len(session_ids)} selected sessions?"
        )

        if confirmation == QMessageBox.No:
            return  # Cancel deletion

        # Delete sessions from the database
        session = Session()
        try:
            deleted_sessions = 0
            deleted_session_id = None  # Store the ID of the deleted session


            for session_id in session_ids:
                session_record = session.query(Sessions).filter_by(session_id=session_id).first()
                if session_record:
                    session.delete(session_record)
                    deleted_sessions += 1
                    if deleted_sessions == 1:  # Capture ID if only one session is deleted
                        deleted_session_id = session_id
            
            session.commit()

            # Remove rows from table (from bottom to top to avoid index shift issues)
            for row in selected_rows:
                self._ui.table_sessions.removeRow(row)

            if deleted_sessions == 1:
                self._ui.label_note.setText(f"Session {deleted_session_id} has been deleted.")
            else:
                self._ui.label_note.setText(f"{deleted_sessions} sessions have been deleted.")

        except Exception as e:
            session.rollback()
            mboxStyle.critical(self, "Database Error", f"Failed to delete sessions: {e}")
            print(f"Error deleting sessions: {e}")

        finally:
            session.close()

    ################################################################################
    # Save and Close window

    def go_back(self):
        self.close()
        self.login_window.show()


    def go_exit(self):
        self.close()

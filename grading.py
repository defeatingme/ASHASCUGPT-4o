import sys
from PIL import Image
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QFileDialog, QMessageBox, QTableWidgetItem, QAbstractItemView
)
from PySide6.QtCore import Qt, Signal, QThread, QObject
from PySide6.QtGui import QPixmap, QIntValidator, QImage
from grading_ui_2 import Ui_Session
from styles import buttonStyle, buttonStyle2, mboxStyle, tableStyle

from database import Session, AnswerKey, StudentHAS
from ak_camera import AK_Camera
from ocr import GeminiOCR
from render_latex import MathJaxSOL, ClearHTML, LoadHTML
from export import export_data

class OCRWorker(QObject):
    """Worker thread for running OCR on images."""
    ocr_completed = Signal(str)  # Signal to send the extracted LaTeX string
    ocr_failed = Signal(str)     # Signal to handle errors

    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def run(self):
        """Runs the OCR process in a separate thread."""
        try:
            print("OCR Processing Started.")

            ak_latex = GeminiOCR(self.file_path)  # Call OCR function
            if "The image does not contain any mathematical expression" not in ak_latex:
                self.ocr_completed.emit(ak_latex)  # Emit success signal
            else:
                self.ocr_failed.emit("The image does not contain any mathematical expression. Please try again.")
        except Exception as e:
            self.ocr_failed.emit(str(e))  # Emit error signal


class SessionWindow(QWidget):
    ak_changed = Signal()

    def __init__(self, home_window, session_id, instructor_name):
        super().__init__()

        self.home_window = home_window
        self.session_id = session_id
        self.instructor_name = instructor_name
        self.ak_latex = ""
        self.saved_ak_latex = None
        self.file_path = None
        self.answer_key_id = None
        self.ak_file = None

        self._ui = Ui_Session()
        self._ui.setupUi(self)

        self.setWindowTitle(f"Session {session_id} - Algeval")
        self._ui.label_session.setText(f"Session: {session_id}")
        self._ui.label_instructor.setText(f"by: {instructor_name}")

        for button in self.findChildren(QPushButton):
            button.setStyleSheet(buttonStyle)
        self._ui.push_save.setStyleSheet(buttonStyle2)
        self._ui.push_start.setStyleSheet(buttonStyle2)

        self._ui.table_checked.setStyleSheet(tableStyle)
        self._ui.table_checked.setAlternatingRowColors(True)
        self._ui.table_checked.setSelectionMode(QAbstractItemView.MultiSelection)
        self._ui.table_checked.setSelectionMode(QAbstractItemView.ExtendedSelection) 

        self.clearhtml = ClearHTML()
        self.loadhtml = LoadHTML()
        self._ui.web_latex.setHtml(self.clearhtml)

        self.ak_window = AK_Camera(self)  # Store instance persistently
        if self.ak_window.cameraStarted == True:
            self.ak_window.stopCamera()

        self.ak_window.imageProcessed.connect(self.camera_file)  # Connect signal

        validator = QIntValidator(1, 100)  # Min: 1, Max: 100
        self.ak_changed.connect(self.verifyToEnable)

        # Apply validator to the input field
        self._ui.edit_fa_weight.setValidator(validator)

        self._ui.push_camera.clicked.connect(self.open_camera)
        self._ui.push_computer.clicked.connect(self.upload_from_computer)
        self._ui.push_save.clicked.connect(self.save_answer_key)
        self._ui.push_start.clicked.connect(self.start_has_checking)
        self._ui.push_back.clicked.connect(self.go_back)
        self._ui.push_redo.clicked.connect(self.OCRProcessing)
        self._ui.push_reload.clicked.connect(self.load_checked)
        self._ui.push_delete.clicked.connect(self.delete_selected)
        self._ui.push_export.clicked.connect(lambda: export_data(self._ui.table_checked))

        
        self._ui.push_redo.setEnabled(False)
        self._ui.push_save.setEnabled(False)
        self._ui.push_start.setEnabled(False)

        self.fetch_data()
        self.load_checked()

    def fetch_data(self):
        """Fetch the first AnswerKey related to this session and update attributes."""
        session = Session()
        try:
            answer_key = session.query(AnswerKey).filter_by(session_id=self.session_id).first()
            
            if answer_key:
                self.answer_key_id = answer_key.id
                self.saved_ak_latex = answer_key.ak_latex
                self.fa_weight = answer_key.fa_weight
                self.ak_file = answer_key.ak_file  # Binary image data
                
                # Display retrieved status
                self.display_status()
            else:
                self._ui.label_save_note.setText(f"*No. of AKs saved: 0/2")

        except Exception as e:
            print(f"Database error: {e}")
        finally:
            session.close()
    
    def display_status(self):
        pixmap = None
        if self.answer_key_id:
            self._ui.label_save_note.setText(f"*Data is saved. Answer key ID: {self.answer_key_id}")
            self.ak_latex = self.saved_ak_latex
            self.display_latex()
            self._ui.edit_fa_weight.setText(f"{int(self.fa_weight)}")

            # Display the image if available
            if self.ak_file:
                file = QImage.fromData(self.ak_file)
                if file.isNull():
                    mboxStyle.warning(self, "Error", "Invalid file data. Cannot display.")
                    return
                pixmap = QPixmap.fromImage(file)
                self._ui.label_image.setPixmap(pixmap.scaled(360, 270, Qt.AspectRatioMode.KeepAspectRatio))

            self.verifyToEnable()

    def load_checked(self):
        session = Session()
        try:
            # Query all student HAS linked to the given answer key ID
            student_records = session.query(
                StudentHAS.id,  
                StudentHAS.has_name,
                StudentHAS.sol_fraction,
                StudentHAS.sol_grade,
                StudentHAS.fa_grade,
                StudentHAS.overall_grade
            ).filter(StudentHAS.answer_key_id == self.answer_key_id).all()

            # Set table row & column count
            self._ui.table_checked.setRowCount(len(student_records))
            self._ui.table_checked.setColumnCount(5)  # Four columns
            self._ui.table_checked.setHorizontalHeaderLabels(["ID", "Name", "Solution", "Final Ans.", "Overall"])

            # Populate the table
            for row, record in enumerate(student_records):
                # Merge sol_fraction and sol_grade into one column
                sol_combined = f"{record.sol_fraction} = {record.sol_grade}"


                id_item = QTableWidgetItem(str(record.id))
                id_item.setFlags(Qt.ItemIsEnabled)  # Make it read-
                self._ui.table_checked.setItem(row, 0, id_item)

                self._ui.table_checked.setItem(row, 1, QTableWidgetItem(record.has_name))  # Student Name
                sol_item = QTableWidgetItem(sol_combined)
                fa_item = QTableWidgetItem(str(record.fa_grade))
                overall_item = QTableWidgetItem(str(record.overall_grade))

                # Right-align the numerical values
                sol_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                fa_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                overall_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

                self._ui.table_checked.setItem(row, 2, sol_item)  # Solution Grade
                self._ui.table_checked.setItem(row, 3, fa_item)  # FA Grade
                self._ui.table_checked.setItem(row, 4, overall_item)  # Overall Grade

            # 💡 Auto-resize settings
            self._ui.table_checked.horizontalHeader().setStretchLastSection(True)
            self._ui.table_checked.resizeColumnsToContents()
            self._ui.table_checked.resizeRowsToContents()
            total_width = self._ui.table_checked.viewport().width()  # Get total table width

            # Adjust column widths
            self._ui.table_checked.setColumnHidden(0, True)
            self._ui.table_checked.setColumnWidth(1, int(total_width * 0.30))  # Student Name
            self._ui.table_checked.setColumnWidth(2, int(total_width * 0.225))  # Solution Grade
            self._ui.table_checked.setColumnWidth(3, int(total_width * 0.225))  # FA Grade
            self._ui.table_checked.setColumnWidth(4, int(total_width * 0.225))  # Overall Grade

            # 💡 Smooth scrolling for better UX
            self._ui.table_checked.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
            self._ui.table_checked.verticalScrollBar().setSingleStep(5)

            # 💡 Prevent editing & enable row selection
            self._ui.table_checked.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self._ui.table_checked.setSelectionBehavior(QAbstractItemView.SelectRows)

            row_count = self._ui.table_checked.rowCount()
            self._ui.label_table_note.setText(f"{row_count} recorded solution(s).")

        except Exception as e:
            mboxStyle.critical(self, "Database Error: ", str(e))
            print(e)
        finally:
            session.close()


    def delete_selected(self):
        """Deletes multiple selected checked solutions from the database and removes them from the table."""
        selected_rows = sorted(set(index.row() for index in self._ui.table_checked.selectionModel().selectedRows()), reverse=True)

        if not selected_rows:
            mboxStyle.warning(self, "No Selection", "Please select at least one checked solution to delete.")
            return

        # Collect checked solution IDs to delete
        has_ids = [int(self._ui.table_checked.item(row, 0).text()) for row in selected_rows]

        # Confirm deletion
        confirmation = mboxStyle.question(
            self,
            "Confirm Deletion",
            f"Are you sure you want to delete {len(has_ids)} selected checked solutions?"
        )

        if confirmation == QMessageBox.No:
            return  # Cancel deletion

        # Delete checked solutions from the database
        session = Session()
        try:
            deleted_has = 0
            deleted_has_name = None

            for has_id in has_ids:
                has_record = session.query(StudentHAS).filter_by(id=has_id).first()
                if has_record:
                    session.delete(has_record)
                    deleted_has += 1
                    
                    if deleted_has == 1:  # Capture ID if only one session is deleted
                        deleted_has_name = has_record.has_name  # Store the name of the deleted record
            
            session.commit()

            # Remove rows from table (from bottom to top to avoid index shift issues)
            for row in selected_rows:
                self._ui.table_checked.removeRow(row)

            if deleted_has == 1:
                self._ui.label_table_note.setText(f"Solution by {deleted_has_name}\nhas been deleted.")
            else:
                self._ui.label_table_note.setText(f"{deleted_has} checked solutions\nhave been deleted.")

        except Exception as e:
            session.rollback()
            mboxStyle.critical(self, "Database Error", f"Failed to delete checked solutions: {e}")
            print(f"Error deleting checked solutions: {e}")

        finally:
            session.close()


    def open_camera(self):
        self.ak_window.startCamera()
        self.ak_window.show()
        self.hide()  # Hide main window


    def camera_file(self, file_path, ak_latex):
        self.show()  # Show main window again

        self._ui.push_redo.setEnabled(False)
        self._ui.push_save.setEnabled(False)
        self._ui.push_start.setEnabled(False)

        self.file_path = file_path
        self.display_image(self.file_path)
        if self.saved_ak_latex not in (None, ak_latex):
            self.ak_changed.emit()
        self.ak_latex = ak_latex
        self.display_latex()
        

    def upload_from_computer(self):
        """Opens file explorer to upload an image."""
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Select Answer Key Image", "", "Images (*.png *.jpg *.jpeg)")
        if self.file_path:
            self.display_image(self.file_path)
            self.OCRProcessing()

    
    def OCRProcessing(self):
        """Starts the OCR process in a separate thread."""
        self._ui.push_redo.setEnabled(False)
        self._ui.push_save.setEnabled(False)
        self._ui.push_start.setEnabled(False)

        self._ui.web_latex.setHtml(self.loadhtml)

        self.ocr_thread = QThread()  # Create a new thread
        self.ocr_worker = OCRWorker(self.file_path)  # Create the worker

        # Move worker to the thread
        self.ocr_worker.moveToThread(self.ocr_thread)

        # Connect signals
        self.ocr_thread.started.connect(self.ocr_worker.run)
        self.ocr_worker.ocr_completed.connect(self.handleOCRSuccess)
        self.ocr_worker.ocr_failed.connect(self.handleOCRError)

        # Ensure cleanup after the thread finishes
        self.ocr_worker.ocr_completed.connect(self.ocr_thread.quit)
        self.ocr_worker.ocr_failed.connect(self.ocr_thread.quit)
        self.ocr_worker.ocr_completed.connect(self.ocr_worker.deleteLater)
        self.ocr_worker.ocr_failed.connect(self.ocr_worker.deleteLater)
        self.ocr_thread.finished.connect(self.ocr_thread.deleteLater)

        self.ocr_thread.start()  # Start the thread


    def handleOCRSuccess(self, ak_latex):
        """Handles successful OCR extraction."""
        if self.saved_ak_latex not in (None, ak_latex):
            self.ak_changed.emit()
        self.ak_latex = ak_latex
        print(self.ak_latex)
        self.display_latex()


    def handleOCRError(self, error_message):
        """Handles OCR failure."""
        mboxStyle.warning(self, "OCR Error", error_message)
        
        self._ui.push_redo.setEnabled(True)

        if self.saved_ak_latex:
            self.display_status()
        else:
            self._ui.web_latex.setHtml(self.clearhtml)
            
        self.verifyToEnable()


    def display_image(self, file):
        """Displays the selected image in QLabel."""
        pixmap = QPixmap(file)
        self._ui.label_image.setPixmap(pixmap.scaled(360, 270, Qt.AspectRatioMode.KeepAspectRatio))


    def display_latex(self):
        html_content = MathJaxSOL(self.ak_latex)
        self._ui.web_latex.setHtml(html_content)

        self._ui.push_redo.setEnabled(True)
        self._ui.push_save.setEnabled(True)
        self.verifyToEnable()

        
    def save_answer_key(self):
        """Saves the answer key to the database using SQLAlchemy ORM."""
        # Retrieve form inputs
        fa_weight = self._ui.edit_fa_weight.text().strip() or 20
        fa_weight = float(fa_weight)
        if fa_weight > 100:
            mboxStyle.warning(self, "Error", "Final answer weight should not exceed 100%")
            return
        
        if self.ak_latex == ("" or "The file does not contain any mathematical expression."):
            mboxStyle.warning(self, "Error", "No LaTeX code detected. Please upload an answer key file first.")
            return

        self.fa_weight = fa_weight
        sol_weight = 100 - self.fa_weight
        

        # Validate the file path before reading the file
        if self.file_path == None:
            if self.ak_file == None:
                mboxStyle.warning(self, "Error", "No file selected. Please upload an answer key file.");
                return
            else:
                pass
        else:
            # Read file
            try:
                with open(self.file_path, "rb") as file:
                    self.ak_file = file.read()
            except FileNotFoundError:
                mboxStyle.critical(self, "Error", "File not found. Please check the file path.")
                return

        #Connect to Database
        session = Session()
        try:
            if self.answer_key_id:
                # Fetch the existing AnswerKey using the new SQLAlchemy 2.0 syntax
                answer_key = session.get(AnswerKey, self.answer_key_id)
                if answer_key:
                    # Update existing record
                    answer_key.sol_weight = sol_weight
                    answer_key.fa_weight = self.fa_weight
                    answer_key.ak_latex = self.ak_latex
                    answer_key.ak_file = self.ak_file  # Store file as BYTEA

                    session.commit()

                    self._ui.label_save_note.setText(f"*Data is updated. Answer key ID: {self.answer_key_id}")
                else:
                    mboxStyle.warning(self, "Error", "Answer key not found in the database.")
                    return
            else:
                # Create a new AnswerKey object if no ID exists
                answer_key = AnswerKey(
                    session_id=self.session_id,
                    sol_weight=sol_weight,
                    fa_weight=self.fa_weight,
                    ak_latex=self.ak_latex,
                    ak_file = self.ak_file  # Store file as BYTEA

                )
                session.add(answer_key)
                session.commit()
                self.answer_key_id = answer_key.id  # Store the new ID
                self._ui.label_save_note.setText(f"*Data is saved. Answer key ID: {self.answer_key_id}")

            self.saved_ak_latex = self.ak_latex
            self.verifyToEnable()
            self._ui.push_save.setEnabled(False)


            # Enable save button if values change
            self._ui.edit_fa_weight.textChanged.connect(self.verifyToEnable)

        except Exception as e:
            session.rollback()
            mboxStyle.critical(self, "Database Error", f"Failed to save answer key: {e}")
            print(e)
        finally:
            session.close()

    def verifyToEnable(self):
        if self.answer_key_id:
            if self._ui.edit_fa_weight.text().strip() or self.ak_latex:
                self._ui.push_save.setEnabled(True)
            else:
                self._ui.push_save.setEnabled(False)
            
            self._ui.push_start.setEnabled(True)
        else:
            if self.ak_latex:
                self._ui.push_save.setEnabled(True)
                self._ui.push_start.setEnabled(False)



    def start_has_checking(self):
        if self.ak_window is not None:
            self.ak_window.close()

        from has_camera import HAS_Camera
        self.has_camera = HAS_Camera(self, self.answer_key_id, self.fa_weight, self.saved_ak_latex)
        self.has_camera.show()
        self.close()

    def go_back(self):
        if self.ak_window is not None:
            self.ak_window.close()
        self.close()
        self.home_window.show()

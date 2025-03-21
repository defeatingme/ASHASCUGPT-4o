from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QApplication, QMessageBox, QPushButton, QWidget, QVBoxLayout

buttonStyle = """QPushButton {
    background-color: rgb(32, 32, 32);
    color: rgb(208, 172, 220);
    border: 1px solid rgb(208, 172, 220);
    border-radius: 4px
    }
    QPushButton:disabled {
    background-color: rgb(48, 48, 48);
    color:  rgb(128, 128, 128);
    border: 1px solid rgb(128, 128, 128);
    border-radius: 4px
    }
    QPushButton:hover {
    color:  rgb(175, 192, 220);
    border: 1px solid rgb(175, 192, 220);
    }
    QPushButton:pressed {
    background-color:  rgb(208, 172, 220);
    color: rgb(224, 224, 224);
    border: 1px solid rgb(224, 224, 224);
    font-weight: bold;
    }
    """

tableStyle = """
    QHeaderView::section {
        background-color: rgb(48, 48, 48); /* Dark gray background */
        color:  rgb(175, 192, 220); /* Light gray font */
        padding: 4px;
        font-size: 12px;
        font-family: Arial;
        border: 1px solid  rgb(175, 192, 220); /* Ensure border applies */
    }

    QTableCornerButton::section {
        background-color: rgb(48, 48, 48);
        border: 1px solid  rgb(175, 192, 220); 
    }

    QTableWidget::item {
        color: rgb(224, 224, 224);
    }

    QTableWidget::item:selected {
        background-color: rgb(208, 172, 220); /* Soft purple selection */
        color: rgb(32, 32, 32);
        border: 1px solid rgb(224, 224, 224);
    }

    QTableWidget {
        gridline-color: rgb(32, 32, 32); /* Change gridline color */
        background-color: rgb(56, 56, 56); 
        alternate-background-color: rgb(64, 64, 64);
        font-size: 12px;
        font-family: Arial;
        color: rgb(224, 224, 224);
        border: 1px solid  rgb(32, 32, 32);
    }
    """

class mboxStyle(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QMessageBox {
                background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255));
                color: rgb(224, 224, 224);
                font-size: 12px;
                border-radius: 8px;
            }
            QMessageBox QLabel {
                background-color: transparent;       
                color: rgb(224, 224, 224);
            }
            QMessageBox QPushButton {
                background-color: rgb(32, 32, 32);
                color: rgb(208, 172, 220);
                border: 1px solid rgb(208, 172, 220);
                border-radius: 4px;
                min-width: 81px;  /* Adjust button width */
                min-height: 21px;  /* Adjust button height */
            }
            QMessageBox QPushButton:disabled {
                background-color: rgb(64, 64, 64);
                color: rgb(128, 128, 128);
                border: 1px solid rgb(128, 128, 128);
            }
            QMessageBox QPushButton:hover {
                color: rgb(175, 192, 220);
                border: 1px solid rgb(175, 192, 220);
            }
            QMessageBox QPushButton:pressed {
                background-color: rgb(208, 172, 220);
                color: rgb(224, 224, 224);
                border: 1px solid rgb(224, 224, 224);
                font-weight: bold;
            }
        """)

    @staticmethod
    def warning(parent, title, text):
        msg = mboxStyle(parent)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    @staticmethod
    def critical(parent, title, text):
        msg = mboxStyle(parent)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    @staticmethod
    def information(parent, title, text):
        msg = mboxStyle(parent)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    @staticmethod
    def question(parent, title, text):
        msg = mboxStyle(parent)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)  # Set "No" as the default
        return msg.exec() 
from PySide6.QtWidgets import QStyledItemDelegate, QLineEdit
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression

class LimitedTextDelegate(QStyledItemDelegate):
    """Enforces a 15-character limit while typing in QTableWidget cells."""
    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setValidator(QRegularExpressionValidator(QRegularExpression(".{0,15}"), parent))  # Limit to 15 chars
        editor.setStyleSheet("color: white;")  # Keep text white
        return editor

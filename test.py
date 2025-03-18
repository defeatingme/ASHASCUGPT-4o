from PySide6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys

class ImageTable(QWidget):
    def __init__(self):
        super().__init__()

        # Create TableWidget
        self.table = QTableWidget(1, 2)  # 1 row, 2 columns
        self.table.setHorizontalHeaderLabels(["Name", "Image"])
        self.table.setColumnWidth(1, 150)  # Adjust column width for image
        self.table.setRowHeight(0, 150)  # Adjust column width for image

        # Add data
        self.add_row("Student 1", r"GPTDataset\example_2.jpg")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

    def add_row(self, name, image_path):
        """Adds a row with text and an image"""
        # Set text in the first column
        self.table.setItem(0, 0, QTableWidgetItem(name))

        # Load image and create QLabel
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio)  # Resize

        label = QLabel()
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)

        self.table.setCellWidget(0, 1, label)  


if __name__ == "__main__":
    app = QApplication(sys.argv)
    start_window = ImageTable()
    start_window.show()
    sys.exit(app.exec())
       

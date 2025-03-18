import sys
import cv2
import numpy as np
import pytesseract
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from sizes_ui import Ui_Size
from styles import buttonStyle

class Characters(QWidget):
    def __init__(self, characters, image, page=0, show_boxes=True):
        super().__init__()
        self.characters = characters
        self.image = image
        self.page = page
        self.show_boxes = show_boxes
        self.chars_per_page = 12
        #self.initUI()

        self._ui = Ui_Size()
        self._ui.setupUi(self)
        
        for button in self.findChildren(QPushButton):
            button.setStyleSheet(buttonStyle)
        
        self.figure = plt.figure(figsize=(6, 4))  # Ensure a reasonable figure size
        self.ax = self.figure.add_subplot(111)

        layout = QVBoxLayout()
        self.figure, self.ax = plt.subplots(figsize=(6, 4))  # Smaller initial figure size
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        
        self._ui.push_prev.clicked.connect(self.prev_page)
        self._ui.push_next.clicked.connect(self.next_page)
        self._ui.push_back.clicked.connect(self.go_back)

        self._ui.widget.setLayout(layout)
        self.update_display()

    def update_display(self):
        plt.close(self.figure)  # Close previous figure to free memory
        self.ax.clear()

        if self.show_boxes:
            img_rgb = cv2.cvtColor(self.image, cv2.COLOR_GRAY2RGB)
            for _, _, x, y, w, h in self.characters:
                cv2.rectangle(img_rgb, (x, y), (x + w, y + h), (0, 255, 0), 2)

            self.ax.imshow(img_rgb, cmap='gray')
            self.ax.set_title("Detected Characters with Bounding Boxes", fontsize=14)
        else:
            start = self.page * self.chars_per_page
            end = min(start + self.chars_per_page, len(self.characters))
            chars_on_page = self.characters[start:end]

            num_chars = len(chars_on_page)
            cols = 4  # Adjust for 4 or 5 characters per row
            rows = (num_chars // cols) + (num_chars % cols > 0)

            # Adjust figure size dynamically
            self.figure.set_size_inches(cols * 2.2, rows * 2.2)

            # Create subplots with tighter layout
            fig, axes = plt.subplots(rows, cols, figsize=(cols * 2, rows * 2),
                                    constrained_layout=True)

            axes = np.array(axes).reshape(-1)

            for i, (_, char_img, x, y, w, h) in enumerate(chars_on_page):
                ax = axes[i]
                char_resized = cv2.resize(char_img, (140, 140), interpolation=cv2.INTER_NEAREST)
                char_resized = cv2.flip(char_resized, 0)
                ax.imshow(char_resized, cmap="gray", extent=[0, w, h, 0])
                ax.invert_yaxis()
                ax.set_title(f"Character {start + i + 1}", fontsize=10, fontweight="bold", pad=5)

            # Hide unused subplots
            for j in range(i + 1, len(axes)):
                axes[j].axis("off")

            # Reduce excess padding

            self.figure.clear()
            self.figure = fig
            self.canvas.figure = self.figure

        self.canvas.draw()



    def next_page(self):
        if self.show_boxes:
            self.show_boxes = False
            self.page = 0
        elif (self.page + 1) * self.chars_per_page < len(self.characters):
            self.page += 1

        self.update_display()
        

    def prev_page(self):
        if not self.show_boxes and self.page == 0:
            self.show_boxes = True
        elif self.page > 0:
            self.page -= 1
        
        self.update_display()

    def go_back(self):
        self.close()
        


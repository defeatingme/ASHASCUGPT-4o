from __future__ import annotations

"""PySide6 port of the QtMultiMedia camera example from Qt v6.x"""

import sys

from PySide6.QtWidgets import QApplication

from camera import Camera


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())
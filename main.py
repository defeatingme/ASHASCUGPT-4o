from __future__ import annotations

"""PySide6 port of the QtMultiMedia camera example from Qt v6.x"""

import sys

from PySide6.QtWidgets import QApplication
from database import setup_tables
from login import Login


if __name__ == "__main__":
    app = QApplication(sys.argv)
    setup_tables()
    start_window = Login()
    start_window.show()
    sys.exit(app.exec())
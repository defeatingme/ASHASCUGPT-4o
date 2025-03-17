from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
import sys
import io
from ak_dialog_ui import Ui_Dialog
from styles import mboxStyle

from database import Session, AnswerKey
from render_latex import MathJaxSOL

class AK_Dialog(QDialog):
    def __init__(self, answer_key_id, fa_weight, ak_latex):
        super().__init__()

        self.answer_key_id = answer_key_id
        self.fa_weight = fa_weight
        self.ak_latex = ak_latex
        self.sol_weight = 100 - self.fa_weight

        self._ui = Ui_Dialog()
        self._ui.setupUi(self)
    
        self.display_file()
        html_content = MathJaxSOL(self.ak_latex)
        self._ui.web_latex.setHtml(html_content)

        self._ui.label_sol_grade.setText(f"Step-by-step solution (SOL): {self.sol_weight}%")
        self._ui.label_fa_grade.setText(f"Final answer (FA): {self.fa_weight}%")
        
        self._ui.push_back.clicked.connect(self.accept)


    def display_file(self):
        """Retrieves and displays the saved answer key file in a QLabel."""

        if not self.answer_key_id:
            mboxStyle.warning(self, "Error", "No Answer Key ID available. Please save an answer key first.")
            return

        session = Session()
        try:
            answer_key = session.get(AnswerKey, self.answer_key_id)
            if answer_key and answer_key.ak_file:
                # Convert BYTEA to QPixmap
                read_file = answer_key.ak_file
                file = QImage.fromData(read_file)

                if file.isNull():
                    mboxStyle.warning(self, "Error", "Invalid file data. Cannot display.")
                    return

                pixmap = QPixmap.fromImage(file)

                # Set the file in QLabel
                self._ui.label_file.setPixmap(pixmap.scaled(460, 460, Qt.AspectRatioMode.KeepAspectRatio))

            else:
                pass
            
        except Exception as e:
            mboxStyle.critical(self, "Database Error", f"Failed to retrieve file: {e}")
            print(e)
        finally:
            session.close()

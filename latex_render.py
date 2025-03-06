import sys
import re
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView

class MathJaxApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create QWebEngineView widget
        self.browser = QWebEngineView()

        # GPT-4o's raw LaTeX response (without delimiters)
        latex_raw = r"""
        x^2 - 5x + 6 = 0
        \[
        x = \frac{-(-5) \pm \sqrt{(-5)^2 - 4(1)(6)}}{2(1)}
        \]
        \[
        x = \frac{5 \pm \sqrt{25 - 24}}{2}
        \]
        \[
        x = \frac{5 \pm 1}{2}
        \]
        \[
        x = \frac{6}{2} \quad \text{or} \quad x = \frac{4}{2}
        \]

        Answer: x = 3 \quad \text{or} \quad x = 2            
        """

        # Apply regex to wrap LaTeX properly
        formatted_latex = self.format_latex(latex_raw)

        # Define HTML content with MathJax
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

        </head>
        <body>
            <h2>Rendered LaTeX Equation:</h2>
            <p>
                {formatted_latex}
            </p>
        </body>
        </html>
        """

        # Load HTML into the QWebEngineView
        self.browser.setHtml(html_content)
        self.setCentralWidget(self.browser)

        # Set window properties
        self.setWindowTitle("MathJax with PySide6")
        self.resize(800, 600)

    def format_latex(self, text):
        """
        Detects standalone LaTeX expressions and wraps them in MathJax delimiters.
        This ensures MathJax can correctly render equations.
        """
        # Ensure block-level equations are properly wrapped
        #text = re.sub(r"(?<!\$)\[", r"$$", text)  # Replace `[` with `$$`
        #text = re.sub(r"\](?!\$)", r"$$", text)   # Replace `]` with `$$`

        # Ensure inline equations are properly wrapped
        #text = re.sub(r"(?<!\$)(\\[a-zA-Z]+[^{ ]*\{[^}]+\})(?!\$)", r"$\1$", text)
        # Step 1: Convert block-level LaTeX (`\[ ... \]`) to MathJax format (`$$ ... $$`)
        text = re.sub(r"\\\[", r"$$", text)  # Replace `\[`
        text = re.sub(r"\\\]", r"$$", text)  # Replace `\]`
        
        # Step 2: Ensure inline LaTeX expressions (like \frac, \sqrt) are wrapped in `$...$`
        text = re.sub(r"(?<!\$)(\\[a-zA-Z]+(?:\{[^}]*\})*)", r"$\1$", text)

        return text

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MathJaxApp()
    window.show()
    sys.exit(app.exec())

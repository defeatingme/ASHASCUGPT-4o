import sys
import re
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from ocr import GeminiOCR

class MathJaxApp(QMainWindow):
    def __init__(self, latex_raw):
        super().__init__()

        # Create QWebEngineView widget
        self.browser = QWebEngineView()

        # GPT-4o's raw LaTeX response (without delimiters)

        # Apply regex to wrap LaTeX properly
        formatted_latex = self.format_latex(latex_raw)

        # Define HTML content with MathJax
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <script id="MathJax-script" async 
                src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
            <style>
                body {{
                    background-color: #333; /* Dark background */
                    color: #eee; /* Light gray text */
                    font-size: 14px; /* Adjusted for better visibility in 320x300 px */
                    padding: 5px;
                    font-family: Arial, sans-serif;
                    overflow: auto; /* Enable scrolling if needed */
                }}
                .math-container {{
                    text-align: left;
                    white-space: pre-wrap; /* Preserve new lines */
                    font-size: 12px; /* Ensuring 7-8 layers fit */
                    line-height: 0.5; /* Reduce line spacing */

                }}
            </style>
        </head>
        <body>
            <div class="math-container">
                {latex_raw}
            </div>
        </body>
        </html>
        """
        # Load HTML into the QWebEngineView
        self.browser.setHtml(html_content)
        self.setCentralWidget(self.browser)

        # Set window properties
        self.setWindowTitle("MathJax with PySide6")
        self.resize(320, 300)

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
    image = r"images\has\has1.png"
    #latex_raw = GeminiOCR(image)
    latex_raw = r'''$$ \frac{1}{2}(x-4)+\frac{1}{3}(x+6)=5 $$
$$ 6 \times [\frac{1}{2}(x-4)+\frac{1}{3}(x+6)] = 6 \times (5) $$
$$ 3(x-4)+2(x+6) = 30 $$
$$ 3x-12+2x+12=30 $$
$$ \frac{5x}{5} = \frac{30}{5} $$
$$ x=6 $$'''
    print(latex_raw)
    window = MathJaxApp(latex_raw)
    window.show()
    sys.exit(app.exec())

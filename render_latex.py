import sys
import re
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from ocr import GeminiOCR

# Define HTML content with MathJax
def MathJaxSOL(latex_raw):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script id="MathJax-script" async 
            src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
        <style>
            body {{
                background-color: rgb(64, 64, 64); /* Dark background */
                color: rgb(224, 224, 224); /* Light gray text */
                font-size: 14px; /* Adjusted for better visibility in 320x300 px */
                padding: 5px;
                font-family: Arial, sans-serif;
                overflow: auto; /* Enable scrolling if needed */
                border: 1px solid rgb(208, 172, 220);
            }}
            .math-container {{
                text-align: left;
                white-space: pre-wrap; /* Preserve new lines */
                font-size: 14px; /* Ensuring 7-8 layers fit */
                line-height: .1; /* Reduce line spacing */

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
    return html_content

def MathJaxRes(latex_raw):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script id="MathJax-script" async 
            src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
        <style>
            body {{
                background-color: rgb(64, 64, 64); /* Dark background */
                color: rgb(224, 224, 224); /* Light gray text */
                font-size: 14px; /* Adjusted for better visibility in 320x300 px */
                padding: 2px;
                font-family: Arial, sans-serif;
                overflow: auto; /* Enable scrolling if needed */
                border: 1px solid rgb(208, 172, 220)
            }}
            .math-container {{
                text-align: left;
                white-space: pre-wrap; /* Preserve new lines */
                font-size: 14px; /* Ensuring 7-8 layers fit */
                line-height: 1.5; /* Reduce line spacing */

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
    return html_content


def ClearHTML():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                background-color: rgb(64, 64, 64);
                margin: 0; /* Ensures no unwanted spacing */
                height: 100vh; /* Makes sure the background covers the whole viewport */
            }
        </style>
    </head>
    <body>
    </body>
    </html>
    """
    return html_content

def LoadHTML():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                background-color: rgb(64, 64, 64); /* Dark background */
                color: rgb(224, 224, 224); /* Light gray text */
                font-size: 14px; /* Adjusted for better visibility in 320x300 px */
                padding: 2px;
                font-family: Arial, sans-serif;
                overflow: auto; /* Enable scrolling if needed */
                border: 1px solid rgb(208, 172, 220)
            }
            .math-container {
                text-align: left;
                white-space: pre-wrap; /* Preserve new lines */
                font-size: 14px; /* Ensuring 7-8 layers fit */
                line-height: 1.5; /* Reduce line spacing */
            }
        </style>
    </head>
    <body>
        <div class="math-container">
            Loading...
        </div>
    </body>
    </html>
    """
    return html_content



class MathJaxApp(QMainWindow):
    def __init__(self, latex_raw):
        super().__init__()

        # Create QWebEngineView widget
        self.browser = QWebEngineView()

        # GPT-4o's raw LaTeX response (without delimiters)

        ## Apply regex to wrap LaTeX properly
        #formatted_latex = self.format_latex(latex_raw)

        html_content = MathJaxSOL(latex_raw)
        
        # Load HTML into the QWebEngineView
        self.browser.setHtml(html_content)
        self.setCentralWidget(self.browser)

        # Set window properties
        self.setWindowTitle("MathJax with PySide6")
        self.resize(320, 300)

        
    r"""
    def format_latex(self, text):

        #Detects standalone LaTeX expressions and wraps them in MathJax delimiters.
        #This ensures MathJax can correctly render equations.
        
        block-level equations are properly wrapped
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
    """    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    image = r"images\has\has1.png"
    #latex_raw = GeminiOCR(image)
    latex_raw = r'''\[x^2 - 5x + 6 = 0\]\[x = \frac{-(-5) \pm \sqrt{(-5)^2 - 4(1)(6)}}{2(1)}\]\[x = \frac{5 \pm \sqrt{25 - 24}}{2}\]\[x = \frac{5 \pm 1}{2}\]\[x = \frac{6}{2} \quad \text{or} \quad x = \frac{4}{2}\]\[x = 3 \quad \text{or} \quad x = 2\]
    '''
    print(latex_raw)
    window = MathJaxApp(latex_raw)
    window.show()
    sys.exit(app.exec())

import sys
import re
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from ocr import GeminiOCR

# Define HTML content with MathJax
def MathJaxSOL(latex_raw):
    # Convert Markdown horizontal rule (---) to HTML with extra spacing
    processed_content = re.sub(r'^---+$', r'<hr class="separator">', latex_raw, flags=re.MULTILINE)

    # Process Markdown headings before sending to MathJax
    processed_content = re.sub(r'### (.*?)(?=\n|$)', r'<h3>\1</h3>', latex_raw)
    
    # Convert "Step X:" format to bold text
    processed_content = re.sub(r'(Step \d+:)', r'<b>\1</b>', processed_content)
    
    # Convert "Final Answer:" to bold text
    processed_content = re.sub(r'(Final Answer:)', r'<b>\1</b>', processed_content)
    
    # Highlight correctness evaluations
    processed_content = processed_content.replace("is Correct", "<span class='correct'>is Correct</span>")
    processed_content = processed_content.replace("is Incorrect", "<span class='incorrect'>is Incorrect</span>")
    
    # Style score information
    processed_content = re.sub(r'(Solution = .*?%)', r'<div class="score">\1</div>', processed_content)
    processed_content = re.sub(r'(Final Answer = .*?%)', r'<div class="score">\1</div>', processed_content)
    processed_content = re.sub(r'(Overall Score = .*?%)', r'<div class="overall-score">\1</div>', processed_content)
    
    # Convert newlines to <br> tags to preserve formatting
    processed_content = processed_content.replace('\n', '<br>')
    
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
                font-size: 16px;
                padding: 10px;
                font-family: Arial, sans-serif;
                overflow: auto; /* Enable scrolling if needed */
                border: 1px solid rgb(208, 172, 220);
            }}
            .math-container {{
                text-align: left;
                line-height: 1.5;
            }}
            h3 {{
                color: rgb(255, 200, 87); /* Goldish color for headings */
                margin-top: 15px;
                margin-bottom: 10px;
                font-size: 18px;
            }}
            b {{
                color: rgb(150, 255, 150); /* Light green for steps */
            }}
            .correct {{
                color: rgb(100, 255, 100); /* Green for correct items */
            }}
            .incorrect {{
                color: rgb(255, 100, 100); /* Red for incorrect items */
            }}
            .score {{
                margin-top: 10px;
                color: rgb(200, 200, 255); /* Light blue for scores */
                font-weight: bold;
            }}
            .overall-score {{
                color: rgb(255, 255, 150); /* Light yellow for overall score */
                font-weight: bold;
                font-size: 18px;
                margin-top: 5px;
            }}
            .separator {{
                height: 1px;
                background-color: rgb(150, 150, 150);
                border: none;
                margin-top: 25px;
                margin-bottom: 25px;
            }}
        </style>
    </head>
    <body>
        <div class="math-container">
            {processed_content}
        </div>
    </body>
    </html>
    """
    return html_content



def MathJaxRes(latex_raw):
    processed_content = re.sub(r'^---+$', r'<hr class="separator">', latex_raw, flags=re.MULTILINE)

    # Process Markdown headings before sending to MathJax
    processed_content = re.sub(r'### (.*?)(?=\n|$)', r'<h3>\1</h3>', latex_raw)
    
    # Convert "Step X:" format to bold text
    processed_content = re.sub(r'(Step \d+:)', r'<b>\1</b>', processed_content)
    
    # Convert "Final Answer:" to bold text
    processed_content = re.sub(r'(Final Answer:)', r'<b>\1</b>', processed_content)
    
    # Highlight correctness evaluations
    processed_content = processed_content.replace("is Correct", "<span class='correct'>is Correct</span>")
    processed_content = processed_content.replace("is Incorrect", "<span class='incorrect'>is Incorrect</span>")
    
    # Style score information
    processed_content = re.sub(r'(Solution = .*?%)', r'<div class="score">\1</div>', processed_content)
    processed_content = re.sub(r'(Final Answer = .*?%)', r'<div class="score">\1</div>', processed_content)
    processed_content = re.sub(r'(Overall Score = .*?%)', r'<div class="overall-score">\1</div>', processed_content)
    
    # Convert newlines to <br> tags to preserve formatting
    processed_content = processed_content.replace('\n', '<br>')

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
                font-size: 16px;
                padding: 10px;
                font-family: Arial, sans-serif;
                overflow: auto; /* Enable scrolling if needed */
                border: 1px solid rgb(208, 172, 220);
            }}
            .math-container {{
                text-align: left;
                line-height: 1.5;
            }}
            h3 {{
                color: pink; /* Goldish color for headings */
                margin-top: 15px;
                margin-bottom: 10px;
                font-size: 18px;
            }}
            b {{
                color: pink; /* Light green for steps */
            }}
            .correct {{
                color: rgb(100, 255, 100); /* Green for correct items */
            }}
            .incorrect {{
                color: rgb(255, 100, 100); /* Red for incorrect items */
            }}
            .score {{
                margin-top: 10px;
                color: rgb(175, 192, 220);; /* Light blue for scores */
                font-weight: bold;
            }}
            .overall-score {{
                color: rgb(255, 200, 87); /* Light yellow for overall score */
                font-weight: bold;
                font-size: 18px;
                margin-top: 5px;
            }}
            .separator {{
                height: 1px;
                background-color: rgb(150, 150, 150);
                border: none;
                margin-top: 25px;
                margin-bottom: 25px;
            }}
        </style>
    </head>
    <body>
        <div class="math-container">
            {processed_content}
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
        self.resize(360, 360)

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    latex_raw = r'''(2 solution steps)
### 1. Solve x in the linear equation:
\[ 2x - 3 = -3x + 7 \]	
\[ 2x + 3x = 7 + 3 \]
\[ \frac{5x}{5} = \\frac{10}{5} \]
\[ x = 2 \]


(7 solution steps)
### 2. Solve the system of two linear equations:
\[ \begin{cases} 2x + y = 5 \\ x - 3y = 1 \end{cases} \]

\[ x - 3y = 1 \] 
\[ x = 3y + 1 \] 

\[ \text{Substitute \( x = 3y + 1\) into the first equation} \]
\[ 2x + y = 5 \] 
\[ 2(3y + 1) + y = 5 \] 
\[ 6y + 2 + y = 5 \] 
\[ 7y = 3 \] 
\[ y = \frac{3}{7} \] 

\[ \text{Solve for x:} \]
\[ x - 3y = 1 \] 
\[ x - 3\left(\frac{3}{7}\right) = 1 \] 
\[ x = 1 + \frac{9}{7} \] 
\[ x = \frac{16}{7} \]
\[ \boxed{\left( \frac{16}{7}, \frac{3}{7} \right)} \]



(5 solution steps)
### 3. Solve this quadratic equation using the quadratic formula:
\[ x^2 - 5x + 6 \]

\[ \text{Substitute quadratic formula:} \]
\[ x = \frac{-(-5) \pm \sqrt{-5^2 - 4 (1) (6)}}{2 (1)} \]
\[ x = \frac{5 \pm \sqrt{25 - 24}}{2} \]
\[ x = \frac{5 \pm 1}{2} \]
\[ x = \frac{6}{2} \quad \text{, or} \quad x = \frac{4}{2}\]
\[ x = 3 \quad \text{, or} \quad x = 2\]



(4 solution steps)
### 4. Simplify the expression:
\[ (4xy^{-3})^2 \]
\[ \text{Distribute exponent:} \]
\[ (4xy^{-3})^2 \]
\[ = 4^2 \cdot x^2 \cdot (y^{-3})^2 \]
\[ Compute:\]
\[ 4^2 = 16 \]
\[ x^2 = x^2 \]
\[ (y^{-3})^2 = y^{-6} \]
\[ \frac{16x^2}{y^6} \]

    '''
    latex_raw_2 = r'''
### Problem 1: \[ 2x - 3 = -3x + 7 \]
Step 1 is Correct: \[\frac{-(-5) \pm \sqrt{-5^2 - 4 (1) (6)}}{2 (1)} \]
Step 2 is Incorrect: \[ x = 1 - \frac{9}{7} \] also has an incorrect sign, \( -\frac{9}{7} \). It should be \[ x = 1 + \frac{9}{7} \]
Final Answer is Correct: \[ x = 2 \]

Solution = (4/6)54 = 36%
Final Answer = 46%
Overall Score = 82%
''' 
    print(latex_raw)
    window = MathJaxApp(latex_raw_2)
    window.show()
    sys.exit(app.exec())
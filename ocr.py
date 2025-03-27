import os
import google.generativeai as genai
import time

print("imports done")
# System runtime timer



# function to send images to gemini
def upload_to_gemini(genai, path, mime_type=None):
    file = genai.upload_file(path, mime_type=mime_type)
    print(f"Uploaded file '{file.display_name}' as: {file.uri}")
    return file

def GeminiOCR(image):
    gen_model = genai
    gen_model.configure(api_key="AIzaSyA8E5xI2z_K9D14--1yN62zjIVnFVcfvI4") # Replace with your API Key

    # commands the ai will follow
    rules = (
        "You are an expert at Optical Character Recognition (especially in handwritten characters), only generating the extracted text from the image and nothing else"
        "Extract the full step-by-step math solution exactly as shown in the image, including mistakes in the solution. Do not omit any numbers or symbols."
        "Include the full mathematical problem setup or statement"
        r"Display them in a well documented latex code starting and ending each line with delimiters '\[...\]'"
        "If included in the image, also extract the name of the writer of the solution, typically at the top left of the image. "
        "Count the number of solution steps, excluding the problem equation and the final answer, but including all intermediate steps. "
        "Identify the problem equation separately if possible. If not, assume the first expression is the problem equation. "
        "Format the result in JSON with the following structure:\n"
        "{\n"
        '  "name": "<Name of writer if available>",\n'
        '  "expressions": ["<Extracted LaTeX Expression 1>", "<Expression 2>", ...],\n'
        '  "problem_equation": "<Extracted problem equation if identifiable>",\n'
        '  "layers": <count the number of layers in the solution, including the problem and final answer>,\n'
        '  "solution_steps": <count the number of solution steps>,\n'
        '  "message": "<Message \"The image does not contain any mathematical expression.\" if no math expressions are found>"\n'
        "}"
    )

    # Gemini model and its configuration 
    model = gen_model.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config= {
            "temperature": 0.2,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
    )

    chat_session = model.start_chat(history=[{"role": "user", "parts": [rules]}])
    response = chat_session.send_message([upload_to_gemini(gen_model, image, mime_type="image/png")]) # gemini prompt

    return response.text

if __name__ == "__main__":
    image = r"images\answerkey\20250322202128.jpg"
    print(GeminiOCR(image))
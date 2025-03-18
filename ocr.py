import os
import google.generativeai as genai
import time

print("imports done")
# System runtime timer


genai.configure(api_key="AIzaSyA8E5xI2z_K9D14--1yN62zjIVnFVcfvI4") # Replace with your API Key

# function to send images to gemini
def upload_to_gemini(path, mime_type=None):
    file = genai.upload_file(path, mime_type=mime_type)
    print(f"Uploaded file '{file.display_name}' as: {file.uri}")
    return file

def GeminiOCR(image):

    # commands the ai will follow
    rules = (
        "You are an expert at Optical Character Recognition (especially in handwritten characters), only generating the extracted text from the image and nothing else"
        "Extract the full step-by-step math solution exactly as shown in the image, preserving all fractions in a slashed format. Do not omit any numbers or symbols."
        "Display them in a latex code starting and ending each line with delimiters '$$...$$'"
        "If included in the image, also extract the name of the writer of the solution, typically at the top left of the image"
        "If there is not even a single mathematical expression from the image, only state 'The image does not contain any mathematical expression.' and nothing else"
        "The results should be in plain text format."
    )

    # Gemini model and its configuration 
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config= {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
    )

    chat_session = model.start_chat(history=[{"role": "user", "parts": [rules]}])
    response = chat_session.send_message([upload_to_gemini(image, mime_type="image/png")]) # gemini prompt

    return response.text

if __name__ == "__main__":
    image = r"images\has\has1.png"
    print(GeminiOCR(image))
import os
import google.generativeai as genai
import json  # Import JSON for structured output

print("Imports done")

# Configure Gemini API
genai.configure(api_key="AIzaSyA8E5xI2z_K9D14--1yN62zjIVnFVcfvI4")  # Replace with your actual API Key

# Function to send images to Gemini
def upload_to_gemini(path, mime_type=None):
    file = genai.upload_file(path, mime_type=mime_type)
    print(f"Uploaded file '{file.display_name}' as: {file.uri}")
    return file

def GeminiOCR(image):
    # Structured response format instruction
    rules = (
        "You are an expert at Optical Character Recognition (especially in handwritten characters), only generating the extracted text from the image and nothing else. "
        "Extract the full step-by-step math solution exactly as shown in the image, preserving all fractions in a slashed format. Do not omit any numbers or symbols. "
        "Display them in a LaTeX code starting and ending each line with delimiters '\[...\]'. "
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

    # Gemini model configuration with structured output
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config={
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_mime_type": "application/json",  # Ensuring JSON output
        }
    )

    chat_session = model.start_chat(history=[{"role": "user", "parts": [rules]}])
    response = chat_session.send_message([upload_to_gemini(image, mime_type="image/png")])  # Send image

    # Parse JSON response
    try:
        result = json.loads(response.text)  # Convert response to dictionary
        if "layers" in result:
            result["solution_steps"] = max(result["layers"] - 2, 0)  # Ensure non-negative step count
        return result
    except json.JSONDecodeError:
        print("Error: Unable to decode JSON response.")
        return {"error": "Invalid JSON output from Gemini."}

if __name__ == "__main__":
    image = r"ASHASCUGPT-4o-main\images\has\blank_paper.png"
    result = GeminiOCR(image)

    # Ensure output directory exists
    output_dir = "json_files_test"
    os.makedirs(output_dir, exist_ok=True)

    # Define output file path
    output_file = os.path.join(output_dir, "output.json")

    # Save JSON output to file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)

    print(f"JSON file saved at: {output_file}")

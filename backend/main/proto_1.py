import time
import re
from PIL import Image
from transformers import TrOCRProcessor
from optimum.onnxruntime import ORTModelForVision2Seq

# Record the start time
start_time = time.time()

# Load the processor and model
processor = TrOCRProcessor.from_pretrained('breezedeus/pix2text-mfr')
model = ORTModelForVision2Seq.from_pretrained('breezedeus/pix2text-mfr', use_cache=False)

# List of image file paths
image_paths = [
    #'HAS_images/processed_image.png',
    #'main/HAS_images/LE_1.jpg',
    'main/HAS_images/test1.png'
]

# Iterate over each image path
for image_fp in image_paths:
    try:
        # Load the image
        image = Image.open(image_fp).convert('RGB')

        # Preprocess and perform OCR
        pixel_values = processor(images=image, return_tensors="pt").pixel_values
        generated_ids = model.generate(pixel_values)
        generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)

        # Clean up the output to remove \qquad and other LaTeX spacing commands
        cleaned_text = [re.sub(r'\\qquad|\\quad|\\,|\\:', '', text) for text in generated_text]

        # Output the cleaned result
        print(f'Generated text for {image_fp}: {cleaned_text[0]}\n')

    except FileNotFoundError:
        print(f"Error: The file '{image_fp}' was not found.")
    except Exception as e:
        print(f"An error occurred while processing {image_fp}: {e}")

# Record the end time
end_time = time.time()

# Calculate and print the total runtime
total_runtime = end_time - start_time
print(f"Total runtime: {total_runtime:.2f} seconds")

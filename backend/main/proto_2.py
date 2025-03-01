import time
import re
import os
from PIL import Image
from transformers import TrOCRProcessor
from optimum.onnxruntime import ORTModelForVision2Seq, ORTOptimizer, AutoOptimizationConfig
import torch
from torch.utils.data import DataLoader
from torchvision import transforms
from tqdm import tqdm

# Function to load and preprocess images
def load_images(image_paths):
    images = []
    for image_fp in image_paths:
        try:
            image = Image.open(image_fp).convert('RGB')
            images.append(image)
        except FileNotFoundError:
            print(f"Error: The file '{image_fp}' was not found.")
        except Exception as e:
            print(f"An error occurred while processing {image_fp}: {e}")
    return images

# Function to perform OCR on a batch of images
def ocr_batch(images, processor, model, device):
    pixel_values = processor(images=images, return_tensors="pt").pixel_values.to(device)
    generated_ids = model.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)
    # Clean up the output to remove \qquad and other LaTeX spacing commands
    cleaned_text = [re.sub(r'\\qquad|\\quad|\\,|\\:', '', text) for text in generated_text]
    return cleaned_text

# Main function
def main():
    # Record the start time
    start_time = time.time()

    # Load the processor and model
    processor = TrOCRProcessor.from_pretrained('breezedeus/pix2text-mfr')
    model = ORTModelForVision2Seq.from_pretrained('breezedeus/pix2text-mfr', use_cache=False)

    # Optimize the model
    optimizer = ORTOptimizer.from_pretrained(model)
    optimization_config = AutoOptimizationConfig.O2()
    optimized_model_dir = "./optimized_model"
    optimizer.optimize(save_dir=optimized_model_dir, optimization_config=optimization_config)
    model = ORTModelForVision2Seq.from_pretrained(optimized_model_dir, use_cache=False)

    # Move model to GPU if available
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)

    # List of image file paths
    image_dir = 'HAS_images'
    image_paths = [os.path.join(image_dir, img) for img in os.listdir(image_dir) if img.endswith(('.png', '.jpg', '.jpeg'))]

    # Load and preprocess images
    images = load_images(image_paths)

    # Define batch size
    batch_size = 4

    # Create DataLoader for batch processing
    dataloader = DataLoader(images, batch_size=batch_size, shuffle=False)

    # Iterate over batches
    for batch in tqdm(dataloader, desc="Processing Batches"):
        cleaned_texts = ocr_batch(batch, processor, model, device)
        for image_fp, text in zip(image_paths, cleaned_texts):
            print(f'Generated text for {image_fp}: {text}\n')

    # Record the end time
    end_time = time.time()

    # Calculate and print the total runtime
    total_runtime = end_time - start_time
    print(f"Total runtime: {total_runtime:.2f} seconds")

if __name__ == "__main__":
    main()

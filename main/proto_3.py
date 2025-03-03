#! pip install pix2text>=1.1
import requests
from io import BytesIO
from PIL import Image

from pix2text import Pix2Text, merge_line_texts

def download_img(url):
    response = requests.get(url)
    image_file = BytesIO(response.content)
    return Image.open(image_file).convert('RGB')

image_fps = [
    'https://raw.githubusercontent.com/breezedeus/Pix2Text/main/docs/examples/formula.jpg',
    'https://raw.githubusercontent.com/breezedeus/Pix2Text/main/docs/examples/math-formula-42.png',
]
images = [download_img(img_fp) for img_fp in image_fps]

p2t = Pix2Text.from_config()
outs = p2t.recognize_formula(images, return_text=True)  # recognize pure formula images
print('outs for pure formula images', outs)

mixed_img_fp = 'https://raw.githubusercontent.com/breezedeus/Pix2Text/main/docs/examples/en1.jpg'
mixed_img = download_img(mixed_img_fp)

outs2 = p2t.recognize(mixed_img, file_type='text_formula', return_text=True, save_analysis_res='en1-out.jpg')  # recognize mixed images
print(outs2)
from IPython.display import display
display(Image.open('en1-out.jpg'))
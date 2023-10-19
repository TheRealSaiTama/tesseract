import pytesseract
import os 
from PIL import Image

os.environ['TESSDATA_PREFIX'] = '/usr/share/tesseract-ocr/4.00/tessdata/'
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

def convert():
    try:
        if os.path.exists('img.jpg'):
            img = Image.open('img.jpg')
            text = pytesseract.image_to_string(img)
            print(text)
        else:
            print('Image file not found')
    except Exception as e:
        print(f'Error: {e}')

convert()
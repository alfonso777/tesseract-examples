#!/usr/bin/python
import sys
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename), lang='por')
    return text

if __name__ == "__main__":
    image_path = sys.argv[1]
    #print(ocr_core('images/example_1.png'))
    print(ocr_core(image_path))

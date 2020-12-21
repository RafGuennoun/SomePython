# Install the tesseract package from this website
# https://github.com/UB-Mannheim/tesseract/wiki

# install the pytesseract package with the command
# pip install pyteserract

import pytesseract
import os
from PIL import Image

# Path to the tesseract.exe already installed in our pc
# For me G:\OCR\tesseract.exe is the path for the tesseract in my pc
pytesseract.pytesseract.tesseract_cmd= r"G:\OCR\tesseract.exe"


def convert():

    # The variable that contains the image
    img = Image.open('img.png')

    # The variable that will contain the text of the image
    text = pytesseract.image_to_string(img)

    # And here is our text from the imageg
    print(text)

convert()
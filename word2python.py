import shutil
import docx2txt
import pytesseract
from docx import *
import cv2
import os

detected_word = []
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Tesseract-OCR\tesseract.exe'
imagedir = ("C:\\Users\\image")
text = docx2txt.process("C:\\Users\\text1.docx", 'C:\\Users\\image') 

for image in os.listdir(imagedir):
    image_path = os.path.join(imagedir,image)
    if os.path.isfile(image_path):
        img = cv2.imread(image_path)
        imageText = pytesseract.image_to_string(img)
        detected_word.append(imageText)
        try:
            if os.path.isfile(image_path) or os.path.islink(image_path):
                os.unlink(image_path)
            elif os.path.isdir(image_path):
                shutil.rmtree(image_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (image_path, e))

detected_word.append(text)

for match in detected_word:
    if "shut" in match:
        print("yes")

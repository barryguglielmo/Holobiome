from PIL import Image
import pytesseract
print('success at pyt')
import os
os.chdir("C:/Users/barry/Desktop/Holobiome__Local")
im = Image.open("sample1.jpg")
txt = pytesseract.pytesseract.image_to_string(im, lang='eng')

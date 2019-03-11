# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: ocr_recognize.py
@time: 2019/3/11
"""
import pytesseract
from PIL import Image

tesseract_cmd = r'F:/tesseract_ocr/Tesseract-OCR/tesseract.exe'

image = Image.open('./sample/randomimage1.jpg')
code = pytesseract.image_to_string(image,
                                   # config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789'
                                     lang='eng',
                                    config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'
                                   )
print(code)
print(type(code))


# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: captcha_recognize.py
@time: 2019/3/14
"""


def captcha_recognize(file_path):
    from PIL import Image
    import pytesseract
    image = Image.open(file_path)
    image = image.convert('RGBA')
    pix_data = image.load()
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            if pix_data[x, y][0] == 100 and pix_data[x, y][1] == 150 and pix_data[x, y][2] == 150:
                pix_data[x, y] = (255, 255, 255, 255)

    image_str = pytesseract.image_to_string(image,
                                       lang='eng',
                                       config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'
                                       )
    return image_str


if __name__ == "__main__":
    code = captcha_recognize('./sample/randomimage1.jpg')
    print(code)
    print(type(code))


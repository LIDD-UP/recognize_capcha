# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: image_capcha_testg.py
@time: 2019/3/12
"""
from PIL import Image
from captcha.image import ImageCaptcha
import matplotlib.pyplot as plt
import numpy as np
import random


if __name__ == '__main__':
    captcha_text_list = []
    for i in range(6):
        captcha_text_list.append(str(random.choice([0,1,2,3,4,5,6,7,8,9])))
    captcha_text = ''.join(captcha_text_list)
    print(captcha_text)
    image = ImageCaptcha(height=30, width=100)
    image_captcha = image.generate(captcha_text)
    image_captcha = Image.open(image_captcha)
    image_captcha_array = np.array(image_captcha)
    print(image_captcha_array.shape)
    # plt.plot(image_captcha)
    plt.tight_layout()
    plt.imshow(image_captcha_array)
    plt.show()

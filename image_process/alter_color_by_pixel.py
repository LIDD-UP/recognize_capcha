# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: alter_color_by_pixel.py
@time: 2019/3/12
"""
from captcha.image import ImageCaptcha
from PIL import Image


image = Image.open('../sample/randomimage1.jpg')

print('p_mode',image.mode)
print(image.getcolors())
pxdata_P = image.load()
print('P_load',pxdata_P)
image = image.convert('RGBA')
print('RGB_mode',image.mode)
print(image.getcolors())
pixdata = image.load()
print('rgb_load',pixdata)
# print(image.font)

# print(image.show())
for y in range(image.size[1]):
    for x in range(image.size[0]):
        if pixdata[x,y][0]==100 and pixdata[x,y][1]==150 and pixdata[x,y][2]==150:
           pixdata[x, y] = (255, 255, 255,255)

print(image.getcolors())
# image.show()
image.save('../sample/process2.png','PNG')




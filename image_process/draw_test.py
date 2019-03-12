# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: draw_test.py
@time: 2019/3/12
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


from PIL import Image, ImageDraw, ImageFont
# get an image
base = Image.open('Pillow/Tests/images/hopper.png').convert('RGBA')

# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype('FreeMono.ttf', 40)
# get a drawing context
d = ImageDraw.Draw(txt)

# draw text, half opacity
d.text((10,10), "Hello", font=fnt, fill=(255,255,255,128))
# draw text, full opacity
d.text((10,60), "World", font=fnt, fill=(255,255,255,255))

out = Image.alpha_composite(base, txt)

out.show()






























































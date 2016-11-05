#/usr/bin/python3
#coding:utf-8
from PIL import Image
im = Image.open('img/gril.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((1150, 575))
im.save('img/thumb.jpg', 'JPEG')

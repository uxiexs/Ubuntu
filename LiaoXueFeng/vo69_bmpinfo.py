#!/usr/bin/python3
# coding:utf-8

#*************************************************************************
# 编写一个bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。
#*************************************************************************
import struct


def bmp(path):
    with open(path, 'rb') as f:
        byte = f.read(30)  # 打开BMP位图文件->二进制模式 读取前30个字节
        rb = struct.unpack('<ccIIIIIIHH', byte)  # unpack把bytes变成相应的数据类型
        if rb[0] == b'B' and rb[1] == b'M':
            return ('图片大小: %s bytes\n图片分辨率: %s x %s\n颜色数: %s ' % (rb[2], rb[6], rb[7], rb[-1]))
        else:
            raise TypeError('It\'s not a bmp file! ')

path = '/home/uxeix/Pictures/bmp/robit.bmp'
path2 = '/home/uxeix/Pictures/Wallpapers/cold-wallpaper-3.jpg'
print(bmp(path))
print(bmp(path2))

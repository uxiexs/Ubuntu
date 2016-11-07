#!/usr/bin/python3
# encoding: utf-8
"""
@version: 3.52
@author: Uxeix
@license: Apache Licence 
@contact: Uxeixs@gmail.com
@site: https://github.com/uxiexs
@software: PyCharm
@file: vo43_propertyTest.py.py
@time: 2016/11/7 23:11
"""

#***********************************************************************
# 利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
#***********************************************************************

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise ValueError('width must be a integer')
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        if not isinstance(value,int):
            raise ValueError('height must be a integer')
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height
s = Screen()
s.height = 1024
s.width = 768
print(s.resolution)
print('1027*768 = %d ?' % s.resolution)
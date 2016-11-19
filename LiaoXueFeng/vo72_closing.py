#!/usr/bin/python3
# encoding: utf-8
"""
@version: 3.52
@author: Uxeix
@license: Apache Licence 
@contact: Uxeixs@gmail.com
@site: https://github.com/uxiexs
@software: PyCharm
@file: vo72_closing.py.py
@time: 2016/11/19 14:57
"""
from contextlib import closing, contextmanager
from urllib.request import urlopen

# *********************************************************************************************************
# @closing
# 如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()：
# *********************************************************************************************************
with closing(urlopen('http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001478651770626de401ff1c0d94f379774cabd842222ff000')) as page:
    with open('./file/closing.html','a') as f:
        for line in page:
            line = line.decode('utf-8')
            f.write(line)
        f.close()

# closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单：
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
# 它的作用就是把任意对象变为上下文对象，并支持with语句。
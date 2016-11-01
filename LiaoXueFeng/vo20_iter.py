#/usr/bin/python3
# coding:utf-8

#*************************************************************************
# 判断一个对象是否是Iterable对象
#*************************************************************************
from collections import Iterable


def isIterable(e):
    return isinstance(e, Iterable)

print('List属于可迭代对象:', isIterable([]))  # list
print('dict属于可迭代对象:', isIterable({}))  # dict
print('set属于可迭代对象:', isIterable(set(['a', 'b', 'c']))) # set
print('tuple属于可迭代对象:',isIterable(('U','x','e','i'))) # tuple
print('str属于可迭代对象:', isIterable('abc'))  # str
print('generator属于可迭代对象:',isIterable(x**x for x in range(10))) #generator
print('number属于可迭代对象:', isIterable(100)) #number

#*******************************************************************************
# 我们已经知道，可以直接作用于for循环的数据类型有以下几种：
# 一类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator，包括生成器和带yield的generator function。
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#*******************************************************************************

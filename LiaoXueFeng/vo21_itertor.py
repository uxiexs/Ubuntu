#/usr/bin/python3
# coding:utf-8
from collections import Iterator
#*************************************************************************
# 判断一个对象是否属于itertor
#*************************************************************************


def isIterator(e):
    return isinstance(e, Iterator)

print('List属于迭代器:', isIterator([]))  # list
print('dict属于迭代器:', isIterator({}))  # dict
print('set属于迭代器:', isIterator(set(['a', 'b', 'c'])))  # set
print('tuple属于迭代器:', isIterator(('U', 'x', 'e', 'i')))  # tuple
print('str属于迭代器:', isIterator('abc'))  # str
print('generator属于迭代器:', isIterator(x**x for x in range(10)))  # generator
print('number属于迭代器:', isIterator(100))  # number

#*************************************************************************
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
#*************************************************************************

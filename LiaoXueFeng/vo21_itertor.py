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
print('generator属于迭代器:', isIterator(x**x for x in range(10))) #generator
print('number属于迭代器:', isIterator(100))  # number

#/usr/bin/python3
# coding:utf-8

#******************************************************************************
# Python本身就内置了很多非常有用的模块，只要安装完毕，这些模块就可以立刻使用。
# 以内建的sys模块为例，编写一个hello的模块：
#******************************************************************************

' a test module '
__author__ = 'Uxeix'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello,World')
    elif len(args) == 2:
        print('Hello %s!' % args[1])
    else:
        print('Too many arguments!')
if __name__ == '__main__':
    test()

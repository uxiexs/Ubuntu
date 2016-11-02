#/usr/bin/python3
# coding:utf-8
import functools
import time
#*************************************************************************
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
#*************************************************************************


# def now():
#     print(time.ctime())
# f = now
# print(now.__name__)
# print(f.__name__)
# print(f == now)
# f()

#*************************************************************************
# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now() # 函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator， # 可以定义如下：
#*************************************************************************


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def local_time():
    print(time.ctime())
local_time()

#/usr/bin/python3
#coding:utf-8
import functools

#*******************************************************************************
# 在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来 # 实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python        # 的decorator可以用函数实现，也可以用类实现。
# decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。
# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
# 再思考一下能否写出一个@log的decorator，使它既支持：
# @log
# def f():
#    pass
# 又支持:
# @log('execute')
#   def f():
#     pass
#*******************************************************************************

# 调用方式@log 或者 @log('xxxx')
def log(args):
    text = "" if callable(args) else args
    def decorator(func):
        @functools.wraps(func)
        def wrapeer(*args,**kw):
            print("begin %s %s():" %(text,func.__name__))
            r = func(*args,**kw)
            print("end %s %s()" %(text,func.__name__))
            return r
        return wrapeer
    return decorator(args) if callable(args) else decorator

@log('excute')
def func1():
    print("I'm func1,I excuted")
func1()
print('\n'+'**********************************************************************'+'\n')
@log
def func2():
    print("I'm func2,I excuted")
func2()

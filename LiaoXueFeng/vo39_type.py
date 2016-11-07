#/usr/bin/python3
# coding:utf-8

#*************************************************************************
# 基本类型都可以用type()判断：
#*************************************************************************

print(type(123), type(1.23), type('str'),
      type(True), type([]), type(()), type({}))

#*************************************************************************
# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types # 模块中定义的常量：
#*************************************************************************
import types


def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(int) == types.BuiltinFunctionType)
print(type(pow) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type(x for x in range(5)) == types.GeneratorType)

#*************************************************************************
# 使用isinstance()
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使          # 用isinstance()函数。
#*************************************************************************


class Animals(object):
    pass


class Dog(Animals):
    pass


class Husky(Dog):
    pass
a = Animals()
d = Dog()
h = Husky()
print(isinstance(h, Husky))
print(isinstance(h, Dog))
print(isinstance(h, Animals))
print(isinstance(d, Animals))
print(isinstance(d, Husky))

#*************************************************************************
# 能用type()判断的基本类型也可以用isinstance()判断：
#*************************************************************************
print(isinstance('a', str), isinstance(1, int), isinstance(1.20, float))
print(isinstance([], list), isinstance((), tuple), isinstance({}, dict))

#*************************************************************************
# 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，  # 获得一个str对象的所有属性和方法：
#*************************************************************************
print(dir('abc'))
print('Abc'.lower())

#*************************************************************************
# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接    # 操作一个对象的状态：
#*************************************************************************


class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x
obj = MyObject()

# 测试该对象的属性：
print('是否有属性 x:', hasattr(obj, 'x'))
print('打印属性 x:' + '\n', obj.x)
print('是否有属性 y:', hasattr(obj, 'y'))
setattr(obj, 'y', 88)
print('是否有属性 y:', hasattr(obj, 'y'))
print('打印属性 y:', obj.y)
print(getattr(obj,'x'),getattr(obj,'y'))
print(getattr(obj,'z',404))
print(obj.x+obj.y)

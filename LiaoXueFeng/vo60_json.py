#!/usr/bin/python3
# encoding: utf-8
"""
@version: 3.52
@author: Uxeix
@license: Apache Licence 
@contact: Uxeixs@gmail.com
@site: https://github.com/uxiexs
@software: PyCharm
@file: vo60_json.py.py
@time: 2016/11/12 16:57
"""

# ********************************************************************************************************
# JSON
# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，
# 可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
# JSON类型	Python类型
#  {}	     dict
#  []	     list
# "string"	 str
# 1234.56	int或float
# true/false True/False
#  null	     None
# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：
# ********************************************************************************************************
import json


# d = dict(name='Bob', age=20, score=88)
# print(json.dumps(d))

# ***********************************************************************************************************
# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
# ***********************************************************************************************************

# json_str = '{"age":20, "score":88, "name":"Bob"}'
# print(json.loads(json_str))

# ***********************************************************************************************************
# 由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换。
# ***********************************************************************************************************

# ***********************************************************************************************************
# JSON进阶
# Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：
# ***********************************************************************************************************

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)


# print(json.dumps(s))


# ***********************************************************************************************************
# 错误的原因是Student对象不是一个可序列化为JSON的对象。
# 如果连class的实例对象都无法序列化为JSON，这肯定不合理！
# 别急，我们仔细看看dumps()方法的参数列表，可以发现，除了第一个必须的obj参数外，dumps()方法还提供了一大堆的可选参数：
# https://docs.python.org/3/library/json.html#json.dumps
# 这些可选参数就是让我们来定制JSON序列化。前面的代码之所以无法把Student类实例序列化为JSON，是因为默认情况下，dumps()方法不知道如何将Student
# 实例变为一个JSON的{}对象。
# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：
# ***********************************************************************************************************

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


# 这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON：
print(json.dumps(s, default=student2dict))
# 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
print(json.dumps(s, default=lambda obj: obj.__dict__))


# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把
# dict转换为Student实例：

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age":20, "score":88,"name":"Bob"}'
print(json.loads(json_str,object_hook=dict2student)) # 打印出的是反序列化的Student实例对象。

#***********************************************************************************************************
# 小结
# Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。
# json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。但是，当默认的序列化或反序列机制不满足我们
# 的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，既做到了接口简单易用，又做到了充分的扩展性和灵活性。
#***********************************************************************************************************

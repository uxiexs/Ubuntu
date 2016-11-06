#!/usr/bin/python3
# encoding: utf-8
"""
@version: 3.52
@author: Uxeix
@license: Apache Licence 
@contact: Uxeixs@gmail.com
@site: https://github.com/uxiexs
@software: PyCharm
@file: vo36_class.py.py
@time: 2016/11/6 21:25
"""
#**************************************************************
# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，\
# 如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
# 定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的：
#**************************************************************
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s : %s' %(self.name,self.score))
    def get_grade(self):
        if self.score>=90:
            return 'A'
        elif self.score>=60:
            return 'B'
        else:
            return 'C'
#**************************************************************
# 可以看到，变量bart指向的就是一个Student的实例，后面的0x10a67a590是内存地址，每个object的地址都不一样，而Student本身则是一个类。
#**************************************************************
bart = Student('Bart Simple',59)
koro = Student('Koro Simple',60)
print(bart)
print(koro)
print(Student)
# print(bart.name,bart.score)
# print(koro.name,koro.score)

#***************************************************************
# 数据封装
# 面向对象编程的一个重要特点就是数据封装。在上面的Student类中，每个实例就拥有各自的name和score这些数据。我们可以通过函数来访问这些数据，
# 比如打印一个学生的成绩：
#***************************************************************
def print_score(std):
    return ('%s: %s' %(std.name,std.score))
# print(print_score(bart))
bart.print_score()
print(bart.get_grade())
print(koro.get_grade())

#***************************************************************
# 小结
# 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
# 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
# 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
#***************************************************************
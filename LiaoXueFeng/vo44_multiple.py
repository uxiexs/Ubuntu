#/usr/bin/python3
#coding:utf-8

#*******************************************************************************
# 继承是面向对象编程的一个重要的方式，因为通过继承，子类就可以扩展父类的功能。
# 回忆一下Animal类层次的设计，假设我们要实现以下4种动物：
# Dog - 狗狗
# Bat - 蝙蝠
# Parrot - 鹦鹉
# Ostrich - 鸵鸟
# 正确的做法是采用多重继承。首先，主要的类层次仍按照哺乳类和鸟类设计：
#*******************************************************************************

# 父类: 动物
class Animal(object):
    pass
# 父类: 奔跑能力
class Runnable(object):
    def run(self):
        return 'Running...'
# 父类: 飞行能力
class Flyable(object):
    def run(self):
        return 'Flying...'
# 大类: 哺乳类
class Mammal(Animal):
    pass

# 大类: 鸟类
class Bird(Animal):
    pass

# 子类: 狗狗
class Dog(Mammal,Runnable):
    pass

# 子类: 蝙蝠
class Bat(Mammal, Flyable):
    pass

# 子类: 鹦鹉
class Parrot(Bird, Flyable):
    pass

# 子类: 鸵鸟
class Ostrich(Bird, Runnable):
    pass


d = Dog() # 狗狗实例化
print('狗狗是动物:',isinstance(d,Animal))
print('狗狗可以飞:',isinstance(d,Flyable))
print('狗狗可以跑:',isinstance(d,Runnable))

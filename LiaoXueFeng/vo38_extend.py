#/usr/bin/python3
#coding:utf-8

#*******************************************************************************
# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类 #（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。
# 比如，我们已经编写了一个名为Animal的class，有一个run()方法可以直接打印：
#*******************************************************************************

class Animals(object):

    def run(self):
        print('Animal is running')

class Dog(Animals):
    def run(self):
        return 'Dog is running'
        # print('Dog is running')
    def eat(self):
        return 'Eat meat'

class Cat(Animals):
    def run(self):
        return 'Cat is running'
    def eat(self):
        return 'Eat fish'

class Tortoise(Animals):
    def run(self):
        return 'Tortoise is running slowly!'

class Timer(object):
    def run(self):
        return 'Timer start ...'
def run_twice(animal):
    return animal.run()+'\n'+animal.run()

    # animal.run()

dog = Dog() # 对于Dog，Animal就是它的父类，对于Animal，Dog是它的子类。Cat和Dog类似。
# print(dog.run())
#*******************************************************************************
# 继承有什么好处？最大的好处是子类获得了父类的全部功能。由于Animial实现了run()方法，因此   # Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法：
#*******************************************************************************
cat = Cat()
print(cat.run(),cat.eat())

# run_twice(Animals())
print(run_twice(Dog()))
print(run_twice(Tortoise()))
print(run_twice(Timer()))

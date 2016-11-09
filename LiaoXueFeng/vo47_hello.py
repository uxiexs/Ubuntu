#/usr/bin/python3
# coding:utf-8

#*************************************************************************
# 当Python解释器载入hello模块时，就会依次执行该模块的所有语句，执行结果就是动态创建出      # 一个Hello的class对象，测试如下：
#*************************************************************************


class Hello(object):

    def hello(self, name='王迅洋'):
        print('我喜欢%s' % name)

#*************************************************************************
# metaclass
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
# metaclass，直译为元类，简单的解释就是：
# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
# 但是如果想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
# 所以，metaclass允许你创建类或者修改类。换句话说，可以把类看成metaclass创建出来的“实例”。
# 我们先看一个简单的例子，这个metaclass可以给我们自定义的MyList增加一个add方法：
# 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这 # 是一个metaclass：
#*************************************************************************

# metaclass是类的模板，所以必须从`type`类型派生：


class ListMetaclass(type):

    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字     # 参数metaclass：

class MyList(list,metaclass=ListMetaclass):
    pass
# ***********************************************************************
# 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，      # 要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，   # 然后，返回修改后的定义。
# __new__()方法接收到的参数依次是：
# 1.当前准备创建的类的对象；
# 2.类的名字
# 3.类继承的父类集合
# 4.类的方法集合
# ***********************************************************************

# 测试一下MyList是否可以调用add()方法：
L = MyList()
L.add(1)
L.add(2)
print(L)

#/usr/bin/python3
# coding:utf-8

#*************************************************************************
# 定制类
#*************************************************************************


class Student(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return ('Student Object (name: %s)' % self.name)
    __repr__ = __str__

Student('WangXunYang')


class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self   # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b

        if self.a > 1000:
            raise StopIteration()
        return self.a


# for n in Fib():
#     print (n)

class Fib1(object):

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f1 = Fib1()
print(f1[0], f1[1], f1[2], f1[3])


class Fib2(object):

    def __getitem__(self, n):
        if isinstance(n, int):   # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
f2 = Fib2()
print(f2[:10])

#*************************************************************************
# __getattr__
#*************************************************************************


class Student1(object):

    def __init__(self):
        self.name = '王迅洋'

    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25
        raise AttributeError(
            '\'Student1\' object has not attribute \'%s\'' % attr)
Wang = Student1()
print('name: %s age: %s' % (Wang.name, Wang.age()))
# print(Wang.s)

#*******************************************************************************
# 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
# 这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。
# 举个例子:
# 现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
# http://api.server/user/friends
# http://api.server/user/timeline/list
# 如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
# 利用完全动态的__getattr__，我们可以写出一个链式调用：
#*******************************************************************************

class Chain(object):
    def __init__(self,path=''):
        self._path = path
    def __getattr__(self,path):
        return Chain('%s/%s' %(self._path,path))
    def __str__(self):
        return self._path
    __repr__ = __str__

print(Chain().status.user.WangXunYang)

#***********************************************************
# __call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？
# 在Python中，答案是肯定的
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：
#***********************************************************
class Student3(object):
    def __init__(self,name):
        self.name = name
    def __call__(self, *args, **kwargs):
        return ('My name is %s' %self.name)
s3 = Student3('王迅洋')
print(s3()) # self参数不要传入
#*****************************************************************************************
# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就
# 没啥根本的区别。
# 如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。
# 那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们
# 上面定义的带有__call__()的类实例：
#*****************************************************************************************
print('Student是否能被调用:',callable(Student))
print('Student1是否能被调用:',callable(Student1))
print('Fib是否能被调用:',callable(Fib))
print('Fib1是否能被调用:',callable(Fib1))
print('Fib2是否能被调用:',callable(Fib2))
print('Chain是否能被调用:',callable(Chain))
print('字符串st是否能被调用:',callable('st'))
print('Integer 2是否能被调用:',callable(2))
print('List [1,2,3]是否能被调用:',callable([1,2,3]))
#********************************************************
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
#********************************************************

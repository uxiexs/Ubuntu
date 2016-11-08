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

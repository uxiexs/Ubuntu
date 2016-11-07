#/usr/bin/python3
# coding:utf-8

#*************************************************************************
# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以  # 把成绩随便改 这显然不合逻辑。
# 为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()     # 来获取成绩，这样，在set_score()方法里，就可以检查参数
#*************************************************************************


class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer')
        elif value < 0 or value > 100:
            raise ValueError('score must between 0~100 !')
        self._score = value

Lily = Student()
Lily.set_score(60)
# print(Lily.get_score())

#*************************************************************************
# 上面的调用方法又略显复杂，没有直接用属性这么直接简单。
# Python内置的@property装饰器就是负责把一个方法变成属性调用的
#*************************************************************************


class Student1(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score muste be integer')
        elif value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

s1 = Student1()
s1.score = 99
print(s1.score)

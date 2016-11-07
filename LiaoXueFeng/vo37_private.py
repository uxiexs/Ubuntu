#/usr/bin/python3
# coding:utf-8

#*************************************************************************
# 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就 # 隐藏了内部的复杂逻辑
#*************************************************************************


class Studuent(object):

    def __init__(self, name, score):
        self.__name = name  # 要让内部属性不被外部访问，属性的名称前需加上两个下划线__
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return ('%s : %s' % (self.__name, self.__score))

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

s = Studuent('ux', 88)
k = Studuent('king', 98)
print(s.get_name())
# s.set_score(99)
#*******************************************************************************
# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因      # 为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name # 来访问__name变量：
#*******************************************************************************
print(s._Studuent__name)

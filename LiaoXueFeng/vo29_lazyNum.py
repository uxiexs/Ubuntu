#/usr/bin/python3
# coding:utf-8

#*************************************************************************
# 调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
#*************************************************************************


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum
n = int(input("请输入要求和的范围(ex:100 = 100以内的所有值的和):"))
f = lazy_sum(*map(int, list(x for x in range(n+1))))
print(type(f))
print(f())

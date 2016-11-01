#/usr/bin/python3
# coding:utf-8
from functools import reduce
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把  # 结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)


def add(x, y):
    return x + y

# r1 = reduce(add, [x for x in range(1, 10, 2)])


def charToNums(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def fn(x, y):
    return x * 10 + y


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(charToNums,s))

# r2 = reduce(fn, map(charToNums, '13579'))

s = str(input("输入要转换成int的数字:"))
print(str2int(s))

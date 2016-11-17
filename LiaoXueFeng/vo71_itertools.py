#!/usr/bin/python3
#coding:utf-8

import itertools

# count()会创建一个无限的迭代器:
natuals = itertools.count(0)

# for n in natuals:
#     if n <= 100:
#         print(n)

# cycle()会把传入的一个序列无限重复下去：
# cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
#
# for c in cs:
#     print(c)
# 同样停不下来。

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
# ns = itertools.repeat('A', 3)
# for n in ns:
#     print(n)

# 无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。

# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
# natuals2 = itertools.count(1)
# ny = itertools.takewhile(lambda x: x <= 10, natuals2)
# s = set(ny)
# k = list(s)
# print(k)

#*******************************************************************************
# chain()
# 把一组迭代对象串联起来，形成一个更大的迭代器：
#*******************************************************************************
for n in itertools.chain('abc',[1,2,3]):
    print(n)

#*******************************************************************************
# groupby()
# 把迭代器中相邻的重复元素挑出来放在一起：
#*******************************************************************************
for key, group in itertools.groupby('aaabbbccdd'):
    print(key,list(group))
#实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组，而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
for key, group in itertools.groupby('AaaBbbCcDd', lambda x: x.upper()):
    print(key,list(group))

#*******************************************************************************
# 小结
# itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。
#*******************************************************************************

#/usr/bin/python3
#coding:utf-8
from functools import reduce
#*******************************************************************************
# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利 # 用reduce()求积：
#*******************************************************************************

def prod(L):
    if L == None:
        return '无名氏'
    else:
        cname = [letter.lower() for letter in L]
        cname[0] = cname[0].upper()
        return ''.join(cname)

l1 = input("输入要转换的字符串:")
l2 = str.split(l1,',')
l3 = list(map(prod,l2))
print(l3)

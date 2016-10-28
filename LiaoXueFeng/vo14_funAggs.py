#/usr/bin/python3
#coding:utf-8
#************
#可变参数
#************
a = input("a: ")
b = input("b: ")
c = input("c: ")
args = (a,b,c)

def funAggs(a,b,c,*args):
    return 'a: ',a,'b: ',b,'other: ',args

print(funAggs(a,b,c,*args))

#/usr/bin/python3
#coding:utf-8

g = (x * x for x in range(11))
arr = []
def getGenaral(g):
    for n in g:
        arr.append(n)
getGenaral(g)
print(arr)

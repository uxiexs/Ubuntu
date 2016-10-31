#/usr/bin/python3
#coding:utf-8

#*********************************************************
# 杨辉三角的实现
#*********************************************************
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0);
        L = [L[i-1] + L[i] for i in range(len(L))]

def trianglesPrint(times):
    n = 0
    for t in triangles():
        print(t)
        n = n + 1
        if n == times:
            break
times = input('输入杨辉三角的层级:')
trianglesPrint(int(times))

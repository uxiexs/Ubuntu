#/usr/bin/python3
# coding:utf-8
import math

#*************************************************************************
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0
#*************************************************************************
a, b, c = input("请输入参数a:"), input("请输入参数b:"), input("请输入参数c:")


def quadratic(a, b, c):
    a, b, c = int(a), int(b), int(c)
    d = b**2 - 4 * a * c  # 求值公式
    if d < 0:
        return "参数无解"
    elif d == 0:
        return (-d / (2 * a))
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2

print(quadratic(a, b, c))

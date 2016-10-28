#/usr/bin/python3
# coding:utf-8

#*************
# 关键字参数
#*************


def fun(name=input("name: "), age=input("age: "), **kw):
    return {'name': name, 'age': age, 'other': kw}

print(fun(color="red"))

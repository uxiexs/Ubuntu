#!/usr/bin/python3
#coding:utf-8

#*******************************************************************************
# 注册
#*******************************************************************************

# 从vo70_getMd5模块中引用get_md5函数:接收参数,返回MD5值
from vo70_getMd5 import get_md5

def register(username, password): #接收用户名,密码
    md5_pwd = get_md5(username+password+'the_salt') # 生成md5(用户名+密码+自定义)
    with open('/home/uxeix/workspace/LiaoXueFeng/file/user.list','a') as f:
        f.write(username+':'+md5_pwd+'\r\n')

if __name__ == '__main__':
    username = input('请输入用户名: ')
    password = input('请输入密码: ')
    register(username,password)

#!/usr/bin/python3
#coding:utf-8

#*******************************************************************************
# 登录
#*******************************************************************************
from vo70_getMd5 import get_md5

# 检测: 用户名,密码不可为空
def check(username,password):
    if username == '':
        print('用户名不能为空')
        return False
    elif password == '':
        print('密码不能为空')
        return False

# 登录成功后的提示
def login_success(username):
    print('%s 登录成功' % username)


# 检测:用户名 密码  并根据匹配程度返回不同的值(flag)
def check_pwd(line, username, password):
    if len(line.strip()) == 0:
        return
    L = line.strip() # 去除空格
    L = L.split(':') # 分割当前行(uxeixs:d276419c7755686b7e58837efcb42e13)为List
    if L[0] != username:
        return 1 # 用户名不存在返回1
    elif L[0] == username:
        if L[1] != password:
            return 2 # 用户名匹配 密码不匹配 返回2
        elif L[1] == password:
            return 3 # 用户名与密码都匹配 返回3

# 登录
def login(username,password):
    # 先检测用户密码是否为空:
    if check(username,password) is False:
        return
    # 将用户输入的用户名与密码加密成MD5
    md5_pwd = get_md5(username+password+'the_salt')

    # 与用户名密码存储文件内的数据对比
    with open('/home/uxeix/workspace/LiaoXueFeng/file/user.list', 'r') as f:
        # 遍历文件内的数据对比
        for line  in f.readlines():
            # 当用户名被包含在某行时,执行匹配操作
            if username in line:
                # 获取flag
                flag = check_pwd(line, username, md5_pwd)
                # 根据flag的不同做不同的处理
                if flag == 1:
                    print('用户名不存在')
                    return
                elif flag == 2:
                    print('密码错误')
                    return
                elif flag == 3:
                    login_success(username)
                    return
if __name__ == '__main__':
    username = input('请输入用户名: ')
    password = input('请输入密码: ')
    login(username, password)

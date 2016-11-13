#!/usr/bin/python3
# encoding: utf-8
"""
@version: 3.52
@author: Uxeix
@license: Apache Licence 
@contact: Uxeixs@gmail.com
@site: https://github.com/uxiexs
@software: PyCharm
@file: vo63_threadLocal.py.py
@time: 2016/11/13 17:10
"""
#*****************************************************************************************************
# 在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，
# 而全局变量的修改必须加锁。但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦：
# ThreadLocal应运而生，不用查找dict，ThreadLocal帮你自动做这件事：
#*****************************************************************************************************
import threading, os

#创建全局ThreadingLocal对象
local_school = threading.local()

def process_student():
    #获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s) pid: %s tid: %s' % (std, threading.current_thread().name, os.getpid(), threading.current_thread().ident))

def process_thread(*args):
    #绑定ThreadLocal的student:
    local_school.student = args
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice','Alex'), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# 全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。你可以把local_school看成全局
# 变量，但每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。
# 可以理解为全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等。
# ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
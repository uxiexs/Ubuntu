#!/usr/bin/python3
# encoding: utf-8
"""
@version: 3.52
@author: Uxeix
@license: Apache Licence 
@contact: Uxeixs@gmail.com
@site: https://github.com/uxiexs
@software: PyCharm
@file: vo64_taskWorker.py.py
@time: 2016/11/13 23:21
"""

# task_worker.py
# 客户端，从服务器的任务队列中获取任务，进行计算并放入结果队列

import time
# import sys
import queue
from multiprocessing.managers import BaseManager
# from multiprocessing import freeze_support


# 创建继承自BaseManager的QueueManager
class QueueManager(BaseManager):
    pass


# ??modified
def start_worker():
    # 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    # 连接到服务器，也就是运行task_master.py的机器
    # 任务进程要通过网络连接到服务进程，所以要指定服务进程的IP
    server_addr = '127.0.0.1'   # 服务器地址
    server_port = 5000          # 服务器端口
    print('Connect to server %s...' % server_addr)

    # 端口和验证码需要保持与task_master.py中设置的完全一致
    manager = QueueManager(address=(server_addr, server_port), authkey=b'abc')

    # 从网络连接
    manager.connect()

    # 获取Queue的对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 从task队列取任务，并把结果写入result队列
    for i in range(10):
        try:
            n = task.get(timeout=1)
            print('run task %d * %d...' % (n, n))
            r = '%d * %d = %d' % (n, n, n * n)
            time.sleep(1)
            result.put(r)
        except queue.Empty:
            print('task queue is empty.')

    # 处理结束
    print('worker exit.')
# ??

if __name__ == '__main__':
    # freeze_support()        # 注释掉也可以正常运行
    start_worker()
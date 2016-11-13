#!/usr/bin/python3
# encoding: utf-8
"""
@version: 3.52
@author: Uxeix
@license: Apache Licence 
@contact: Uxeixs@gmail.com
@site: https://github.com/uxiexs
@software: PyCharm
@file: vo64_taskManage.py.py
@time: 2016/11/13 22:46
"""

#**************************************************************************
# 分布式进程
# 在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。
# Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。一个服务进程可以作为调度者，将任务分布到其他
# 多个进程中，依靠网络通信。由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。
# 举个例子：如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，现在，由于处理任务的进程任务繁重，希望把发送任务的进程和处理任务的进程
# 分布到两台机器上。怎么用分布式进程实现？
# 原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了。
# 我们先看服务进程，服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务：
#**************************************************************************
# 当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，
# 但是，在分布式多进程环境下，添加任务到Queue不可以直接对
# 原始的task_queue进行操作，那样就绕过了QueueManager的封装，
# 必须通过manager.get_task_queue()获得的Queue接口添加。
import random
# import time
import queue
from multiprocessing.managers import BaseManager
# from multiprocessing import freeze_support   # 不用加也可以正常启动服务器

# 发送任务的队列
task_queue = queue.Queue()

# 接收结果的队列
result_queue = queue.Queue()


# modified
def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass


# 注册到网络
# modified
def start_server():
    # modified
    # 把两个Queue都注册到网络上，callable参数关联了Queue对象
    # register内不要使用lambda，否则win7运行出错
    # callable=lambda: task_queue => callable=return_task_queue
    # callable=lambda: result_queue => callable=return_result_queue
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)

    # 绑定端口5000，设置验证码'abc'
    # win7 需要写ip地址
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

    # 启动Queue
    manager.start()

    # 获得通过网络访问的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放几个任务进去
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)

    # 从result队列读取结果
    print('Try get results...')
    # 服务器已经准备好接收数据，故开始启动task_worker.py
    for i in range(10):
        try:
            r = result.get(timeout=10)
            print('Result: %s' % r)
        except queue.Empty:     # Queue.Empty => queue.Empty
            print('result queue is empty.')

    # 关闭
    manager.shutdown()
    print('master exit.')

if __name__ == '__main__':
    # freeze_support()      # 注释掉也可以正常运行
    start_server()
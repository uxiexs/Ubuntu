#!/usr/bin/python3
# encoding: utf-8
"""
@version: 3.52
@author: Uxeix
@license: Apache Licence 
@contact: Uxeixs@gmail.com
@site: https://github.com/uxiexs
@software: PyCharm
@file: vo61_multiprocessing.py.py
@time: 2016/11/13 12:28
"""

#*************************************************************************************************
# 如果你打算编写多进程的服务程序，Unix/Linux无疑是正确的选择。由于Windows没有fork调用，难道在Windows上无法用Python编写多进程的程序？
# 由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。
# multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：
#*************************************************************************************************
# from multiprocessing import Process
# import os

#子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' %(name, os.getpid()))
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end')

#********************************************************************************************************
# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
#********************************************************************************************************

#********************************************************************************************************
# Pool
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
#********************************************************************************************************
# from multiprocessing import Pool
# import os, time, random
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random()*3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' %(name, (end-start)))
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

# import subprocess
# print('$ nslookup www.baidu.com')
# r = subprocess.call(['nslookup', 'www.baidu.com'])
# print('Exit code:',r)

#*******************************************************************************************************
# 进程间通信
# Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes
# 等多种方式来交换数据。
# 我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
#*******************************************************************************************************
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    # 父进程创建Queue,并传给多个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入：
    pw.start()
    # 启动子进程pr, 读取：
    pr.start()
    # 等待pw结束：
    pw.join()
    # pr进程是死循环，无法等待其结束，需强行终止：
    pr.terminate()

#***************************************************************************************************
# 在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。由于Windows没有fork调用，因此，
# multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，所有，如果multiprocessing
# 在Windows下调用失败了，要先考虑是不是pickle失败了。
#***************************************************************************************************

#***************************************************************************************************
# 小结
# 在Unix/Linux下，可以使用fork()调用实现多进程。要实现跨平台的多进程，可以使用multiprocessing模块。
# 进程间通信是通过Queue、Pipes等实现的。
#***************************************************************************************************


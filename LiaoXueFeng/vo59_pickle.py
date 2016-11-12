#!/usr/bin/python3
# encoding: utf-8
"""
@version: 3.52
@author: Uxeix
@license: Apache Licence 
@contact: Uxeixs@gmail.com
@site: https://github.com/uxiexs
@software: PyCharm
@file: vo59_pickle.py.py
@time: 2016/11/12 16:10
"""

# *************************************************************************************************************
# 在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict：
# d = dict(name='Bob', age=20, score=88)
# 可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。如果没有把修改后的'Bill'存储到磁盘上，
# 下次重新运行程序，变量又被初始化为'Bob'。
# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，
# flattening等等，都是一个意思。
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
# Python提供了pickle模块来实现序列化。
# 首先，我们尝试把一个对象序列化并写入文件：
# *************************************************************************************************************
import pickle

# d = dict(name='Bob', age=20, score=88)
# print(pickle.dumps(d))

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个
# file-like Object：

# f = open('file/dump.txt', 'wb')
# pickle.dump(d,f)
# f.close()

# 看看写入的dump.txt文件，一堆乱七八糟的内容，这些都是Python保存的对象内部信息。
# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个
# file-like Object中直接反序列化出对象。我们打开另一个Python命令行来反序列化刚才保存的对象：
f = open('file/dump.txt','rb')
d = pickle.load(f)
f.close()
print(d)

#*************************************************************************************************************
# 变量的内容又回来了！
# 当然，这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。
# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些
# 不重要的数据，不能成功地反序列化也没关系。
#*************************************************************************************************************
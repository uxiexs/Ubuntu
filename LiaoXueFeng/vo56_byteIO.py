#/usr/bin/python3
#coding:utf-8

#*******************************************************************************
# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
#*******************************************************************************
from io import StringIO;

f = StringIO();
print(f.tell())
f.write('Hello World');
print(f.tell())
f.seek(0)
print(f.tell())
s = f.readline();
print (s)

#/usr/bin/python3
# coding:utf-8

#*************************************************************************
# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
#*************************************************************************
from io import BytesIO
f = BytesIO()
print(f.write('中文'.encode('utf-8')))
print(f.getvalue())

# 请注意，写入的不是str，而是经过UTF-8编码的bytes。和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：

f1 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f1.read())

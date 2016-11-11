#/usr/bin/python3
#coding:utf-8

#*******************************************************************************
# the stream position 当你用：
# d = StringIO('Hello World')
# 其stream position为0（可以通过d.tell()获得），而后执行
# d.readline()
# stream position移动到11.因此在执行此方法时，返回的是空字符串。
# 类似的，使用 f = StringIO() stream position也为0，而执行f.write('Hello World')
# stream position就移动到11了，因此你再执行readline时返回的依旧是空字符串，若你需要返回'Hello World'可以通过f.seek(0) 调整stream position即可。
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

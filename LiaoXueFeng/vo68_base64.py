#!/usr/bin/python3
#coding:utf-8

#*******************************************************************************
# Base64是一种用64个字符来表示任意二进制数据的方法。
# 用记事本打开exe、jpg、pdf这些文件时，我们都会看到一大堆乱码，因为二进制文件包含很多无法显示和打印的字符，所以，如果要让记事本这样的文本处理软件能处理二进制数据，就需要一个二进制到字符串的转换方法。Base64是一种最常见的二进制编码方法。
# 如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。
# Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
# 能处理去掉=的base64解码函数：
#*******************************************************************************
import base64
def safe_base64_decode(s):
    str_s = s.decode('ascii')
    length = len(str_s)
    while(length % 4 != 0):
        str_s = str_s + '='
        length = length + 1

    bit_s = str_s.encode('ascii')
    base64_s = base64.b64decode(bit_s)
    return base64_s
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')

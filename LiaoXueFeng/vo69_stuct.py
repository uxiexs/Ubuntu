#!/usr/bin/python3
#coding:utf-8

#*******************************************************************************
# 准确地讲，Python没有专门处理字节的数据类型。但由于b'str'可以表示字节，所以，字节数组＝二进制str。而在C语言中，我们可以很方便地用struct、union来处理字节，以及字节和int，float的转换。
# Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
#*******************************************************************************
import struct
# struct的pack函数把任意数据类型变成bytes：
print(struct.pack('>I',861715))
# pack的第一个参数是处理指令，'>I'的意思是：
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
# unpack把bytes变成相应的数据类型：
print( struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。

import io

with io.open ('/home/uxeix/Pictures/bmp/robit.bmp','rb') as file:
    head_bytes = file.read(30)
    print(s)
    print(struct.unpack('<ccIIIIIIHH', head_bytes))

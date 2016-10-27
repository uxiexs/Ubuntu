#/usr/bin/python3
#coding:utf-8

#字符转ascii
input_word = input('请输入要转换ascii的文字：') #输入需要转换为ascii的字符串
temp = []                                    #创建加密字符串空列表
for i in input_word:                         #ascii需要一个字节一个字节的转换
    x = bin(ord(i))                               #转码
    temp.append(x)                           #将每一个字符添加到列表中
print(temp)

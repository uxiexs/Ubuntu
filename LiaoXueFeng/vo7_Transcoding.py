#/usr/bin/python3
# coding:utf-8

# 字符转ascii
input_word = input('请输入要转换ascii的文字：')  # 输入需要转换为ascii的字符串
temp = []  # 创建加密字符串空列表
for i in input_word:  # ascii需要一个字节一个字节的转换
    # x = ord(i)  # 转码(十进制)
    # x = bin(ord(i))  # 转码(二进制)
    # x = oct(ord(i))  # 转码(八进制)
    x = hex(ord(i))  # 转码(十六进制)
    temp.append(x)  # 将每一个ascii添加到列表中
print(temp)

# ascii转字符
char = []  # 创建加密字符串空列表
word = ''  # 创建空字符串
for asc in temp:
    # j = chr(int(asc)) #十进制转码为字符
    # j = chr(int(asc, base=2))  # 二进制转码为字符
    # j = chr(int(asc, base=8))  # 八进制转码为字符
    j = chr(int(asc, base=16))  # 十六进制转码为字符
    word += j  # 拼接字符串
    char.append(j)  # 将每一个字符添加到列表中
print(char)
print(word)

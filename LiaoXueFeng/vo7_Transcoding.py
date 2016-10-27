#/usr/bin/python3
# coding:utf-8

# 字符转ascii
input_word = input('请输入要转换ascii的文字：')  # 输入需要转换为ascii的字符串
temp = []  # 创建加密字符串空列表
for i in input_word:  # ascii需要一个字节一个字节的转换
    x = ord(i)  # 转码
    temp.append(x)  # 将每一个ascii字符添加到列表中
print(temp)

#ascii转字符
char = [] #创建加密字符串空列表
word = '' #创建空字符串
for asc in temp:
    j = chr(int(asc)) #转码
    word += j #拼接字符串
    char.append(j) # 将每一个字符添加到列表中
print(char)
print(word)

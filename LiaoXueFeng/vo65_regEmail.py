#!/usr/bin/python3
#coding:utf-8

#*******************************************************************************
# 练习
# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
#*******************************************************************************
import re
str1 = 'jimmy.Wang@zzu.edu.cn'
r1 = r'([a-zA-Z][a-zA-Z0-9\.]*)@(\w+\.\w+)'
def regExp(r,s):
    if re.match(r, s):
        return 'ok'
    else:
        return 'failed'
print(regExp(r1,str1))

# 版本二可以验证并提取出带名字的Email地址：
str2 = '<Tom Paris> tom@voyager.org'
r2 = r'<([a-zA-Z]+?)\s+[a-zA-Z]+>\s+([a-zA-Z]+?@[a-zA-Z0-9]+?\.\w+)'
email2 = re.compile(r2)
m  = email2.match(str2)
print(regExp(r2,str2))
print('%s \'s email: %s' % (m.group(1), m.group(2)))

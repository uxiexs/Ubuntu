#!/usr/bin/python3
# encoding: utf-8
"""
@version: 3.52
@author: Uxeix
@license: Apache Licence 
@contact: Uxeixs@gmail.com
@site: https://github.com/uxiexs
@software: PyCharm
@file: vo74_useHtmlParser.py.py
@time: 2016/11/20 20:00
"""

#*************************************************************************************************
# 练习
# 找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，然后尝试解析一下HTML，
# 输出Python官网发布的会议时间、名称和地点。
#*************************************************************************************************
import requests
from bs4 import BeautifulSoup

resp = requests.get('https://www.python.org/events/python-events/')
# resp = requests.get('https://mail.google.com/mail/u/0/#inbox/')
soup = BeautifulSoup(resp.text, 'html.parser')

for li in soup.select('.list-recent-events > li'):
    print('title:',li.find('a').text)
    print('time:' ,li.find('time').text)
    print('location:',li.select_one('.event-location').text)
    print('*' * 100)
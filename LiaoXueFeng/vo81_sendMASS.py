#!/usr/bin/python3
#coding:utf-8

from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr, formatdate

import smtplib


# def prompt(prompt):
#     return input(prompt).strip()


# return Alias_name <xxxx@example.com>
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'uxeixs@126.com'                # 用户的邮件地址
# from_addr = prompt('From: ')                # 用户的邮件地址
password = '870125xx'            # 用户的邮件密码
# password = prompt('Password: ')            # 用户的邮件密码
to_addrs = ['406602271@qq.com','koulaxx@163.com','uxeixs@gmail.com']           # 收件人邮件地址
# to_addrs = prompt('To: ').split()           # 收件人邮件地址
smtp_server = 'smtp.126.com'       # 用户的SMTP服务器地址
# smtp_server = prompt('SMTP server: ')       # 用户的SMTP服务器地址

# 带附件邮件
# 指定subtype为alternative，同时支持html和plain格式
msg = MIMEMultipart('alternative')  #
# 邮件正文为MIMEText
# msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
# 邮件正文中显示图片，同时附件的图片将不再显示
# plain = 'Hello world and hello me!'
# msg.attach(MIMEText(plain, 'plain', 'utf-8'))       # 纯文本
html = '<html><body><h1>Hello</h1><p><img src="cid:0"></p></body></html>'
msg.attach(MIMEText(html, 'html', 'utf-8'))         # HTML
# 添加附件：即关联一个MIMEBase，图片为本地读取
with open('/home/uxeix/Pictures/head/de6bb76ed48a224b0041c55007f9171a.jpg', 'rb') as f:
    # 设置附件中的MIME和文件名
    mime = MIMEBase('image', 'jpeg', filename='hope.jpg')
    # 加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename='hope.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来
    mime.set_payload(f.read())
    # 用Base64编码
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart
    msg.attach(mime)

# 未指定用户别名，则客户端会自动提取邮件地址中的名称作为邮件的用户别名
msg['From'] = _format_addr('linuxforshine<%s>' % from_addr)
msg['To'] = '%s' % ','.join([_format_addr('<%s>' % to_addr) for to_addr in to_addrs])
msg['Subject'] = Header('Getting started with Python', 'utf-8').encode()
msg['Date'] = formatdate()

# 标准的25端口连接SMTP服务器时，使用明文传输，发送邮件的整个过程可能会被窃听。
# 更安全地发送邮件，需加密SMTP会话，即先创建SSL安全连接，再使用SMTP协议发送邮件。
smtp_port = 25                  # smtp.gmail.com:587
server = smtplib.SMTP(smtp_server, smtp_port)   # 创建SMTP实例，默认端口是25
# server.starttls()                               # 创建安全连接
server.set_debuglevel(1)                        # 打印出和SMTP服务器交互的所有信息
server.login(from_addr, password)               # 用来登录SMTP服务器

# 为了可以一次发给多个人，传入一个list
# 邮件正文是一个str，as_string()把MIMEText对象变成str
server.sendmail(from_addr, to_addrs, msg.as_string())   # 发邮件
server.quit()                               # 终止SMTP会话以及关闭连接

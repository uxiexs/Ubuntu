#!/usr/bin/python3
#coding:utf-8

#===============================================================================
# 发送附件
#
# 如果Email中要加上附件怎么办？带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，所以，可以构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象即可：
#===============================================================================
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

import smtplib

#=========================================================================
# _format_addr()来格式化一个邮件地址。注意不能简单地传入name <addr@example.com>，因为  # 如果包含中文，需要通过Header对象进行编码。
#=========================================================================

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 接收参数: 发件人地址
from_addr = 'uxeixs@126.com'

# 接收参数: 客户端授权密码
passwd = '870125xx'

# 接收参数: 收件人地址,可多个
to_addr = '406602271@qq.com'
# to_addr = 'uxeixs@gmail.com'

# 接收参数: SMTP服务器(注意:是发件人的smtp服务器)
smtp_server = 'smtp.126.com'

# 接收参数: 邮件主题
subject = input('邮件主题: ')

# 接收参数: 邮件正文
content = input('邮件正文: ')

#===============================================================================
# 邮件对象
#===============================================================================
msg = MIMEMultipart()
msg['From'] = _format_addr(from_addr)
msg['To'] = _format_addr(to_addr)
msg['Subject'] = Header(str(subject), 'utf-8').encode()

#===============================================================================
# 邮件正文是MIMEText
#===============================================================================
msg.attach(MIMEText(str(content), 'plain', 'utf-8'))

#===============================================================================
# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
#===============================================================================
with open('/home/uxeix/Pictures/head/1.png', 'rb') as f:
    # 设置附件的MIME和文件名,这里是png类型:
    mime = MIMEBase('image', 'png', filename='test.png')
    # 加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件内容读进来
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

#===============================================================================
# 发送邮件
#===============================================================================
try:
    # SMTP服务器设置(地址,端口):
    server = smtplib.SMTP(smtp_server, 25)

    # 连接SMTP服务器(发件人地址, 客户端授权密码)
    server.login(from_addr, passwd)

    # 发送邮件
    server.sendmail(from_addr, [to_addr], msg.as_string())

    print('邮件发送成功')

except smtplib.SMTPException:
    print('邮件发送失败')

finally:
    # 退出SMTP服务器
    server.quit()

#!/usr/bin/python3
# coding:utf-8

#=========================================================================
# SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
# Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
# 首先，我们来构造一个最简单的纯文本邮件：
#=========================================================================
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

#=========================================================================
# _format_addr()来格式化一个邮件地址。注意不能简单地传入name <addr@example.com>，因为  # 如果包含中文，需要通过Header对象进行编码。
#=========================================================================


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 接收参数: 发件人地址
from_addr = 'uxeixs@126.com'

# 接收参数: 密码(客户端授权密码)
password = '870125xx'

# 接收参数: 收件人地址,可以是多个,逗号分隔开.
to_addr = input('收件人邮箱: ')

# 接收参数: SMTP服务器(注意:是发件人的smtp服务器)
smtp_server = 'smtp.126.com'

# 接收参数: 邮件主题
subject = input('邮件主题: ')

# 接收参数: 邮件正文
content = '''<html><body><h1>Hello</h1>
    <p>send by <a href="http://www.python.org">Python</a>...</p>
    </body></html>
    '''

# 构造MIMEText对象:第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'html'表示网页文件，最终的MIME就是'text/html'，最后一定要用utf-8编码保证多语言兼容性。
msg = MIMEText(str(content), 'html', 'utf-8')

# 格式化发件人地址
msg['From'] = _format_addr(from_addr)

# 格式化收件人地址: msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。
msg['To'] = _format_addr(to_addr)

# 邮件主题
msg['Subject'] = Header(str(subject), 'utf-8').encode()

try:
    # SMTP服务器设置(地址,端口)
    server = smtplib.SMTP(smtp_server, 25)

    # 打印出和SMTP服务器交互的所有信息
    # server.set_debuglevel(1)

    # 连接SMTP服务器(发件人邮箱,密码[客户端授权密码])
    server.login(from_addr, password)

    # 发邮件:由于可以一次发给多个人，所以传入一个list 邮件正文是一个str，as_string()把MIMEText对象变成str
    server.sendmail(from_addr, [to_addr], msg.as_string())
    print('邮件发送成功')
except smtplib.SMTPException:
    print('邮件发送失败')
finally:
    # 退出SMTP服务器
    server.quit()

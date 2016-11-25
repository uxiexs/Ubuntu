#!/usr/bin/python3
# coding:utf-8

#=========================================================================
# 加密SMTP
# 使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。要更安全地发送邮件，可以加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。
#=========================================================================
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr, formatdate
import smtplib

# return Alias_name <xxxx@example.com>
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'uxeixs@126.com' # 接收参数: 发件人地址
passwd = '870125xx' # 接收参数: 客户端授权密码
to_addrs = ['406602271@qq.com','koulaxx@163.com','uxeixs@gmail.com'] # 接收参数: 收件人地址,多个
smtp_server = 'smtp.126.com' # 接收参数: SMTP服务器(注意:是发件人的smtp服务器)
subject = input('邮件主题: ') # 接收参数: 邮件主题
plain = input('邮件正文: ') # 接收参数: 邮件正文

msg = MIMEMultipart('alternative') # 指定subtype为alternative，同时支持html和plain格式
msg.attach(MIMEText(str(plain), 'plain', 'utf-8')) # 纯文本
#添加附件：即关联一个MIMEBase，图片为本地读取
with open('/home/uxeix/Pictures/icon/favicon (Jianshu).ico', 'rb') as f:
    mime = MIMEBase('image', 'jpeg', filename='hot.jpg') # 设置附件中的MIME和文件名
    mime.add_header('Content-Disposition', 'attachment',
                    filename='hot.jpg')  # 加上必要的头信息
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read()) # 把附件的内容读进来
    encoders.encode_base64(mime) # 用Base64编码
    msg.attach(mime)  # 添加到MIMEMultipart

# 未指定用户别名，则客户端会自动提取邮件地址中的名称作为邮件的用户别名
msg['From'] = _format_addr(from_addr)
msg['To'] = '%s' % ','.join([_format_addr('<%s>' % to_addr) for to_addr in to_addrs])
msg['Subject'] = Header(str(subject), 'utf-8').encode()
msg['Date'] = formatdate()
#=========================================================================
# 发送邮件
#=========================================================================
try:
    server = smtplib.SMTP_SSL(smtp_server, 465)  # SMTP服务器设置(地址,端口):
    server.login(from_addr, passwd) # 连接SMTP服务器(发件人地址, 客户端授权密码)
    server.sendmail(from_addr, to_addrs, msg.as_string()) # 发送邮件
    print('邮件发送成功')
except smtplib.SMTPException as e:
    print(e)
finally:
    server.quit() # 退出SMTP服务器

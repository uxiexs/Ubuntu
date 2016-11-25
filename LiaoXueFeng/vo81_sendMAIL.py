#!/usr/bin/python3
#coding:utf-8

#===============================================================================
# 简单的基于python3的邮件发送程序
#===============================================================================
import smtplib
from email.mime.text import MIMEText

#===============================================================================
# 第三方 SMTP 服务
#===============================================================================
mail_host = 'smtp.126.com'   # SMTP服务器
mail_user = 'uxeixs@126.com' # 用户名
mail_pass = '870125xx'       # 客户端授权密码

#===============================================================================
# 发件人 与 收件人
#===============================================================================
sender = 'uxeixs@126.com'        # 发件人邮箱
receivers = ['406602271@qq.com','koulaxx@163.com'] # 收件人邮箱

#===============================================================================
# 邮件内容设置
#===============================================================================
content = '<em style="color:red">cool</em>'
title = 'Python SMTP Mail Test'  # 邮件主题
# 指定subtype为alternative，同时支持html和plain格式
msg = MIMEMultipart('alternative')
message = MIMEText(content, 'html', 'utf-8')  # 内容, 格式, 编码
message['From'] = "{}".format(sender)
message['To'] = ",".join(receivers)
message['Subject'] = title

#===============================================================================
# 发送邮件:
# step1: STMP服务器设置
# step2: 连接STMP服务器
# step3: 使用STMP发送邮件[明文或机密]
# step4: 关闭STMP服务器
#===============================================================================
try:
    smtpObj = smtplib.SMTP(mail_host, 25)  # 启用明文发信, 端口25
    # smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
    smtpObj.login(mail_user, mail_pass)  # 登录验证
    smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
    print("mail has been send successfully.")
except smtplib.SMTPException as e:
    print(e)
finally:
    smtpObj.quit()

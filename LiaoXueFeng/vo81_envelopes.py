#!/usr/bin/python3
# coding:utf-8


__author__ = 'Uxeixs'

from envelopes import Envelope, SMTP, GMailSMTP

#=========================================================================
# Envelopes是对Python的email和smtplib库进行封装，使其对email的操作更方便简单。
# 构造envelope:
#=========================================================================
envelope = Envelope(
    from_addr=(u'uxeixs@126.com', u'Uxeix'),           # 发件人 [必选参数]
    to_addr=[u'406602271@qq.com', u'koulaxx@163.com'],  # 收件人 [必选参数]
    subject=u'envelope库的使用',                        # 邮件主题 [必选参数]
    cc_addr=u'uxeixs@gmail.com',                        # 抄送人 [可选参数]
    text_body=u'envelope是一个python库，可以用来发送邮件', # 邮件正文 [必选参数]
)

#=========================================================================
# 添加附件
#=========================================================================
envelope.add_attachment(
    '/home/uxeix/Pictures/list.jpg')

#=========================================================================
# 发送邮件
#=========================================================================
try:
    envelope.send('smtp.126.com', login='uxeixs@126.com', password='你猜')
    print('邮件发送成功')
except Exception as e:
    print(e)

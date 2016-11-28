#!/usr/bin/python3
# coding: utf-8

#=========================================================================
# Python IMAP收取邮件
# IMAP相比单向通信的POP3来说更便捷，体验更好，更可靠。
# 用python来开发邮件接收程序非常的简单，主要还是用两个自带的库就可以了，imaplib库和email库
#=========================================================================
import imaplib
import email

try:
    # 登陆邮箱
    conn = imaplib.IMAP4_SSL(port='993', host='imap.qq.com')
    conn.login('406602271@qq.com', 'aaiauktplbnxbjab')
    conn.select()

    # 取邮件 如果我们要取回第一封邮件可以把newlist[0]传递给fetch()
    type, data = conn.search(None, 'ALL')
    newlist = data[0].split()
    type, data = conn.fetch(newlist[0], '(RFC822)')

    # 从邮件中取出需要的信息: 主题/发件人/收件人/抄送人/发送时间
    msg = email.message_from_string(data[0][1].decode('utf-8'))
    m_sub = msg.get('subject')
    m_from = msg.get('From')
    m_to = msg.get('To')
    m_cc = msg.get('CC')
    m_date = msg.get('Date')
    sub_decode = email.header.decode_header(m_sub)[0][0]

    # 打印: 主题/发件人/收件人/抄送人/发送时间
    print('主题: ', sub_decode.decode('utf-8'))
    print('发件人: ', m_from)
    print('收件人: ', m_to)
    print('抄送人: ', m_cc)
    print('发送日期: ', m_date)

    # 打印: 邮件正文
    for part in msg.walk():
        # 如果ture的话内容是没用的
        if not part.is_multipart():
            print('正文: ', part.get_payload(decode=True).decode('utf-8'))

except Exception as e:
    print(e)

finally:
    conn.close()
    print('断开连接')
    conn.logout()
    print('登出')

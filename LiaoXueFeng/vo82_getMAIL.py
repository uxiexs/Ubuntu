#!/usr/bin/python3
# coding:utf-8

#=========================================================================
# 邮件协议
#
# 在开始之前下面我们来认识一下邮件协议（POP3,IMAP,SMTP）
#
# 协议	功能
# POP3	主要用于客户端远程管理服务器上的邮件
# IMAP	交互式邮件访问协议
# SMTP	简单邮件传输协议
#
# POP3
#
# POP3协议是Post Office Protocol 3的简称，即邮局协议的第3个版本，是TCP/IP协议族中的一员（默认端口是110）。本协议主要用于支持使用客户端远程管理在服务器上的电子邮件。
#
# IMAP
#
# IMAP全称是Internet Mail Access Protocol，即交互式邮件访问协议，是一个应用层协议（端口是143）。用来从本地邮件客户端（Outlook Express、Foxmail、Mozilla Thunderbird等）访问远程服务器上的邮件。
#
# SMTP
#
# SMTP的全称是“Simple Mail Transfer Protocol”，即简单邮件传输协议（25号端口）。它是一组用于从源地址到目的地址传输邮件的规范，通过它来控制邮件的中转方式。SMTP 协议属于 TCP/IP 协议簇，它帮助每台计算机在发送或中转信件时找到下一个目的地。我们知道SMTP协议简单来说就是一个邮件发送的传输协议（不提供邮件接收功能），而POP3和IMAP这两个协议是邮件的接收（下载）协议。那么POP3和IMAP的区别是什么呢？
#
# POP3和IMAP协议的区别
#
# 下面就来说一说这两个协议的主要区别。
# 虽然这两个协议都是从邮件服务器那里下载邮件到本地的协议，但是不同的是IMAP提供跟邮件服务器的双向通信，也即在客户端所作的更改会反馈给服务器端，跟服务器端形成同步（例如删除邮件，创建文件夹等等的操作）。而POP3是单向通信的，即下载邮件到本地就算了，所作的更改都只是在客户端，不会反映到服务器端。所以使用IMAP协议也会更便捷，体验更好，更可靠。
#=========================================================================

#=========================================================================
# 读取邮件
#
# 用python来开发邮件接收程序非常的简单，主要还是用两个自带的库就可以了，imaplib库和email库。一开始先用import把两个库导入进来。
#=========================================================================
import imaplib
import email

try:
    # 登陆邮箱
    conn = imaplib.IMAP4_SSL(port='993', host='imap.qq.com')
    conn.login('406602271@qq.com', 'aaiauktplbnxbjab')
    conn.select()

    # 拉取邮件
    type, data = conn.search(None, 'ALL')

    # 打印邮件 data[0]:默认收件箱
    for num in data[0].split():
        typ, data = conn.fetch(num, '(RFC822)')
        print ('Message %s\n%s\n' % (num, data[0][1].decode('utf-8')))
except Exception as e:
    print(e)

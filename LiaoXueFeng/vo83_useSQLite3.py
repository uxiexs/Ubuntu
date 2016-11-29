#!/usr/bin/python3
#coding:utf-8

#===============================================================================
# SQLite3 查询
#===============================================================================
import sqlite3

try:
    # 连接SQLlite3数据库:
    conn = sqlite3.connect('./vo83_SQLite3.db')
    # 创建游标:
    cursor = conn.cursor()
    # 执行查询语句:
    cursor.execute('select * from user where id=?',('1',))
    # 获取查询结果集:
    values = cursor.fetchall()
    print(values)
except Exception as e:
    print(e)
finally:
    # 关闭游标
    cursor.close()
    # 断开数据库连接
    conn.close()

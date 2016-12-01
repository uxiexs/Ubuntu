#!/home/uxeix/.virtualenvs/py3env/bin/python3
#coding:utf-8

#===============================================================================
# ORM：Object-Relational Mapping，把关系数据库的表结构映射到对象上
# 在Python中，最有名的ORM框架是SQLAlchemy。
#===============================================================================

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker

try:
    # 初始化数据库连接:
    eng= create_engine('postgresql+psycopg2://workspace:123@127.0.0.1:5432/workspace', echo=False, client_encoding='utf-8')
    # 创建session对象:
    DB_Session = sessionmaker(bind=eng)
    session = DB_Session()
    # 获取查询到的数据:
    data = session.execute('select * from %s'%('auth_user'))
    # 操作数据:
    t_data = []
    for row in data:
        row_data = {}
        for index in range(len(row)):
            row_data[row.keys()[index]] = row.values()[index]
        t_data.append(row_data)
    print(t_data)
except Exception as e:
    # 打印错误信息(程序正常则不会执行这段代码)
    print(e)
finally:
    # 断开连接
    session.close()

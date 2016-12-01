#/usr/bin/python3
#coding:utf-8

from sqlalchemy import *
from sqlalchemy.orm import *

try:
    # 初始化数据库连接:
    eng = create_engine('postgresql+psycopg2://workspace:123@127.0.0.1:5432/workspace', echo=True, client_encoding='utf-8')
    # 绑定元信息
    metadata = MetaData(eng)
    m_table = Table('vo84_user', metadata, autoload=True)
    session = create_session()
    query = session.query(m_table)
    data = query.all()
    t_data = []
    # print(data)
    for row in data:
        row_data = {}
        for index in range(len(row)):
            row_data[row.keys()[index]] = row[index]
        t_data.append(row_data)
    print(t_data)
except Exception as e:
    print(e)
finally:
    session.close()

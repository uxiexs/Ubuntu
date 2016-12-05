#!/usr/bin/python3
# coding:utf-8

from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


class Stu(Base):
    # 表的名字:
    __tablename__ = 'Stu'
    # 表的结构:
    SNO = Column(String(7), primary_key=True)
    SNAME = Column(String(8))
    SEX = Column(String(2))
    BDATE = Column(DATETIME)
    DIR = Column(String(16))

    def __repr__(self):
        return "<Stu(SNO='%s', SNAME='%s', SEX='%s',BDATE ='%s',DIR ='%s')>" % \
            (self.SNO, self.SNAME, self.SEX,
             self.BDATE.strftime("%Y-%m-%d"), self.DIR)

try:
    # 初始化数据库连接:
    eng = create_engine('postgresql+psycopg2://workspace:123@127.0.0.1:5432/workspace',
                        echo=False, client_encoding='utf-8')
    # 创建session对象:
    DB_Session = sessionmaker(bind=eng)
    session = DB_Session()
    query = session.query(Stu)
    for s in session.query(Stu):
        print(s)
except Exception as e:
    # 打印错误信息(程序正常则不会执行这段代码)
    print(e)
finally:
    # 断开连接
    session.close()

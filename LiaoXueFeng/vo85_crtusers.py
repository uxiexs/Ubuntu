#!/usr/bin/python3
# coding:utf-8

#=========================================================================
# 表的创建crtusers.py
#=========================================================================
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine(
    'postgresql+psycopg2://workspace:123@127.0.0.1:5432/workspace', echo=False, client_encoding='utf-8')
Base = declarative_base()


class User(Base):
    __tablename__ = 'vo85_users'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    fullname = Column(String(40))
    password = Column(String(12))

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)
Base.metadata.create_all(engine)


class Address(Base):
    __tablename__ = 'vo85_addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(40), nullable=False)
    user_id = Column(Integer, ForeignKey('vo85_users.id'))

    user = relationship("User", back_populates="vo85_addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address

try:

    User.addresses = relationship(
        "Address", order_by=Address.id, back_populates="user")
    Base.metadata.create_all(engine)

    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
    session.add(ed_user)

    session.add_all([User(name='wendy', fullname='Wendy Williams', password='foobar'),
                     User(name='mary', fullname='Mary Contrary',
                          password='xxg527'),
                     User(name='lisa', fullname='lisa Contrary', password='ls123'),
                     User(name='cred', fullname='cred Flinstone',
                          password='bla123'),
                     User(name='fred', fullname='Fred Flinstone', password='blah')])

    jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
    jack.addresses = [Address(email_address='jack@google.com'), Address(
        email_address='j25@yahoo.com')]
    session.add(jack)

    session.commit()

except Exception as e:
    print(e)
finally:
    session.close()

#!/usr/bin/python3
# coding: utf-8

from operator import or_
from sqlalchemy import text
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

from vo85_crtusers import Address, User

engine = create_engine(
    'postgresql+psycopg2://workspace:123@127.0.0.1:5432/workspace', echo=False, client_encoding='utf-8')
DBSession = sessionmaker(bind=engine)
session = DBSession()


query = session.query(User)
for u in query.all():
    print (str(u.id) + ' ' + u.name + ' ' + u.fullname + ' ' + u.password)
for u in session.query(User).order_by(User.id)[1:4]:
    print(u)
for name in session.query(User.name).filter_by(fullname='Ed Jones'):
    print(name)
for u in session.query(User).filter(User.name.isnot(None)):
    print(u)
for u in session.query(User).filter(or_(User.name == 'ed', User.name == 'wendy')):
    print(u)
for u in session.query(User).filter(~User.name.like('%ed')).order_by(User.id):
    print(u)
for u in session.query(User).filter(User.name == 'ed').filter(User.fullname == 'Ed Jones'):
    print(u)
for u in session.query(User).filter(User.name.in_(['ed', 'wendy', 'jack'])):
    print(u)


for user in session.query(User).filter(text("id<224")).order_by(text("id")).all():
    print(user.name)
for u in session.query(User).from_statement\
    (text("SELECT * FROM vo85_users where id >= :id")).\
        params(id=2).all():
    print(u)

for u in session.query(User).from_statement \
    (text("SELECT * FROM vo85_users where name=:name")). \
        params(name='ed').all():
    print(u)

print(session.query(func.count('*')).select_from(User).scalar())
print(session.query(User).filter(User.name.like('%ed')).count())
for n in session.query(func.count(User.name), User.name).group_by(User.name).all():
    print(n)


for u, a in session.query(User, Address).filter(User.id == Address.user_id).\
        filter(Address.email_address == 'jack@google.com').all():
    print(u)
    print(a)

for u in session.query(User).join(Address).filter(Address.email_address == 'jack@google.com').all():
    print(u)
for name, in session.query(User.name).filter(User.vo85_addresses.any(Address.email_address.like('%google%'))):
    print(name)

#/usr/bin/python3
#coding:utf-8

import hashlib

def get_md5(x):
    md = hashlib.md5()
    md.update(x.encode('utf-8'))
    return md.hexdigest()

# print(get_md5('uxeix'))

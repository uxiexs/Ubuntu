#!/home/uxeix/.virtualenvs/py3env/bin/python3
#coding:utf-8

#===============================================================================
# 用Flask编写Web App比WSGI接口简单
# app.py，处理3个URL，分别是：
# GET /：首页，返回Home；
# GET /signin：登录页，显示登录表单；
# POST /signin：处理登录表单，显示登录结果。
#===============================================================================
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1 style="color:pink">你的名字</h1>'

@app.route('/signin', methods=['GET'])
def signin_from():
    return '''<form action="/signin" method="post">
    user:<p><input name="username"></p>
    pass:<p><input name="password" type="password"></p>
    <p><button type="submit">Sign In</button></p>
    </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容:
    if request.form['username'] == 'yourname' and request.form['password'] == '1202':
        return '<h3>宫水三叶</h3>'
    return '<h3>Bad username or password</h3>'

if __name__ == '__main__':
    app.run()

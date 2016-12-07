#!/home/uxeix/.virtualenvs/py3env/bin/python3
#coding:utf-8

#===============================================================================
# 启动WSGI服务器，加载application()函数
#===============================================================================

# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
from vo86_hello import application

# 创建一个服务器,IP地址为空,端口是8000,处理函数是application
httpd = make_server(host='', port=8000, app=application)
print('Server HTTP on port 8000...')

# 开始监听HTTP请求
httpd.serve_forever()

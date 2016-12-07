#!/home/uxeix/.virtualenvs/py3env/bin/python3
# coding:utf-8

#=========================================================================
# Web应用的本质就是：
#
# 浏览器发送一个HTTP请求；
#
# 服务器收到请求，生成一个HTML文档；
#
# 服务器把HTML文档作为HTTP响应的Body发送给浏览器；
#
# 浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。
#=========================================================================


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello %s!</h1>' % (environ['PATH_INFO'][1:] or 'Web')
    return [body.encode('utf-8')]


# 上面的application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：
#
# environ：一个包含所有HTTP请求信息的dict对象；
#
# start_response：一个发送HTTP响应的函数。

#===============================================================================
# 小结
# 无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。HTTP请求的所有输入信息都可以通       # 过environ获得，HTTP响应的输出都可以通过start_response()加上函数返回值作为Body。
#===============================================================================

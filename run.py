#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-16 19:52:18
# Filename        : run.py
# Description     : 

from proxy.app import ProxyApplication
from tornado import httpserver, ioloop


if __name__ == "__main__":
    app = ProxyApplication()
    http_server = httpserver.HTTPServer(app)
    http_server.listen(1111, '127.0.0.1')
    ioloop.IOLoop.instance().start()


#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-13 18:13:59
# Filename        : run.py
# Description     : 

from proxy.app import ProxyApplication
from tornado import httpserver, ioloop
from tornado.options import define, options

define('port', default=1111, help="run on the given port", type=int)

if __name__ == "__main__":
    app = ProxyApplication()
    http_server = httpserver.HTTPServer(app)
    http_server.listen(options.port, '127.0.0.1')
    ioloop.IOLoop.instance().start()


#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-15 19:00:44
# Filename        : run.py
# Description     : 

from proxy.app import ProxyApplication
from tornado import httpserver, ioloop
from tornado import netutil, process


if __name__ == "__main__":
    app = ProxyApplication()
    socket_1111 = netutil.bind_sockets(1111, '127.0.0.1')
    socket_1112 = netutil.bind_sockets(1112, '127.0.0.1')
    socket_1113 = netutil.bind_sockets(1113, '127.0.0.1')
    http_server = httpserver.HTTPServer(app)
    process.fork_processes(0)
    http_server.add_sockets(socket_1111)
    http_server.add_sockets(socket_1112)
    http_server.add_sockets(socket_1113)
    ioloop.IOLoop.instance().start()


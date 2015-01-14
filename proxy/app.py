#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-14 16:49:35
# Filename        : proxy/app.py
# Description     : 
from tornado import web
from os import path
from proxy.core import ProxyHandler
from proxy.module import ProxyModule

class ProxyApplication(web.Application):
    def __init__(self):
        handlers = [
                (r'/.*', ProxyHandler),
                ]
        settings = {
                }
        web.Application.__init__(self, handlers, **settings)


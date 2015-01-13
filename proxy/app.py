#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-13 14:58:07
# Filename        : proxy/app.py
# Description     : 
from tornado import web
from proxy.core import ProxyHandler

class ProxyApplication(web.Application):
    def __init__(self):
        handlers = [
                (r'/.*', ProxyHandler),
                ]
        settings = {
                'debug':True,
                }
        web.Application.__init__(self, handlers, **settings)


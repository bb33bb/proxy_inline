#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-14 13:52:36
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
                'debug':True,
                }
        web.Application.__init__(self, handlers, **settings)


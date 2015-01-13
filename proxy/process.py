#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-13 16:58:13
# Filename        : proxy/process.py
# Description     : 

from proxy.config import config
import re

cfg = config()

class Process():
    def __init__(self, body, request):
        self.request = request
        self.body = body

    def _sub_host(self):
        host = cfg.get('proxy', 'host')
        self.body = self.body.replace(host, self.request.headers['host'])
        

    def process(self):
        self._sub_host()
        return self.body


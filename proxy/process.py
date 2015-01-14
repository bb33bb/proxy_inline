#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-14 12:35:08
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
        #self.body = self.body.replace('https://www.google.com.sg', 'http://%s' % self.request.headers['Host']).replace(host, 
        #        self.request.headers['Host'])
        self.body = self.body.replace(host, self.request.headers['Host']).replace('www.google.com', self.request.headers['Host'])
        
    def process(self):
        self._sub_host()
        return self.body


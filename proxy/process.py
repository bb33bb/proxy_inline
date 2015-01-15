#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-15 13:03:00
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
        self.body = self.body.replace(host, self.request.headers['Host']).replace('www.google.com', self.request.headers['Host'])

    # 读取js文件，并将它添加到body中
    def _sub_js(self):
        try:
            js = cfg.get('proxy', 'js')
            js_fd = open(js, 'r')
            self.body = self.body.replace("</html>",
                    "<script>%s</script></html>" % js_fd.read())
        except:
            pass
        finally:
            js_fd.close()
        
    def process(self):
        self._sub_host()
        self._sub_js()
        return self.body


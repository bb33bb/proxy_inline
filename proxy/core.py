#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-14 14:15:32
# Filename        : proxy/core.py
# Description     : 
from tornado import web, httpclient
from tornado.web import HTTPError
from proxy.config import config
from proxy.process import Process

cfg = config()

class ProxyHandler(web.RequestHandler):
    # 接收客户端的request，并把handler修改好,返回一个HTTPRequest
    def get_request(self):
        host = cfg.get('proxy', 'host')
        port = cfg.get('proxy', 'port')
        protocol = cfg.get('proxy', 'protocol')
        uri = self.request.uri
        url = "{protocol}://{host}:{port}{uri}".format(protocol = protocol,
                host = host, port = port, uri = uri)
        headers = dict(self.request.headers)
        headers['Host'] = host
        return httpclient.HTTPRequest(
                url = url, 
                method = self.request.method,
                headers = headers,
               # body = self.request.body,
                follow_redirects = True,
                )

    def send_response(self, response):
        if response.error:
            raise HTTPError(500)
            self.finish()
            return
        self.set_status(response.code)
        for header in ('Date', 'Cache-Control', 'Server', 'Content-Type', 'Location'):
            v = response.headers.get(header)
            if v:
                self.set_header(header, v)
        self.set_header('Set-Cookie', cfg.get('proxy', 'cookies'))

        if response.body:
            # 只对html 进行内容替换
            if 'html' in self.request.headers['Accept']:
                process = Process(response.body, self.request)
                body = process.process()
            else:
                body = response.body
            self.write(body)

        self.finish()


    @web.asynchronous
    def get(self):
        request = self.get_request()
        try:
            httpclient.AsyncHTTPClient().fetch(request,
                    callback = self.send_response)
        except HTTPError, e:
            pass
    


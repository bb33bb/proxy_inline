#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-16 19:45:10
# Filename        : proxy/core.py
# Description     : 
try:
    from tornado.curl_httpclient import AsyncHTTPClient
except ImportError:
    from tornado.simple_httpclient import AsyncHTTPClient


from tornado import web, httpclient
from tornado.web import HTTPError
import os
from proxy.config import config
from proxy.mail import Mail
from proxy.process import Process

# 下面三个来将tornado从阻塞变成非阻塞的
from tornado.concurrent import run_on_executor
from tornado import gen
from concurrent.futures import ThreadPoolExecutor


cfg = config()



class ProxyHandler(web.RequestHandler):
    executor = ThreadPoolExecutor(10)

    @run_on_executor
    def _send_mail(self, mail_txt):
        mail = Mail(mail_txt)
        mail.send()


    # 当服务器发生错误的时候，发送邮箱给我的email
    @gen.coroutine
    def write_error(self, status_code, **kwargs):
        self.set_status(status_code)
        mail_txt = "错误代码:{status_code}\n请求头:\n{headers}\n异常情况:\n{exc_info}".format(
                status_code = status_code, 
                headers = '\n'.join([': '.join(item) for item in self.request.headers.items()]),
                exc_info = str(kwargs.get('exc_info', ''))
                )
        self.render('error.html', status_code = str(status_code))
        if 'Googlebot' not in self.request.headers['User-Agent']:
            self._send_mail(mail_txt)

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
        # 把cookie让用户知道
        self.set_header('Set-Cookie', cfg.get('proxy', 'cookies'))
        # 把服务器改成我的。。纯粹为了打广告
        self.set_header('Server', 'tuxpy-tornado_%s' % os.getpid())

        if response.body:
            # 只对html 进行内容替换, 通过判断response的Content-Type来决定
            if 'html' in response.headers['Content-Type']:
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
    


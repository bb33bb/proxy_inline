#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-15 12:56:07
# Filename        : proxy/mail.py
# Description     : 
from proxy.config import config
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib

cfg = config()
EMAIL_HOST = cfg.get('mail', 'host')
EMAIL_USER = cfg.get('mail', 'username')
EMAIL_PWD = cfg.get('mail', 'password')
EMAIL_ADMIN = cfg.get('mail', 'admin')

class Mail():
    def __init__(self, mail_txt):
        self._login = False
        self.mail_txt = mail_txt
        self._smtp = smtplib.SMTP()

    def login(self):
        self._smtp.connect(EMAIL_HOST)
        self._smtp.ehlo()
        self._smtp.login(EMAIL_USER, EMAIL_PWD)
        self._login = True

    def _get_msgRoot(self):
        msgRoot = MIMEMultipart()
        msgRoot['Subject'] = '急：在线代理网站出错了。。。'
        msgAttr = MIMEText(self.mail_txt)
        msgRoot.attach(msgAttr)
        msgRoot['From'] = EMAIL_USER
        msgRoot['to'] = EMAIL_ADMIN
        return msgRoot

    def send(self):
        if not self._login:
            self.login()
        msgRoot = self._get_msgRoot()
        self._smtp.sendmail(EMAIL_USER, [EMAIL_ADMIN], msgRoot.as_string())


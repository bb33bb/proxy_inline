#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-01-13 14:59:13
# Filename        : proxy/config.py
# Description     : 

import ConfigParser
import os

def config():
    cfg = ConfigParser.ConfigParser()
    for f in ['proxy.cfg', '/etc/proxy.cfg']:
        if os.path.exists(f):
            cfg.read(f)
            return cfg
    raise Exception('proxy.cfg not exists!')




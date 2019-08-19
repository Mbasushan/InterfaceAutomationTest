#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#连接数据库
import json

import pymysql

def my_db():
    conn = pymysql.Connect(
        host='192.168.1.158',
        port=3306,
        user='wikiuser',
        passwd='amoy@china4com',
        db='wikidb',
        charset='utf8'
    )
    return conn
#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import datetime
#获取时间

#获取当前时间
def now_time(strTime): #strTime  时间格式
    now_time = datetime.datetime.now()
    #转格式
    now_time=now_time.strftime(strTime)
    print(now_time)
    return now_time
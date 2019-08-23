#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as geToken
#记录大咖音频播放日志
class AudioListenLog(unittest.TestCase):

    def setUp(self):
        self.base_url="http://www.test.mbalib.com/appwiki/audiolistenlog"

    def audioListenLog(self):
        """记录大咖音频播放日志"""
        User_Agent = "MBALIB-WIKI-APP/6.7.1(iPhone 8 Plus;iOS 12.3.2;mbalibnormal;zh-cn;Build/374;)"
        headers = {"User-Agent": User_Agent}
        access_token=geToken.getToken()
        device_id='1C13DB96-1660-4BDA-A229-B69CD03D0B18'#设备号
        audio_id=64
        play_num=1
        play_time=0
        params={"access_token":access_token,"device_id":device_id,"audio_id":audio_id,"play_num":play_num,"play_time":play_time}
        response=requests.post(self.base_url,params,headers)
        result=response.json()
        print(result)
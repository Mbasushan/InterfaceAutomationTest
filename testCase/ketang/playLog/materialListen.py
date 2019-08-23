#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as getToken
import testCase.common.md5 as Md5
#用户播放日志

class MateriaListen(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/api/MaterialListenV2"

    def test_materiaListen_web(self):
        """用户播放记录-章节学习进度-web端"""
        access_token=getToken.getToken()
        ss=str(795)+str(60)+"material.less-list2sel"
        sign=Md5.my_md5(ss)
        params={"access_token":access_token,"id":795,"duration":60,"cid":"92","ctype":"column","sign":sign,"starttime":"0","endtime":"60"}
        response=requests.post(self.base_url,params=params)
        result=response.json()
        self.assertEqual(result['state'],'success')

    def test_materiaListen_app(self):
        """用户播放记录-章节学习进度-app"""
        User_Agent="MBALIB-WIKI-APP/6.7.1(iPhone 8 Plus;iOS 12.3.2;mbalibnormal;zh-cn;Build/374;)"
        headers={"User-Agent":User_Agent}
        access_token=getToken.getToken()
        ss=str(795)+str(60)+"mbalibduration"
        sign=Md5.my_md5(ss)
        params={"access_token":access_token,"id":795,"duration":60,"cid":"92","ctype":"column","sign":sign,"starttime":"0","endtime":"60"}
        response=requests.post(self.base_url,params=params,headers=headers)
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')

    def test_materiaListen_noToken(self):
        """用户播放记录-章节学习进度-未传用户信息"""
        access_token=""
        ss=str(795)+str(60)+"material.less-list2sel"
        sign=Md5.my_md5(ss)
        params={"access_token":access_token,"id":795,"duration":60,"cid":"92","ctype":"column","sign":sign,"starttime":"0","endtime":"60"}
        response=requests.post(self.base_url,params=params)
        result=response.json()
        self.assertEqual(result['errorno'],'未登陆')

    def test_materiaListen_noSign(self):
        """用户播放记录-章节学习进度-未传sign"""
        access_token = getToken.getToken()
        ss=""
        sign=Md5.my_md5(ss)
        params={"access_token":access_token,"id":795,"duration":60,"cid":"92","ctype":"column","sign":sign,"starttime":"0","endtime":"60"}
        response=requests.post(self.base_url,params=params)
        result=response.json()
        print(result)
        self.assertEqual(result['errorno'],'sign 错误')

    def test_materiaListen_noID(self):
        """用户播放记录-章节学习进度-未传章节id"""
        access_token = getToken.getToken()
        ss = str(60) + "material.less-list2sel"
        sign = Md5.my_md5(ss)
        params = {"access_token": access_token, "duration": 60, "cid": "92", "sign": sign,"starttime": "0", "endtime": "60"}
        response=requests.post(self.base_url,params=params)
        result=response.json()
        print(result)
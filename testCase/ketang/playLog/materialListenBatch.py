#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as getToken
import testCase.common.md5 as Md5
#批量提交播放日志（用于APP离线）

class MaterialListenBatch(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/api/materialListenBatch"

    def test_materialListenBatch_ios(self):
        """批量提交播放日志--ios"""
        access_token=getToken.getToken()
        User_Agent = "MBALIB-WIKI-APP/6.7.1(iPhone 8 Plus;iOS 12.3.2;mbalibnormal;zh-cn;Build/374;)"
        headers = {"User-Agent": User_Agent}
        sign1=Md5.my_md5(str(795)+str(60)+"material.less-list2sel")
        data=[]
        data.append({"id":795,"uration":60,"cid":"92","ctype":"column","sign":sign1})
        sign2=Md5.my_md5(str(795)+str(40)+"material.less-list2sel")
        data.append({"id":795,"duration":40,"cid":"92","ctype":"column","sign":sign2})
        print("data",data)
        params={"data":data,"access_token":access_token}
        response=requests.post(self.base_url,params,headers=headers)
        result=response.json()
        self.assertEqual(result['state'],'success')

    def test_materialListenBatch_ios_noToken(self):
        """批量提交播放日志--ios-未登录"""
        access_token=""
        User_Agent = "MBALIB-WIKI-APP/6.7.1(iPhone 8 Plus;iOS 12.3.2;mbalibnormal;zh-cn;Build/374;)"
        headers = {"User-Agent": User_Agent}
        sign1=str(795)+str(60)+"material.less-list2sel"
        data=[]
        data.append({"id":795,"duration":60,"cid":"92","ctype":"column","sign":sign1})
        sign2=str(795)+str(40)+"material.less-list2sel"
        data.append({"id":795,"duration":40,"cid":"92","ctype":"column","sign":sign2})
        response=requests.post(self.base_url,params={"data":data,"access_token":access_token},headers=headers)
        result=response.json()
        print(result)
        self.assertEqual(result['errorno'],'未登陆')

    def test_materialListenBatch_android(self):
        """批量提交播放日志--android"""
        access_token=getToken.getToken()
        User_Agent = "MBALIB-WIKI-APP/6.6.0(VTR-AL00; Android 9;zh-cn;Build/113;)"
        headers = {"User-Agent": User_Agent}
        sign1=str(795)+str(60)+"material.less-list2sel"
        data=[]
        data.append({"id":795,"duration":60,"cid":"92","ctype":"column","sign":sign1})
        sign2=str(795)+str(40)+"material.less-list2sel"
        data.append({"id":795,"duration":40,"cid":"92","ctype":"column","sign":sign2})
        response=requests.post(self.base_url,params={"data":data,"access_token":access_token},headers=headers)
        result=response.json()
        self.assertEqual(result['state'], 'success')

    def test_materialListenBatch_android_noToken(self):
        """批量提交播放日志--android-未登录"""
        access_token=""
        User_Agent = "MBALIB-WIKI-APP/6.6.0(VTR-AL00; Android 9;zh-cn;Build/113;)"
        headers = {"User-Agent": User_Agent}
        sign1=str(795)+str(60)+"material.less-list2sel"
        data=[]
        data.append({"id":795,"duration":60,"cid":"92","ctype":"column","sign":sign1})
        sign2=str(795)+str(40)+"material.less-list2sel"
        data.append({"id":795,"duration":40,"cid":"92","ctype":"column","sign":sign2})
        response=requests.post(self.base_url,params={"data":data,"access_token":access_token},headers=headers)
        result=response.json()
        self.assertEqual(result['errorno'], '未登陆')
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token

#充值班费
class Recharge(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/recharge"

    def test_recharge_weixin(self):
        """充值班费---微信充值"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':'1000','paytype':'weixin','amount':'1000'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')

    def test_recharge_alipay(self):
        """充值班费---支付宝充值"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':'1000','paytype':'alipay','amount':'1000'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')


    def test_recharge_alipaynew(self):
        """充值班费---支付宝(手机)充值"""
        User_Agent = "MBALIB-WIKI-APP/6.7.1(iPhone 8 Plus;iOS 12.3.2;mbalibnormal;zh-cn;Build/374;Device/7740195D-701F-4026-9A05-C05954C2AFEC;)"
        headers = {"User-Agent": User_Agent}
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':'1000','paytype':'alipaynew','amount':'1000'}
        response=requests.post(self.base_url,params,headers=headers)
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')

    def test_recharge_noToken(self):
        """充值班费---未传token"""
        params={'access_token':"",'class_id':'1000','paytype':'weixin','amount':'1000'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_recharge_noClassId(self):
        """充值班费---未传班级id"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':'','paytype':'weixin','amount':'1000'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_recharge_noPayType(self):
        """充值班费---未传支付方式"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':'1000','paytype':'','amount':'1000'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)

    def test_recharge_noAmount(self):
        """充值班费---未传金额"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':'1000','paytype':'weixin','amount':''}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_recharge_noJoinClass(self):
        """充值班费---不是该班级成员"""
        access_token=Token.get_token_login('sxs14','123456')
        params={'access_token':access_token,'class_id':'1000','paytype':'weixin','amount':''}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')
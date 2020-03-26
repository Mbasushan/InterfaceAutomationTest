#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import testCase.common.virtualPayment as virtualPayment

#充值班费
class Recharge(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/recharge"
        self.access_token = Token.get_token_login('sxs14', '123456')

    def test_recharge_weixin(self):
        """充值班费---微信充值"""
        params={'access_token':self.access_token,'class_id':'1079','paytype':'weixin','amount':'1000'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')
        order_number = result['order_number']
        # 虚拟支付
        virtualPayment.ketang_pay(self, order_number, 1000)

    def test_recharge_alipay(self):
        """充值班费---支付宝充值"""
        params={'access_token':self.access_token,'class_id':'1079','paytype':'alipay','amount':'1000'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')
        order_number = result['order_number']
        # 虚拟支付
        virtualPayment.ketang_pay(self, order_number, 1000)

    # def test_recharge_alipaynew(self):
    #     """充值班费---支付宝(手机)充值"""
    #     User_Agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36"
    #     headers = {"User-Agent": User_Agent}
    #     params={'access_token':self.access_token,'class_id':'1079','paytype':'alipaynew','amount':'1000'}
    #     response=requests.post(self.base_url,params,headers=headers)
    #     result=response.json()
    #     print(result)
    #     self.assertEqual(result['state'],'success')
    #     order_number = result['order_number']
    #     # 虚拟支付
    #     virtualPayment.ketang_pay(self, order_number, 1000)

    def test_recharge_noToken(self):
        """充值班费---未传token"""
        params={'access_token':"",'class_id':'1079','paytype':'weixin','amount':'1000'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_recharge_noClassId(self):
        """充值班费---未传班级id"""
        params={'access_token':self.access_token,'class_id':'','paytype':'weixin','amount':'1000'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_recharge_noPayType(self):
        """充值班费---未传支付方式"""
        params={'access_token':self.access_token,'class_id':'1079','paytype':'','amount':'1000'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)

    def test_recharge_noAmount(self):
        """充值班费---未传金额"""
        params={'access_token':self.access_token,'class_id':'1079','paytype':'weixin','amount':''}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_recharge_noJoinClass(self):
        """充值班费---不是该班级成员"""
        access_token=Token.get_token_login('sxs1','123456')
        params={'access_token':access_token,'class_id':'1079','paytype':'weixin','amount':''}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')
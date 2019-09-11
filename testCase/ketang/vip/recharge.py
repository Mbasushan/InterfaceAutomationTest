#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as getToken


#开通会员
class Recharge(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/vip/recharge"

    def test_getVipConfig_noType(self):
        """开通会员-未传会员类型"""
        #paytype:weixin,alipay,mb
        access_toke=getToken.getToken()
        params={"paytype":"weixin","access_token":access_toke}
        response = requests.post(self.base_url,params=params)
        result = response.json()
        self.assertEqual(result['error'],'参数错误')

    def test_getVipConfig_noPayType(self):
        """开通会员-未传支付类型"""
        #paytype:weixin,alipay,mb
        access_toke=getToken.getToken()
        params={"type":"ketang_vip_15month","access_token":access_toke}
        response = requests.post(self.base_url,params=params)
        result = response.json()
        print(result)
        self.assertEqual(result['state'],'success')
        print("未传支付类型，则默认为微信支付，所以发起开通会员成功")

    def test_getVipConfig_noAccessToke(self):
        """开通会员-未传用户令牌"""
        #paytype:weixin,alipay,mb
        params={"type":"ketang_vip_15month","payType":'weixin',"access_token":''}
        response = requests.post(self.base_url,params=params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_getVipConfig_weixin(self):
        """开通会员-微信支付"""
        #paytype:weixin,alipay,mb
        print("发起订单")
        access_toke = getToken.getToken()
        params={"type":"ketang_vip_15month","payType":'weixin',"access_token":access_toke}
        response = requests.post(self.base_url,params=params)
        result = response.json()
        print(result)
        self.assertEqual(result['state'],'success')
        # print("执行支付")
        # trade=result['order']
        # print(trade)
        # re=requests.get('http://ke.test.mbalib.com/adminorder/test?trade=338644811566287031&fee=998')
        # print(re)


    def test_getVipConfig_alipay(self):
        """开通会员-支付宝"""
        #paytype:weixin,alipay,mb
        print("发起订单")
        access_toke = getToken.getToken()
        params={"type":"ketang_vip_15month","payType":'alipay',"access_token":access_toke}
        response = requests.post(self.base_url,params=params)
        result = response.json()
        print(result)
        self.assertEqual(result['state'],'success')
        #print("执行支付")
        # trade=result['order']
        # print(trade)
        # re=requests.get('http://ke.test.mbalib.com/adminorder/test?trade=338644811566287031&fee=998')
        # print(re)

    def test_getVipConfig_mb(self):
        """开通会员-支付宝"""
        #paytype:weixin,alipay,mb
        print("发起订单")
        access_toke = getToken.getToken()
        params={"type":"ketang_vip_15month","payType":'mb',"access_token":access_toke}
        response = requests.post(self.base_url,params=params)
        result = response.json()
        print(result)
        self.assertEqual(result['state'],'success')
        #print("执行支付")
        # trade=result['order']
        # print(trade)
        # re=requests.get('http://ke.test.mbalib.com/adminorder/test?trade=338644811566287031&fee=998')
        # print(re)

def getType(self):
    response = requests.post('http://ke.test.mbalib.com/vip/config')
    result = response.json()
    self.assertEqual(result['state'], 'success')
    type=result['data']['key']
    print(type)
    return type
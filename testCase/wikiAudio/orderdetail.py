#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as getToken
import db_fixture.mysql_db as mySqlConnect

#用户大咖讲百科-订单详情
class OrderDetail(unittest.TestCase):

    def setUp(self):
        self.base_url='http://www.test.mbalib.com/appaudio/orderdetail'

    def test_orderDetail(self):
        """大咖讲百科-订单详情"""
        access_token=getToken.getToken()
        #订单号
        key='wikiaudio-361866081540870844'
        response=requests.get(self.base_url,params={'access_token':access_token,"key":key})
        result=response.json()
        print(result)
        self.assertEqual(result['data']['order_number'],key)

    def test_orderDetail_noKey(self):
        """大咖讲百科-订单详情:未传订单号"""
        access_token=getToken.getToken()
        response=requests.get(self.base_url,params={'access_token':access_token,"key":""})
        result=response.json()
        print(result)
        self.assertEqual(result['error'],"参数错误")

    def test_orderDetail_noToken(self):
        """大咖讲百科-订单详情:未传access_token"""
        key='wikiaudio-361866081540870844'
        response=requests.get(self.base_url,params={'access_token':"","key":key})
        result=response.json()
        print(result)
        self.assertEqual(result['data']['order_number'], key)
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import unittest
import requests
import testCase.common.getToken as Token

#订单列表
class GetOrderList(unittest.TestCase):

    def setUp(self):
        self.base_url='http://www.test.mbalib.com/goods/order/getOrderList'
        self.accsee_token = Token.getToken()

    def test_getOrderList(self):
        """订单列表"""
        response=requests.post(self.base_url,params={'access_token':self.accsee_token})
        result=response.json()
        print(result)

    def test_getOrderList_noToken(self):
        """订单列表--未传token"""
        response = requests.post(self.base_url, params={'access_token': ''})
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '令牌错误')
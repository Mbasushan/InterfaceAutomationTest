#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import unittest
import requests
import testCase.common.getToken as Token

#获取课堂用户订单列表
class Userorder(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/order/userorder"

    def test_userOrder(self):
        """获取课堂用户订单列表"""
        access_token=Token.getToken()
        params={'access_token':access_token,'start':0,'num':10}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        if len(result['data'])==0:
            print('无订单')
        else:
            print('有订单')

    def test_userOrder_page(self):
        """获取课堂用户订单列表---分页"""
        start = 0
        access_token=Token.getToken()
        params={'access_token':access_token,'start':start,'num':10}
        response=requests.get(self.base_url,params)
        result=response.json()
        size = len(result['data'])
        i = 0
        while len(result['data']) != 0:
            start = start + 10
            params = {'access_token': access_token, 'start': start, 'num': 10}
            response = requests.post(self.base_url, params)
            result = response.json()
            size = len(result['data']) + size
            i = i + 1
            print("第", str(i) + "页")
        print("总数:", size)
        self.assertEqual(math.ceil(size / 10), i)
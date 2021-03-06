#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import unittest
import requests
import testCase.common.getToken as Token

#获取已购的专栏
class PurchasedColumn(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/api/purchasedColumn"

    def test_purchasedColumn(self):
        """获取已购的专栏"""
        response=requests.get(self.base_url,params={'access_token':Token.getToken()})
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')

    def test_purchasedColumn_noToken(self):
        """获取已购的专栏---未登录"""
        response = requests.get(self.base_url)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')

    def test_purchasedColumn_page(self):
        """获取已购的专栏---分页"""
        start = 0
        response = requests.get(self.base_url, params={'access_token': Token.getToken(),"start":start,"num":10})
        result = response.json()
        size = len(result['data'])
        i = 0
        while len(result['data']) != 0:
            start = start + 10
            response = requests.post(self.base_url, params={'access_token': Token.getToken(),"start":start,"num":10})
            result = response.json()
            size = len(result['data']) + size
            i = i + 1
            print("第", str(i) + "页")
        print("总数:", size)
        self.assertEqual(math.ceil(size / 10), i)
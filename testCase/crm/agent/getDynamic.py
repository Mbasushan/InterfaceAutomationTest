#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math

import requests
import unittest
import testCase.common.getToken as Token

#动态列表
class GetDynamic(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/home/getDynamic'
        self.access_token=Token.getToken()

    def test_getDynamic(self):
        """动态列表"""
        page = 0
        params = {"page": 1, "size": 10,'access_token':self.access_token}
        response = requests.post(self.base_url, params=params)
        result = response.json()
        print(result)
        size = len(result['list'])
        #i = 0
        # while result['count']!= 0:
        #     page = page + 10
        #     params = {"page": page, "size": 10,'access_token':self.access_token}
        #     response = requests.post(self.base_url, params=params)
        #     result = response.json()
        #     print(result)
        #     size = len(result['list']) + size
        #     i = i + 1
        #     print("第", str(i) + "页")
        # print("总数:", size)
        # self.assertEqual(math.ceil(size / 10), i)

    def test_noToken(self):
        """动态列表-未登录"""
        params = { 'access_token': ''}
        response = requests.post(self.base_url, params=params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'令牌错误')
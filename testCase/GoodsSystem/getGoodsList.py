#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import unittest
import requests
import testCase.common.getToken as Token
import datetime


#商品列表
class GetGoodsList(unittest.TestCase):

    def setUp(self):
        self.base_url='http://www.test.mbalib.com/goods/goods/getGoodsListNew'
        self.accsee_token = Token.getToken()

    def test_getGoodsListNew(self):
        """商品列表"""
        response=requests.post(self.base_url)
        result=response.json()
        print(result)

    def test_getGoodsListNew_bean(self):
        """商品列表-仅获取可智豆购买的商品"""
        params={'bean':1}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)

    def test_getGoodsListNew_type(self):
        """商品列表-网页用参数'type'”'和'paygno'来分页"""
        pageno=0
        params={'type':'page','pageno':pageno,'num':12}
        response=requests.post(self.base_url,params)
        result=response.json()
        i = 0
        while pageno != result['lastPage']:
            pageno = pageno + 1
            params={'type':'page','pageno':pageno,'num':12}
            response = requests.post(self.base_url, params)
            result = response.json()
            print(result)
            i = i + 1
            print("第", str(i) + "页")



    def test_getGoodsListNew_star(self):
        """商品列表-app用参数'start'”'和'num'来分页"""
        start=0
        params={'num':12,'start':start}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        size = len(result['data'])
        i = 0
        while len(result['data']) != 0:
            start = start + 10
            params={'num':12,'start':start}
            response = requests.post(self.base_url, params)
            result = response.json()
            size = len(result['data']) + size
            i = i + 1
            print("第", str(i) + "页")
        print("总数:", size)
        self.assertEqual(math.ceil(size / 10), i)
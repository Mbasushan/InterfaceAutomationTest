#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math

import requests
import unittest
import testCase.common.getToken as Token
import testCase.crm.agent.base.getGoodsListBase as getGoodsListBase

#获取商品列表
class GetGoodsList(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/goods/getGoodsList'
        self.access_token=Token.getToken()

    def test_getGoodsList(self):
        """获取商品列表"""
        result = getGoodsListBase.getGoodsList(self)
        print(result)
        # if result.index('goods_id'):
        #     print('该代理商有商品')
        #     size = len(result)
        #     print(size)
        #     i = 1
        #     while len(result) != 0:
        #         start = start + 10
        #         params = {"start": start, "num": 10,'access_token':self.access_token}
        #         response = requests.post(self.base_url, params=params)
        #         result = response.json()
        #         print(result)
        #         if 'goods_id' in dir(result):
        #             size = len(result) + size
        #             i = i + 1
        #         else:
        #             size=0
        #     print("总数:", size)
        #     print("分页:", i-1)
        #     self.assertEqual(math.ceil(size / 10), i-1 )
        # else:
        #     print('该代理商无商品')

    def test_noToken(self):
        """获取商品列表-未登录"""
        params = { 'access_token': ''}
        response = requests.post(self.base_url, params=params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'令牌错误')
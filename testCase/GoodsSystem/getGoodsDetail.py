#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import unittest
import requests
import testCase.common.getToken as Token
import testCase.GoodsSystem.getGoodBase as getGoodBase

#商品详情
class GetGoodsDetail(unittest.TestCase):

    def setUp(self):
        self.base_url='http://www.test.mbalib.com/goods/goods/getGoodsDetail'
        self.access_token = Token.getToken()

    def test_getGoodsDetail(self):
        """商品详情"""
        #获取商品列表中第一个商品
        id=getGoodBase.get_goods(self)
        params={'access_token':self.access_token,'goods_id':id}
        response = requests.post(self.base_url,params)
        result = response.json()
        print(result)
        self.assertEqual(result['data']['goods_id'],id)

    def test_getGoodsDetail_noToken(self):
        """商品详情-未传token"""
        #获取商品列表中第一个商品
        id=getGoodBase.get_goods(self)
        params={'access_token':'','goods_id':id}
        response = requests.post(self.base_url,params)
        result = response.json()
        print(result)
        self.assertEqual(result['data']['goods_id'],id)

    def test_getGoodsDetail_noId(self):
        """商品详情-未传商品id"""
        params={'access_token':'','goods_id':''}
        response = requests.post(self.base_url,params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],"商品不存在")
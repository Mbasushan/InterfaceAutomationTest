#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import testCase.GoodsSystem.receive.base.getReceiveListBase as getReceiveListBase

#收货地址列表
class GetReceiveListBase(unittest.TestCase):

    def setUp(self):
        self.base_url='http://www.test.mbalib.com/goods/receive/getReceiveList'
        self.access_token = Token.getToken()

    def test_getGoodsDetail(self):
        """收货地址列表"""
        result= getReceiveListBase.get_receiveList(self)

    def test_noToken(self):
        """收货地址列表——未传token"""
        response = requests.post(self.base_url, params={'access_token': ''})
        result = response.json()
        print(result)
        self.assertEqual(result['error'],"令牌错误")
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import testCase.GoodsSystem.receive.base.getReceiveListBase as getReceiveListBase

#收货地址详情
class GetReceiveDetail(unittest.TestCase):

    def setUp(self):
        self.base_url='http://www.test.mbalib.com/goods/receive/getReceiveDetail'
        self.access_token = Token.getToken()

    def test_getGoodsDetail(self):
        """地址详情"""
        receive= getReceiveListBase.get_receiveList(self)
        if len(receive['data']['list'])!=0:
            id=receive['data']['list'][0]['receive_id']
            params={'access_token':self.access_token,'receive_id':id}
            response = requests.post(self.base_url, params)
            result = response.json()
            print(result)
            self.assertEqual(result['data']['receive_id'],id)
        else:
            print("该用户未有收获地址")

    def test_getGoodsDetail_noToken(self):
        """地址详情-未传token"""
        receive= getReceiveListBase.get_receiveList(self)
        if len(receive['data']['list'])!=0:
            id=receive['data']['list'][0]['receive_id']
            params={'access_token':'','receive_id':id}
            response = requests.post(self.base_url, params)
            result = response.json()
            print(result)
            self.assertEqual(result['error'],'令牌错误')
        else:
            print("该用户未有收获地址")

    def test_getGoodsDetail_noId(self):
        """地址详情-传0或者空值 返回默认地址"""
        params={'access_token':self.access_token,'receive_id':''}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['data']['is_default'],'0')
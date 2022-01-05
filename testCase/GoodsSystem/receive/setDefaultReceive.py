#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import testCase.GoodsSystem.receive.base.deleteReceiveBase as deleteReceiveBase
import testCase.GoodsSystem.receive.base.addReceiveBase as addReceiveBase
import testCase.GoodsSystem.receive.base.getReceiveListBase as getReceiveListBase

#修改默认收货地址
class SetDefaultReceive(unittest.TestCase):

    def setUp(self):
        self.base_url='http://www.test.mbalib.com/goods/receive/setDefaultReceive'
        self.access_token = Token.getToken()

    def test_setDefaultReceive(self):
        """修改默认收货地址"""
        # 查找收货地址列表第一个地址
        receive = getReceiveListBase.get_receiveList(self)
        receive_id = ''
        if len(receive['data']['list']) != 0:
            # 判断该收货地址是否为默认地址
            for i in range(len(receive['data']['list'])):
                is_default = receive['data']['list'][i]['is_default']
                receive_id=receive['data']['list'][i]['receive_id']
                if is_default==0:
                    break
        else:
            #未查到收货地址，新增收货地址
            receive_id = addReceiveBase.addReceive(self)
        params = {'access_token': self.access_token, 'receive_id': receive_id}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)

    def test_setDefaultReceive_noToken(self):
        """修改默认收货地址-未传token"""
        # 查找收货地址列表第一个地址
        receive = getReceiveListBase.get_receiveList(self)
        receive_id = ''
        if len(receive['data']['list']) != 0:
            # 判断该收货地址是否为默认地址
            for i in range(len(receive['data']['list'])):
                is_default = receive['data']['list'][i]['is_default']
                receive_id=receive['data']['list'][i]['receive_id']
                if is_default==0:
                    break
        else:
            #未查到收货地址，新增收货地址
            receive_id = addReceiveBase.addReceive(self)
        params = {'access_token': '', 'receive_id': receive_id}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'令牌错误')

    def test_setDefaultReceive_noId(self):
        """修改默认收货地址-未传id,地址不是必填，未填写就是没有默认收货地址"""
        # 查找收货地址列表第一个地址
        receive = getReceiveListBase.get_receiveList(self)
        receive_id = ''
        if len(receive['data']['list']) != 0:
            # 判断该收货地址是否为默认地址
            for i in range(len(receive['data']['list'])):
                is_default = receive['data']['list'][i]['is_default']
                receive_id=receive['data']['list'][i]['receive_id']
                if is_default==0:
                    break
        else:
            #未查到收货地址，新增收货地址
            receive_id = addReceiveBase.addReceive(self)
        params = {'access_token': self.access_token, 'receive_id': ''}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
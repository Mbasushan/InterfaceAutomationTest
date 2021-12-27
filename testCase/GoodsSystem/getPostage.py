#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import testCase.GoodsSystem.receive.base.getReceiveListBase as getReceiveListBase
from testCase.GoodsSystem.receive.base import addReceiveBase
import testCase.GoodsSystem.getGoodBase as getGoodBase

#获取邮费
class GetPostage(unittest.TestCase):

    def setUp(self):
        self.base_url='http://www.test.mbalib.com/goods/order/getPostage'

    def test_getPostage(self):
        """获取邮费"""
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
        # 获取商品列表中第一个商品
        goodsId = getGoodBase.get_goods(self)
        params = {'goods_id': goodsId, 'receive_id': receive_id}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        print("该地址邮为：",result['postage'])

    def test_getPostage_noRId(self):
        """获取邮费-未传receivedId"""
        # 获取商品列表中第一个商品
        goodsId = getGoodBase.get_goods(self)
        params = {'goods_id': goodsId, 'receive_id': ''}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_getPostage_nogId(self):
        """获取邮费-未传goodsId"""
        # 查找收货地址列表第一个地址
        receive = getReceiveListBase.get_receiveList(self)
        receive_id = ''
        if len(receive['data']['list']) != 0:
            # 判断该收货地址是否为默认地址
            for i in range(len(receive['data']['list'])):
                is_default = receive['data']['list'][i]['is_default']
                receive_id = receive['data']['list'][i]['receive_id']
                if is_default == 0:
                    break
        else:
            # 未查到收货地址，新增收货地址
            receive_id = addReceiveBase.addReceive(self)
        # 获取商品列表中第一个商品
        #goodsId = getGoodBase.get_goods(self)
        params = {'goods_id': '', 'receive_id': receive_id}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')
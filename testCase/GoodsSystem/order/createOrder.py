#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import unittest
import requests
import testCase.common.getToken as Token
import testCase.GoodsSystem.getGoodBase as getGoodBase
import testCase.GoodsSystem.goodsPackage as goodsPackage
import testCase.GoodsSystem.receive.base.getReceiveListBase as getReceiveListBase

#创建订单
class CreateOrder(unittest.TestCase):

    def setUp(self):
        self.base_url='http://www.test.mbalib.com/goods/order/createOrder'
        self.accsee_token = Token.getToken()

    def test_createOrder(self):
        """创建订单"""
        #获取商品
        goodId=getGoodBase.get_goods(self)
        #该套餐详情
        gps=goodsPackage.get_gp(self)
        gp_id=gps[0]['gp_id']
        #收货地址
        relist=getReceiveListBase.get_receiveList(self)
        receive_id=relist['data']['list'][0]['receive_id']
        params={'access_token':self.accsee_token,'goods_id':goodId,'num':1,'pay_type':'weixin','receive_id':receive_id,'gp_id':gp_id}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)


    def test_createOrder_noToken(self):
        """创建订单-未传token"""
        #获取商品
        goodId=getGoodBase.get_goods(self)
        #该套餐详情
        gps=goodsPackage.get_gp(self)
        gp_id=gps[0]['gp_id']
        #收货地址
        relist=getReceiveListBase.get_receiveList(self)
        receive_id=relist['data']['list'][0]['receive_id']
        params={'access_token':'','goods_id':goodId,'num':1,'pay_type':'weixin','receive_id':receive_id,'gp_id':gp_id}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'令牌错误')

    def test_createOrder_nogId(self):
        """创建订单-未传商品id"""
        #获取商品
        goodId=getGoodBase.get_goods(self)
        #该套餐详情
        gps=goodsPackage.get_gp(self)
        gp_id=gps[0]['gp_id']
        #收货地址
        relist=getReceiveListBase.get_receiveList(self)
        receive_id=relist['data']['list'][0]['receive_id']
        params={'access_token':self.accsee_token,'goods_id':'','num':1,'pay_type':'weixin','receive_id':receive_id,'gp_id':gp_id}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'商品不存在')

    def test_createOrder_noGpID(self):
        """创建订单-未传套餐id"""
        #获取商品
        goodId=getGoodBase.get_goods(self)
        #该套餐详情
        gps=goodsPackage.get_gp(self)
        gp_id=gps[0]['gp_id']
        #收货地址
        relist=getReceiveListBase.get_receiveList(self)
        receive_id=relist['data']['list'][0]['receive_id']
        params={'access_token':self.accsee_token,'goods_id':goodId,'num':1,'pay_type':'weixin','receive_id':receive_id,'gp_id':''}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'请先选择套餐')

    def test_createOrder_noReceive_id(self):
        """创建订单-未传收货地址"""
        #获取商品
        goodId=getGoodBase.get_goods(self)
        #该套餐详情
        gps=goodsPackage.get_gp(self)
        gp_id=gps[0]['gp_id']
        #收货地址
        relist=getReceiveListBase.get_receiveList(self)
        receive_id=relist['data']['list'][0]['receive_id']
        params={'access_token':self.accsee_token,'goods_id':goodId,'num':1,'pay_type':'weixin','receive_id':'','gp_id':gp_id}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'收件地址不可为空')
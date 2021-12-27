#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import unittest
import requests
import testCase.common.getToken as Token
import datetime

#订单收货
class ReceiveOrder(unittest.TestCase):

    def setUp(self):
        self.base_url='http://www.test.mbalib.com/goods/order/receiveOrder'
        self.accsee_token = Token.getToken()


    def test_receiveOrder(self):
        """订单收货"""
        #查找订单列表
        response=requests.post(url='http://www.test.mbalib.com/goods/order/getOrderList',params={'access_token':self.accsee_token})
        olist=response.json()
        print(olist)
        if len(olist['data']['list'])!=0:
            for i in range(len(olist)):
                #判断是否为待收货订单
                if olist['data']['list'][i]['info2']=='待收货':
                    result=requests.post(self.base_url,params={'access_token':self.accsee_token,'goods_order_id':olist['data']['list'][i]['goods_order_id']})
                    rjson=result.json()
                    print(rjson)
                    print("确认收货成功")
                    break
                else:
                    print("订单状态不是待收货")
        else:
            print("该用户未有订单")

    def test_receiveOrder_noToken(self):
        """订单收货-未传token"""
        # 查找订单列表
        response = requests.post(url='http://www.test.mbalib.com/goods/order/getOrderList',params={'access_token': self.accsee_token})
        olist = response.json()
        print(olist)
        if len(olist['data']['list']) != 0:
            for i in range(len(olist)):
                # 判断是否为待收货订单
                if olist['data']['list'][i]['info2'] == '待收货':
                    result = requests.post(self.base_url, params={'access_token': self.accsee_token,'goods_order_id': olist['data']['list'][i]['goods_order_id']})
                    rjson = result.json()
                    print(rjson)
                    print("确认收货成功")
                    break
                else:
                    print("订单状态不是待收货")
        else:
            print("该用户未有订单")


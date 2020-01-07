#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import unittest
import requests
import testCase.common.getToken as Token
import testCase.ketang.order.base.userOrderBase as userOrderBase

#课堂订单详情
class OrderDetail(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/order/orderdetail"
        self.access_token=Token.get_token_login('sxs14','123456')

    def test_order_detail(self):
        """课堂订单详情"""
        #获取课堂订单
        orderNum=userOrderBase.userOrderList('sxs14')
        if orderNum!=None:
            params={'access_token':self.access_token,'key':orderNum}
            response=requests.get(self.base_url,params)
            result=response.json()
            print(result)
            self.assertEqual(result['data']['order_number'],orderNum)
        else:
            print("无订单")

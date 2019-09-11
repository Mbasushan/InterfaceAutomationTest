#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as getToken

#开通会员
class VirtualPayment(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/adminorder/test"

    #虚拟支付
    def test_virtualPaymentKetang(self):   #trade 订单号  fee  金额
        trade='408184201566894069'
        params={'trade':trade,'fee':998}
        response = requests.post(self.base_url, params)
        print(response)
        print("虚拟支付")
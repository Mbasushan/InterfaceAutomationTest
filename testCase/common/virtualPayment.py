#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import testCase.common.getToken as Token

#课堂虚拟支付
def ketang_pay(self,trade,fee):   #trade 订单号  fee  金额
    url='http://ke.test.mbalib.com/order/test'
    params={'trade':trade,'fee':fee}
    response = requests.post(url,params)
    self.assertEqual(response.text, 'success~~~~')

#大咖虚拟支付
def audio_pay(self,trade,fee):
    url='http://passport.test.mbalib.com/api/ttt'
    params={'t':trade,'f':fee}
    response=requests.post(url,params)
    self.assertEqual(response.text, 'success')
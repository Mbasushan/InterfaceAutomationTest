#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token
import testCase.crm.order.base.getOrderList as getOrderList

#订单详情
class Detail(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/order/getDetail'
        self.access_token=Token.getToken()

    def test_getDetail(self):
        """订单详情"""
        list=getOrderList.get_order_list(self,self.access_token)
        if list==None:
            print("无订单")
        else:
            i=0
            for i in range(len(list)):
                id=list[i]['id']
                params={'access_token':self.access_token,'id':id}
                response=requests.post(self.base_url,params)
                result=response.json()
                print(result)

    def test_getDetail_noToken(self):
        """订单详情-未传token"""
        list = getOrderList.get_order_list(self, self.access_token)
        if list == None:
            print("无订单")
        else:
            i = 0
            for i in range(len(list)):
                id = list[i]['id']
                params = {'access_token':'', 'id': id}
                response = requests.post(self.base_url, params)
                result = response.json()
                print(result)

    def test_getDetail_noId(self):
        """订单详情-未传id"""
        params = {'access_token': self.access_token, 'id': ''}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')
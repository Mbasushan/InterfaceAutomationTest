#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import unittest
import requests
import testCase.common.getToken as getToken

#大咖订单列表
class WikiOrderList(unittest.TestCase):

    def setUp(self):
        self.base_url='http://www.test.mbalib.com/app/orderlist'

    def test_getWikiOrderLisst(self):
        """大咖订单列表"""
        access_token=getToken.getToken()
        type='wiki'
        params={"access_token":access_token,"type":type}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        print(len(result['data']))
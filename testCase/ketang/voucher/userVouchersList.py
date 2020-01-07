#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token

#优惠券列表
class UserVouchersList(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/api/userVouchersList"
        self.access_token=Token.get_token_login('sxs14','123456')

    def test_userVoucherList(self):
        """优惠券列表"""
        response=requests.get(self.base_url,params={'access_token':self.access_token})
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')
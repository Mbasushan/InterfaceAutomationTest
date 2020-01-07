#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token

#获取用户优惠劵列表
class GetUserVoucher(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/voucher/GetUserVoucher"

    def test_getUserVoucher(self):
        """获取用户优惠券列表"""
        access_token=Token.get_token_login('sxs14','123456')
        response=requests.get(self.base_url,params={'access_token':access_token})
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']),0)

    def test_getUserVoucher_noToken(self):
        """获取用户优惠券列表---未登录"""
        access_token=''
        response=requests.get(self.base_url,params={'access_token':access_token})
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token

#获取用户信息
class GetUserInfo(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/user/getUserInfo'
        self.access_token=Token.getToken()

    def test_getUserInfo(self):
        """获取用户信息"""
        respose=requests.post(self.base_url,params={'access_token':self.access_token})
        result=respose.json()
        print(result)

    def test_getUserInfo_noToken(self):
        """获取用户信息-未传token"""
        respose=requests.post(self.base_url,params={'access_token':''})
        result=respose.json()
        print(result)
        self.assertEqual(result['error'],'令牌错误')
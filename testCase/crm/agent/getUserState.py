#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token

#代理商：获取用户状态
class GetUserState(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/agent/getUserState'
        self.access_token=Token.get_token_login('sxs14','123456')

    def test_getUserState(self):
        """代理商：获取用户状态"""
        response=requests.post(self.base_url,params={'access_token':self.access_token})
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['state']),0)

    def test_getUserState_noParams(self):
        """代理商：获取用户状态"""
        response=requests.post(self.base_url)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'令牌错误')
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token

#获取登录用户所属代理商信息
class GetUserAgent(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/agent/getUserAgent'

    def test_getUserAgent_noRegister(self):
        """获取登录用户所属代理商信息-未注册代理商"""
        response=requests.post(self.base_url,params={'access_token':Token.get_token_login('sxs14','123456')})
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'未加入代理商')

    def test_getUserAgent(self):
        """获取登录用户所属代理商信息-已注册代理商"""
        response=requests.post(self.base_url,params={'access_token':Token.getToken()})
        result=response.json()
        print(result)
        self.assertNotEqual(len(result),0)

    def test_getUserAgent_noToken(self):
        """获取登录用户所属代理商信息-未登录"""
        response=requests.post(self.base_url)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'令牌错误')
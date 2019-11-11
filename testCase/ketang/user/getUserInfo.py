#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token

#用户信息
class GetUserInfo(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/api/GetUserInfo"

    def test_getUserInfo(self):
        """用户信息"""
        response=requests.post(self.base_url,params={'access_token':Token.getToken()})
        result=response.json()
        print(result)
        self.assertEqual(result['status'],'success')

    def test_getUserInfo_noToken(self):
        """用户信息---未登录"""
        response = requests.post(self.base_url)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')
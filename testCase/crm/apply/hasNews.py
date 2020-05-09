#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token

#是否有新消息
class HasNews(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/apply/hasNews'
        self.access_token=Token.getToken()

    def test_hasNews(self):
        """是否有新消息"""
        response=requests.post(self.base_url,params={'access_token':self.access_token})
        result=response.json()
        print(result)
        if result['has_news']==0:
            print('无新消息')
        else:
            print('有新消息')


    def test_hasNews_noToken(self):
        """是否有新消息-未传token"""
        response=requests.post(self.base_url,params={'access_token':''})
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'令牌错误')
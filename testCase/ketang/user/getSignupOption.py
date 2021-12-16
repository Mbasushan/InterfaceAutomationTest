#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import unittest
import requests
import testCase.common.getToken as Token
import db_fixture.mysql_db as mySqlConnect

#获取报名完成后需要填写的资料
class GetSignupOption(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/api/getSignupOption"
        self.accsee_token=Token.getToken()

    def test_getSignupOption(self):
        """获取报名完成后需要填写的资料"""
        params = {'access_token': self.accsee_token,'item_id':89,'item_type':'column'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)

    def test_getSignupOption_noToken(self):
        """获取报名完成后需要填写的资料-未传token"""
        params = {'item_id':89,'item_type':'column'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_getSignupOption_noId(self):
        """获取报名完成后需要填写的资料-未传课程id"""
        params = {'access_token': self.accsee_token,'item_type':'column'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(len(result['data']['fill']),0)

    def test_getSignupOption_noType(self):
        """获取报名完成后需要填写的资料-未传课程类型"""
        params = {'access_token': self.accsee_token, 'item_id': 89}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)



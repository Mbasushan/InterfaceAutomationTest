#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token


#获取我的班级列表
class GetClassList(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/class/getClassList'

    def test_getClassList(self):
        """获取我的班级列表"""
        access_token=Token.getToken()
        response=requests.get(self.base_url,params={'access_token':access_token})
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']),0)

    def test_getClassList_noToken(self):
        """获取我的班级列表---未登录"""
        response=requests.get(self.base_url)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token


#个人学习明细-章节明细
class Getusermaterial(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/getusermaterial"
        self.access_token=Token.get_token_login('sxs14','123456')

    def test_getusermaterial(self):
        """个人学习明细-章节明细-单课"""
        params={'access_token':self.access_token,'class_id':1079,'user_id':'20314','itemtype':'course','itemid':8526372}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertNotEqual(len(result), 0)

    def test_getusermaterial_column(self):
        """个人学习明细-章节明细-专栏"""
        params={'access_token':self.access_token,'class_id':1079,'user_id':'20314','itemtype':'column','itemid':258}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertNotEqual(len(result), 0)

    def test_getusermaterial_noToken(self):
        """个人学习明细-章节明细-未登录"""
        params={'access_token':'','class_id':1079,'user_id':'20314','itemtype':'course','itemid':8526372}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')

    def test_getusermaterial_noClassId(self):
        """个人学习明细-章节明细-未传班级key"""
        params={'access_token':self.access_token,'class_id':'','user_id':'20314','itemtype':'course','itemid':8526372}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_getusermaterial_noUId(self):
        """个人学习明细-作业明细-未传用户ID"""
        params={'access_token':self.access_token,'class_id':'1079','user_id':'','itemtype':'course','itemid':8526372}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_getusermaterial_noItype(self):
        """个人学习明细-章节明细-未传课程类型"""
        params={'access_token':self.access_token,'class_id':'1079','user_id':'20314','itemtype':'','itemid':8526372}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_getusermaterial_noItemId(self):
        """个人学习明细-章节明细-未传课程id"""
        params={'access_token':self.access_token,'class_id':'1079','user_id':'20314','itemtype':'course','itemid':''}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')
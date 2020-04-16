#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token


#选择题报表详情
class Reporttasksingledetail(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/reporttasksingledetail"
        self.access_token=Token.get_token_login('sxs14','123456')

    def test_reporttasksingledetail(self):
        """选择题报表详情"""
        params={'access_token':self.access_token,'class_id':1079,'question_id':237}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertNotEqual(len(result), 0)

    def test_reporttasksingledetail_noToken(self):
        """选择题报表详情-未登录"""
        params={'access_token':'','class_id':1079,'question_id':237}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')

    def test_reporttasksingledetail_noClassId(self):
        """选择题报表详情-未传班级key"""
        params={'access_token':self.access_token,'class_id':'','question_id':237}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_reporttasksingledetail_noqId(self):
        """选择题报表详情-未传选择题id"""
        params={'access_token':self.access_token,'class_id':1079,'question_id':''}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')
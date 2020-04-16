#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token


#选择题报表单课信息
class ReportTaskSingleSummary(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/ReportTaskSingleSummary"
        self.access_token=Token.get_token_login('sxs14','123456')

    def test_reportTaskSingleSummary(self):
        """选择题报表单课信息"""
        params={'access_token':self.access_token,'class_id':1079,'itemtype':'course','itemid':8526372}
        response=requests.post(self.base_url,params)
        result = response.json()
        print(result)
        self.assertNotEqual(len(result), 0)

    def test_reportTaskSingleSummary_column(self):
        """选择题报表单课信息-专栏"""
        params = {'access_token': self.access_token, 'class_id': 1079, 'itemtype': 'column', 'itemid': 258}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertNotEqual(len(result), 0)

    def test_reportTaskSingleSummary_noToken(self):
        """选择题报表单课信息-未登录"""
        params={'access_token':'','class_id':1079,'itemtype':'course','itemid':8526372}
        response=requests.post(self.base_url,params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')

    def test_reportTaskSingleSummary_noClassId(self):
        """选择题报表单课信息-未传班级id"""
        params={'access_token':self.access_token,'class_id':'','itemtype':'course','itemid':8526372}
        response=requests.post(self.base_url,params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_reportTaskSingleSummary_noItemtype(self):
        """选择题报表单课信息-未传课程类型"""
        params={'access_token':self.access_token,'class_id':1079,'itemtype':'','itemid':8526372}
        response=requests.post(self.base_url,params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_reportTaskSingleSummary_noItemid(self):
        """选择题报表单课信息-未传课程id"""
        params={'access_token':self.access_token,'class_id':1079,'itemtype':'course','itemid':''}
        response=requests.post(self.base_url,params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')
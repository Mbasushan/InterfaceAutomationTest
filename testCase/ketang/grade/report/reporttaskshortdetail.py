#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token


#简答题报表详情
class Reporttaskshortdetail(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/reporttaskshortdetail"
        self.access_token=Token.get_token_login('sxs14','123456')

    def test_reporttaskshortdetail(self):
        """简答题报表详情"""
        params={'access_token':self.access_token,'class_id':1079,'question_id':222}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertNotEqual(len(result), 0)

    def test_reporttaskshortdetail_noToken(self):
        """简答题报表详情"-未登录"""
        params={'access_token':'','class_id':1079,'question_id':222}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertNotEqual(len(result), 0)

    def test_reporttaskshortdetail_noClassId(self):
        """选择题报表详情-未传班级key，就是课程介绍页的作业精选"""
        params={'access_token':self.access_token,'class_id':'','question_id':222}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertNotEqual(len(result), 0)

    def test_reporttaskshortdetail_noqId(self):
        """选择题报表详情-未传选择题id"""
        params={'access_token':self.access_token,'class_id':1079,'question_id':''}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')
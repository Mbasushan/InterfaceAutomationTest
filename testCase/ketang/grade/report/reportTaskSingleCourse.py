#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token


#选择题报表单课题目信息
class ReportTaskSingleCourse(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/ReportTaskSingleCourse"
        self.access_token=Token.get_token_login('sxs14','123456')

    def test_reportTaskSingleCourse(self):
        """选择题报表单课题目信息"""
        params={'access_token':self.access_token,'class_id':1079,'course_id':8526372}
        response=requests.post(self.base_url,params)
        result = response.json()
        print(result)
        self.assertNotEqual(len(result), 0)

    def test_reportTaskSingleCourse_column(self):
        """选择题报表单课题目信息-专栏底下的单课"""
        params={'access_token':self.access_token,'class_id':1079,'course_id':8521220}
        response=requests.post(self.base_url,params)
        result = response.json()
        print(result)
        self.assertNotEqual(len(result), 0)

    def test_reportTaskSingleCourse_noToken(self):
        """选择题报表单课题目信息-未登录"""
        params={'access_token':'','class_id':1079,'course_id':8526372}
        response=requests.post(self.base_url,params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')

    def test_reportTaskSingleCourse_noClassId(self):
        """选择题报表单课题目信息-未传班级Id"""
        params={'access_token':self.access_token,'class_id':'','course_id':8526372}
        response=requests.post(self.base_url,params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_reportTaskSingleCourse_noCouserId(self):
        """选择题报表单课题目信息-未传班级Id"""
        params={'access_token':self.access_token,'class_id':1079,'course_id':''}
        response=requests.post(self.base_url,params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')
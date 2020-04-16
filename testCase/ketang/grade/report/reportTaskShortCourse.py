#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token


#简答题报表单课题目信息，专栏内的每个课程都要去单独请求这个接口
class ReportTaskShortCourse(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/ReportTaskShortCourse"
        self.access_token=Token.get_token_login('sxs14','123456')

    def test_reportTaskShortCourse(self):
        """简答题报表单课题目信息"""
        params={'access_token':self.access_token,'class_id':1079,'course_id':8526372}
        response=requests.post(self.base_url,params)
        result = response.json()
        print(result)
        self.assertNotEqual(len(result), 0)

    def test_reportTaskShortCourse_noToken(self):
        """简答题报表单课题目信息-未登录"""
        params={'access_token':'','class_id':1079,'course_id':8526372}
        response=requests.post(self.base_url,params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')

    def test_reportTaskShortCourse_noClassId(self):
        """简答题报表单课题目信息-未传班级key"""
        params={'access_token':self.access_token,'class_id':'','course_id':8526372}
        response=requests.post(self.base_url,params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_reportTaskShortCourse_noCourseId(self):
        """简答题报表单课题目信息-未传课程Id"""
        params={'access_token':self.access_token,'class_id':'1079','course_id':''}
        response=requests.post(self.base_url,params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')
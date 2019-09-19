#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token

#课程成员清单
class ReportGetCourseMember(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/class/reportGetCourseMember'

    def test_reportGetCourseMember_column(self):
        """专栏成员清单"""
        params={'class_id':1000,'itemid':258,'itemtype':'column'}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)

    def test_reportGetCourseMember_course(self):
        """课程成员清单"""
        params={'class_id':1000,'itemid':8526372,'itemtype':'course'}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)

    def test_reportGetCourseMember_noClassId(self):
        """课程成员清单---未传班级ID"""
        params = {'itemid': 258, 'itemtype': 'column'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'没有找到班级')

    def test_reportGetCourseMember_noItemid(self):
        """课程成员清单---未传课程id"""
        params = {'class_id': 1000, 'itemtype': 'column'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(len(result['data']['list']),0)

    def test_reportGetCourseMember_noItemType(self):
        """课程成员清单---未传课程类型"""
        params = {'class_id': 1000, 'itemid': 258}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(len(result['data']['list']),0)
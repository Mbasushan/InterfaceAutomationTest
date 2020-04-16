#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token


#章节报表单课信息
class ReportCourseMaterials(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/ReportCourseMaterials"
        self.access_token=Token.get_token_login('sxs14','123456')

    def test_reportCourseMaterials_course(self):
        """章节报表单课信息-单课"""
        params={'class_id':'1079','itemtype':'course','itemid':'8520014','access_token':self.access_token}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result),0)

    def test_reportCourseMaterials_column(self):
        """章节报表单课信息(章节概况)"""
        params={'class_id':'1079','itemtype':'column','itemid':'12','access_token':self.access_token}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result),0)

    def test_reportCourseMaterials_noToken(self):
        """章节报表单课信息-单课-未登录"""
        params = {'class_id': '1079', 'itemtype': 'course', 'itemid': '8520014', 'access_token':''}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')

    def test_reportCourseMaterials_noitemtype(self):
        """章节报表单课信息-未传type类型"""
        params = {'class_id': '1079', 'itemtype': '', 'itemid': '8520014', 'access_token':self.access_token}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(len(result['data']), 0)

    def test_reportCourseMaterials_noclassId(self):
        """章节报表单课信息-未传classid类型"""
        params = {'class_id': '', 'itemtype': 'course', 'itemid': '8520014', 'access_token':self.access_token}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_reportCourseMaterials_noitemid(self):
        """章节报表单课信息-未传classid类型"""
        params = {'class_id': '1079', 'itemtype': 'course', 'itemid': '', 'access_token':self.access_token}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(len(result['data']), 0)
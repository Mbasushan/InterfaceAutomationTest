#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token


#章节报表单课章节详情
class ReportMaterials(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/ReportMaterials"
        self.access_token=Token.get_token_login('sxs14','123456')

    def test_reportMaterials_course(self):
        """章节报表单课章节详情"-课程为单课"""
        params={'class_id':'1079','itemid':'8520014','signup_itemtype':'course','signup_itemid':'8520014','access_token':self.access_token}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result), 0)

    def test_reportMaterials_column(self):
        """章节报表单课章节详情-课程为专栏"""
        params = {'class_id': '1079', 'itemid': '8569527', 'signup_itemtype': 'column', 'signup_itemid': '12',
                  'access_token': self.access_token}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertNotEqual(len(result), 0)

    def test_reportMaterials_noToken(self):
        """章节报表单课章节详情"-未登录"""
        params={'class_id':'1079','itemid':'8520014','signup_itemtype':'course','signup_itemid':'8520014','access_token':''}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')

    def test_reportMaterials_noClassId(self):
        """章节报表单课章节详情"-未传班级id"""
        params={'class_id':'','itemid':'8520014','signup_itemtype':'course','signup_itemid':'8520014','access_token':self.access_token}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_reportMaterials_noitemid(self):
        """章节报表单课章节详情"-未传单课id"""
        params={'class_id':'1079','itemid':'','signup_itemtype':'course','signup_itemid':'8520014','access_token':self.access_token}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_reportMaterials_noSignup_itemtype(self):
        """章节报表单课章节详情"-未传报名的课程类型"""
        params={'class_id':'1079','itemid':'8520014','signup_itemtype':'','signup_itemid':'8520014','access_token':self.access_token}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_reportMaterials_noSignup_itemid(self):
        """章节报表单课章节详情"-未传报名的课程id"""
        params={'class_id':'1079','itemid':'8520014','signup_itemtype':'course','signup_itemid':'','access_token':self.access_token}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')
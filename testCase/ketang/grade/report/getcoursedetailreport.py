#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token


#课程报表明细概况
class Getcoursedetailreport(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/getcoursedetailreport"
        self.access_token=Token.get_token_login('sxs14','123456')

    def test_getcoursedetailreport(self):
        """课程报表明细概况-单课"""
        params={'class_id':'1079','item_id':'8520014','type':'course','access_token':self.access_token}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result), 0)

    def test_getcoursedetailreport_column(self):
        """课程报表明细概况-专栏"""
        params={'class_id':'1079','item_id':'12','type':'column','access_token':self.access_token}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result), 0)

    def test_getcoursedetailreport_noToken(self):
        """课程报表明细概况-未登录"""
        params={'class_id':'1079','item_id':'8520014','type':'course','access_token':''}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_getcoursedetailreport_noClassId(self):
        """课程报表明细概况-未传班级id"""
        params={'class_id':'','item_id':'12','type':'column','access_token':self.access_token}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '没有找到班级')


    def test_getcoursedetailreport_noItemId(self):
        """课程报表明细概况-未传课程Id"""
        params={'class_id':'1079','item_id':'','type':'column','access_token':self.access_token}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_getcoursedetailreport_noType(self):
        """课程报表明细概况-未传课程类型"""
        params = {'class_id': '1079', 'item_id': '12', 'type': '', 'access_token': self.access_token}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token


#章节成员信息
class ReportMaterialMember(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/ReportMaterialMember"
        self.access_token=Token.get_token_login('sxs14','123456')

    def test_reportMaterialMember(self):
        """章节成员信息-单课"""
        params={'access_token':self.access_token,'class_id':1079,'material_id':887}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result),0)

    def test_reportMaterialMember_column(self):
        """章节成员信息-专栏章节"""
        params={'access_token':self.access_token,'class_id':1079,'material_id':896}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result),0)

    def test_reportMaterialMember_complete(self):
        """章节成员信息-筛选已完成"""
        params = {'access_token': self.access_token, 'class_id': 1079, 'material_id': 896,'complete':1}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertNotEqual(len(result), 0)

    def test_reportMaterialMember_Nocomplete(self):
        """章节成员信息-筛选未完成"""
        params = {'access_token': self.access_token, 'class_id': 1079, 'material_id': 896,'complete':0}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertNotEqual(len(result), 0)

    def test_reportMaterialMember_noToken(self):
        """章节成员信息-筛选未登录"""
        params = {'access_token':'', 'class_id': 1079, 'material_id': 896,'complete':1}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')

    def test_reportMaterialMember_noClassId(self):
        """章节成员信息-未传班级id"""
        params = {'access_token': self.access_token, 'class_id':'', 'material_id': 896,'complete':1}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_reportMaterialMember_noMaterial_id(self):
        """章节成员信息-未传章节id"""
        params = {'access_token': self.access_token, 'class_id':1079, 'material_id': '','complete':1}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')


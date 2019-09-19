#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token


#获取班级报表信息
class GetReport(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/getReport"

    def test_getReport(self):
        """获取班级报表信息"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':1000}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']),0)

    def test_getReport_admin(self):
        """获取班级报表信息---管理员获取"""
        access_token=Token.get_token_login('冰辰羽','123456')
        params={'access_token':access_token,'class_id':1000}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']),0)

    def test_getReport_normal(self):
        """获取班级报表信息---普通成员获取"""
        access_token=Token.get_token_login('苏珊15','123456')
        params={'access_token':access_token,'class_id':1000}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '您没有权限进行操作')

    def test_getReport_noToken(self):
        """获取班级报表信息---未传token"""
        params={'access_token':"",'class_id':1000}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_getReport_noClassId(self):
        """获取班级报表信息---未传classId"""
        access_token=Token.getToken()
        params={'access_token':access_token}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'没有找到班级')
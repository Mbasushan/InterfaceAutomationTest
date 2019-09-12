#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token


#获取班级用户报表
class GetUserReport(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/getUserReport"

    def test_getUserReport(self):
        """获取班级用户报表"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':1000,'member_id':162}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']['member_info']),0)

    def test_getUserReport_noToken(self):
        """获取班级用户报表---未传token"""
        params={'access_token':"",'class_id':1000,'member_id':162}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_getUserReport_noClassId(self):
        """获取班级用户报表---未传classId"""
        access_token=Token.getToken()
        params={'access_token':access_token,'member_id':162}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '操作失败')

    def test_getUserReport_noMemberId(self):
        """获取班级用户报表---未传班级成员ID"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':1000}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '操作失败')

    def test_getUserReport_MemberId(self):
        """获取班级用户报表---班级成员ID值不属于该班级"""
        access_token = Token.getToken()
        params = {'access_token': access_token, 'class_id': 1000,'member_id':20035}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '找不到成员信息')

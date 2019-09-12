#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token


#系统班报表
class GetUserReport(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/getPackageReport"

    def test_getPackageReport(self):
        """获取系统班报表"""
        access_token = Token.getToken()
        params = {'access_token': access_token, 'class_id': 1000, 'package_id': 1014}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertNotEqual(len(result['data']), 0)

    def test_getPackageReport_noToken(self):
        """获取系统班报表---未传token"""
        params = {'access_token': "", 'class_id': 1000, 'package_id': 1014}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')

    def test_getPackageReport_noClassId(self):
        """获取系统班报表---未传classId"""
        access_token = Token.getToken()
        params = {'access_token': access_token, 'package_id': 1014}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '没有找到班级')


    def test_getPackageReport_noPackageId(self):
        """获取系统班报表---未传package_id"""
        access_token = Token.getToken()
        params = {'access_token': access_token, 'class_id': 1000}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '没有找到班级')


    def test_getPackageReport_errorPackageId(self):
        """获取系统班报表---packageId的值不在该班级"""
        access_token = Token.getToken()
        params = {'access_token': access_token, 'class_id': 1000, 'package_id': 1019}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertNotEqual(len(result['data']), 0)
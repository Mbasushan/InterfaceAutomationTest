#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import unittest
import requests
import testCase.common.getToken as Token

#课程包信息
class PackageDetail(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/api/getpackagedetail'

    def test_packageDetail(self):
        """获取课程包信息"""
        access_token=Token.getToken()
        response=requests.post(self.base_url,params={'id':1002,'access_token':access_token})
        result=response.json()
        self.assertEqual(result['state'],'success')

    def test_packageDetail_noToken(self):
        """获取课程包信息---未登录"""
        response = requests.post(self.base_url, params={'id': 1002})
        result = response.json()
        print(result)
        self.assertEqual(result['state'], 'success')

    def test_packageDetail_noId(self):
        """获取课程包信息---未传课程包id"""
        response = requests.post(self.base_url, params={})
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_packageDetail_errorId(self):
        """获取课程包信息---不存在的课程包id"""
        response = requests.post(self.base_url, params={'id':1})
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '当前课程包不存在')
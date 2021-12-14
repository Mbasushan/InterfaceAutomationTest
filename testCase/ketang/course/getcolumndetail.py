#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token

#专栏信息
class ColumnDetail(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/api/getcolumndetail'

    def test_columnDetail(self):
        """获取专栏信息"""
        access_token=Token.getToken()
        response=requests.post(self.base_url,params={'id':258,'access_token':access_token})
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')

    def test_columnDetail_noToken(self):
        """获取专栏信息---未登录"""
        response = requests.post(self.base_url, params={'id': 258})
        result = response.json()
        print(result)
        self.assertEqual(result['state'], 'success')

    def test_columnDetail_noId(self):
        """获取专栏信息---未传专栏id"""
        response = requests.post(self.base_url, params={})
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_columnDetail_errorId(self):
        """获取专栏信息---不存在的专栏id"""
        response = requests.post(self.base_url, params={'id':1})
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '当前专栏不存在')
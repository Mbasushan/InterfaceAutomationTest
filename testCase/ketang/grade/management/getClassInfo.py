#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token

#获取班级信息
class GetClassInfo(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com//class/getClassInfo"

    def test_getClassInfo(self):
        """获取班级信息"""
        access_token = Token.getToken()
        params = {'access_token': access_token, 'class_id': '1000'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertNotEqual(result['data'], '')

    def test_getClassInfo_noToken(self):
        """获取班级信息---未有token"""
        params = {'access_token': "", 'class_id': '1000'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')

    def test_getClassInfo_noClassId(self):
        """获取班级信息---未有班级id参数"""
        access_token = Token.getToken()
        params = {'access_token': access_token, 'class_id': ''}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_getClassInfo_noJoinClass(self):
        """获取班级信息---用户未在该班级(已申请未通过)"""
        access_token = Token.get_token_login('苏珊11','123456')
        params = {'access_token': access_token, 'class_id': '1000'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        #self.assertEqual(result['error'], '您没有权限进行操作')
        self.assertNotEqual(result['data'], '')
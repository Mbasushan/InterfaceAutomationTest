#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import testCase.ketang.grade.management.base.joinClass as joinClass


#申请入班通过
class PassJoinApply(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/passJoinApply"
        self.access_token = Token.get_token_login('sxs14', '123456')

    def test_passJoinApply(self):
        """申请入班通过"""
        #判断用户20392是否申请入班,有则通过，无则创建用户申请
        joinClass.join_class(self)
        params = {'access_token': self.access_token, 'class_id': 1079,'user_id':20392}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(len(result['data']),0)

    def test_passJoinApply_noToken(self):
        """申请入班通过---未传token"""
        params = {'access_token': "", 'class_id': 1079, 'user_id': 20392}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_passJoinApply_noClassId(self):
        """申请入班通过---未传class_id"""
        params = {'access_token': self.access_token,'user_id': 20392}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'您没有权限进行操作')

    def test_passJoinApply_noUserId(self):
        """申请入班通过---未传user_id"""
        params = {'access_token': self.access_token,'class_id':1079}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'您没有权限进行操作')
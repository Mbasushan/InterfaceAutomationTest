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

    def test_passJoinApply(self):
        """申请入班通过"""
        #判断用户20059是否申请入班,有则通过，无则创建用户申请
        joinClass.join_class(self)
        access_token = Token.getToken()
        params = {'access_token': access_token, 'class_id': 1003,'user_id':20059}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(len(result['data']),0)

    def test_passJoinApply_noToken(self):
        """申请入班通过---未传token"""
        params = {'access_token': "", 'class_id': 1003, 'user_id': 20059}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_passJoinApply_noClassId(self):
        """申请入班通过---未传class_id"""
        access_token = Token.getToken()
        params = {'access_token': access_token,'user_id': 20059}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'您没有权限进行操作')

    def test_passJoinApply_noUserId(self):
        """申请入班通过---未传user_id"""
        access_token = Token.getToken()
        params = {'access_token': access_token,'class_id':1003}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'您没有权限进行操作')
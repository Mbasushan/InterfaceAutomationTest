#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token

#获取入班申请列表
class GetJoinApplyList(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/getJoinApplyList"

    def test_getJoinApplyList(self):
        """获取入班申请列表"""
        access_token = Token.getToken()
        params = {'access_token': access_token, 'class_id': 1000}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertNotEqual(len(result['data']), 0)

    def test_getJoinApplyList_normal(self):
        """获取入班申请列表---普通成员获取"""
        access_token = Token.get_token_login('苏珊15','123456')
        params = {'access_token': access_token, 'class_id': 1000}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'您没有权限进行操作')

    def test_getJoinApplyList_admin(self):
        """获取入班申请列表---管理员获取"""
        access_token = Token.get_token_login('苏珊13', '123456')
        params = {'access_token': access_token, 'class_id': 1000}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertNotEqual(len(result['data']),0)

    def test_getJoinApplyList_noToken(self):
        """获取入班申请列表---未传token"""
        params = {'access_token': "", 'class_id': 1000}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_getJoinApplyList_noClassId(self):
        """获取入班申请列表---未传classId"""
        access_token=Token.getToken()
        params = {'access_token': access_token}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '您没有权限进行操作')
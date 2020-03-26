#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import testCase.ketang.grade.management.base.setClassManagerBase as setClassManagerBase

#获取入班申请列表
class GetJoinApplyList(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/getJoinApplyList"
        self.access_token = Token.get_token_login('sxs14', '123456')

    def test_getJoinApplyList(self):
        """获取入班申请列表"""
        params = {'access_token': self.access_token, 'class_id': 1079}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertNotEqual(len(result['data']), 0)

    def test_getJoinApplyList_normal(self):
        """获取入班申请列表---普通成员获取"""
        access_token = Token.get_token_login('sxs16','123456')
        params = {'access_token': access_token, 'class_id': 1079}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'您没有权限进行操作')

    def test_getJoinApplyList_admin(self):
        """获取入班申请列表---管理员获取"""
        #设置为管理员
        setClassManagerBase.setClassManager_admin(self, self.access_token)
        access_token = Token.get_token_login('sxs15', '123456')
        params = {'access_token': access_token, 'class_id': 1079}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertNotEqual(len(result['data']),0)

    def test_getJoinApplyList_noToken(self):
        """获取入班申请列表---未传token"""
        params = {'access_token': "", 'class_id': 1079}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_getJoinApplyList_noClassId(self):
        """获取入班申请列表---未传classId"""
        params = {'access_token': self.access_token}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '您没有权限进行操作')
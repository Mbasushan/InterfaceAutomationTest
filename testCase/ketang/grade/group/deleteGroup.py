#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token

#删除班级分组
class DeleteGroup(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/delGroup"
        self.access_token=Token.get_token_login('sxs14','123456')

    def test_deleteGroup_noToken(self):
        """删除班级分组-未传token"""
        params = {'access_token': "", 'class_id': 1079, 'group_id': id}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')

    def test_deleteGroup_noClassId(self):
        """删除班级分组-未传classId"""
        params = {'access_token': self.access_token,  'group_id': id}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_deleteGroup_noGroupId(self):
        """删除班级分组-未传groupId"""
        params = {'access_token': self.access_token,  'class_id': 1079}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')
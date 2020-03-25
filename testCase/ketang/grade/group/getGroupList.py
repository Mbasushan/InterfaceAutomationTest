#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import testCase.ketang.grade.group.base.getGroupListBase as getGroupListBase


#获取分组列表
class GetGroupList(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/getGroupList"
        self.access_token=Token.get_token_login('sxs14','123456')

    def test_getGroupList(self):
        """获取分组列表"""
        getGroupListBase.getGroupList(self,self.access_token)

    def test_getGroupList_noToken(self):
        """获取分组列表---未传Token"""
        params = {'access_token': "", 'class_id': 1003}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_getGroupList_noClassId(self):
        """获取分组列表---未传ClassId"""
        params = {'access_token': self.access_token}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')
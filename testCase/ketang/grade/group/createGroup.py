#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import testCase.ketang.grade.group.base.createGroupBase as createGroupBase
import testCase.ketang.grade.group.base.deleteGroupBase as deleteGroupBase

#创建班级分组
class CreateGroup(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/createGroup"

    def test_createGroup(self):
        """创建班级分组"""
        #创建
        groupId=createGroupBase.create_group(self)
        print("创建班级分组成功")
        #删除
        deleteGroupBase.delete_group(self,groupId)
        print("删除班级分组成功")

    def test_createGroup_noToken(self):
        """创建班级分组---未传token"""
        params = {'access_token': "", 'class_id': 1000, 'name': '测试'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')

    def test_createGroup_noClassId(self):
        """创建班级分组---未传classId"""
        access_token=Token.getToken()
        params = {'access_token': access_token,  'name': '测试'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_createGroup_noName(self):
        """创建班级分组---未传name"""
        access_token=Token.getToken()
        params = {'access_token': access_token, 'class_id': 1000}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')
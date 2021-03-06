#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import testCase.ketang.grade.group.base.createGroupBase as createGroupBase
import testCase.ketang.grade.group.base.deleteGroupBase as deleteGroupBase

#修改班级分组
class EditGroup(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/editGroup"
        self.access_token=Token.get_token_login('sxs14','123456')

    def test_editGroup(self):
        """修改班级分组"""
        #创建分组
        groupId=createGroupBase.create_group(self,self.access_token)
        print("创建班级分组")
        #修改分组
        params={'access_token':self.access_token,'group_id':groupId,'class_id':1079,'name':'修改分组'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['data']['result'],1)
        print('修改班级分组成功')
        #删除分组
        deleteGroupBase.delete_group(self,groupId,self.access_token)
        print("删除班级分组成功")

    def test_editGroup_noToken(self):
        """修改班级分组---未传token"""
        # 创建分组
        groupId = createGroupBase.create_group(self,self.access_token)
        print("创建班级分组")
        params = {'access_token': "", 'group_id': groupId, 'class_id': 1079, 'name': '修改分组'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')
        # 删除分组
        deleteGroupBase.delete_group(self, groupId,self.access_token)
        print("删除班级分组成功")


    def test_editGroup_noClassId(self):
        """修改班级分组---未传ClassId"""
        # 创建分组
        groupId = createGroupBase.create_group(self,self.access_token)
        print("创建班级分组")
        params = {'access_token': self.access_token, 'group_id': groupId,  'name': '修改分组'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')
        # 删除分组
        deleteGroupBase.delete_group(self, groupId,self.access_token)
        print("删除班级分组成功")

    def test_editGroup_noGroupId(self):
        """修改班级分组---未传groupId"""
        params = {'access_token': self.access_token, 'class_id': 1079,  'name': '修改分组'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_editGroup_noName(self):
        """修改班级分组---未传name"""
        # 创建分组
        groupId = createGroupBase.create_group(self,self.access_token)
        print("创建班级分组")
        params = {'access_token': self.access_token, 'group_id': groupId,  'class_id': 1079}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')
        # 删除分组
        deleteGroupBase.delete_group(self, groupId,self.access_token)
        print("删除班级分组成功")

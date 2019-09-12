#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import unittest
import requests
import testCase.common.getToken as Token
import testCase.ketang.grade.group.base.getGroupListBase as getGroupListBase


#获取分组成员列表
class GetGroupMemberList(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/getGroupMemberList"

    def test_getGroupMemberList(self):
        """获取分组成员列表"""
        access_token=Token.getToken()
        list=getGroupListBase.getGroupList(self)
        for i in range(len(list)):
            groupId=list[i]['group_id']
            params={'access_token':access_token,'group_id':groupId,'class_id':1000}
            response=requests.get(self.base_url,params)
            result=response.json()
            print('分组成员数量：',len(result['data']['member_list']))
            print(result['data']['member_list'])
            self.assertNotEqual(len(result['data']),0)

    def test_getGroupMemberList_noToken(self):
        """获取分组成员列表---未传token"""
        list = getGroupListBase.getGroupList(self)
        for i in range(len(list)):
            groupId = list[i]['group_id']
            params = {'access_token': "", 'group_id': groupId, 'class_id': 1000}
            response = requests.get(self.base_url, params)
            result = response.json()
            print(result)
            self.assertEqual(result['error'], '获取账号信息失败')

    def test_getGroupMemberList_noClassId(self):
        """获取分组成员列表---未传classId"""
        access_token=Token.getToken()
        list = getGroupListBase.getGroupList(self)
        for i in range(len(list)):
            groupId = list[i]['group_id']
            params = {'access_token': access_token, 'group_id': groupId}
            response = requests.get(self.base_url, params)
            result = response.json()
            print(result)
            self.assertEqual(result['error'], '参数错误')

    def test_getGroupMemberList_noGroupId(self):
        """获取分组成员列表---未传groupId"""
        access_token = Token.getToken()
        params = {'access_token': access_token, 'class_id': 1000}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')
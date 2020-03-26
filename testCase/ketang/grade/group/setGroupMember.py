#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import json
import unittest
import requests
import testCase.common.getToken as Token

#设置分组成员
class SetGroupMember(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/setGroupMember"
        self.access_token = Token.get_token_login('sxs14', '123456')

    def test_setGroupMember(self):
        """设置分组成员"""
        params = {'access_token': self.access_token, 'class_id': 1079, 'set_user_ids': '["20271","20314"]', 'group_id': 78}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['data']['result'],1)
        #清除分组成员
        clear_member(self)

    def test_setGroupMember_noToken(self):
        """设置分组成员---未传token"""
        params = {'access_token': "", 'class_id': 1079, 'set_user_ids': '["20271","20314"]', 'group_id': 78}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_setGroupMember_noClassId(self):
        """设置分组成员---未传classId"""
        params = {'access_token': self.access_token, 'set_user_ids': '["20271","20314"]', 'group_id': 78}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_setGroupMember_noGroupId(self):
        """设置分组成员---未传groupId"""
        params = {'access_token': self.access_token, 'set_user_ids': '["20271","20314"]', 'class_id': 1079}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_setGroupMember_noUserIds(self):
        """设置分组成员---未传成员id,清除分组成员"""
        clear_member(self)

    def test_setGroupMember_errorGroupId(self):
        """设置分组成员---该班级未有该分组"""
        params = {'access_token': self.access_token, 'set_user_ids': '["20271","20314"]', 'group_id': 1}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')


#清除分组成员
def clear_member(self):
    params = {'access_token': self.access_token, 'class_id': 1079, 'group_id': 78}
    response = requests.post(self.base_url, params)
    result = response.json()
    print(result)
    self.assertEqual(result['data']['result'], 2)
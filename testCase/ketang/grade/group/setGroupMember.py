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

    def test_setGroupMember(self):
        """设置分组成员"""
        access_token = Token.getToken()
        params = {'access_token': access_token, 'class_id': 1000, 'set_user_ids': '["20035","20061"]', 'group_id': 17}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['data']['result'],1)
        #清除分组成员
        clear_member(self)

    def test_setGroupMember_noToken(self):
        """设置分组成员---未传token"""
        params = {'access_token': "", 'class_id': 1000, 'set_user_ids': '["20035","20061"]', 'group_id': 17}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_setGroupMember_noClassId(self):
        """设置分组成员---未传classId"""
        access_token=Token.getToken()
        params = {'access_token': access_token, 'set_user_ids': '["20035","20061"]', 'group_id': 17}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_setGroupMember_noGroupId(self):
        """设置分组成员---未传groupId"""
        access_token=Token.getToken()
        params = {'access_token': access_token, 'set_user_ids': '["20035","20061"]', 'class_id': 1000}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_setGroupMember_noUserIds(self):
        """设置分组成员---未传成员id,清除分组成员"""
        clear_member(self)

#清除分组成员
def clear_member(self):
    access_token = Token.getToken()
    params = {'access_token': access_token, 'class_id': 1000, 'group_id': 17}
    response = requests.post(self.base_url, params)
    result = response.json()
    print(result)
    self.assertEqual(result['data']['result'], 2)
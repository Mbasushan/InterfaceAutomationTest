#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token

#删除班级成员
class DeleteClass(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/delMember"
        self.access_token=Token.get_token_login('sxs14','123456')

    def test_deleteMember(self):
        """删除班级成员"""
        params = {'access_token': self.access_token, 'class_id': 1079,'del_user_id':20392}
        response = requests.post(self.base_url, params)
        result = response.json()
        print("删除成功",result)
        self.assertEqual(len(result['data']), 0)
        #删除成功后，添加该成员
        access_tokens = Token.get_token_login('sxs16', '123456')
        params = {'access_token': access_tokens, 'class_id': '1079'}
        response1 = requests.post('http://ke.test.mbalib.com//class/applyJoinClass', params)
        result1 = response1.json()
        print("添加成功", result1)
        self.assertEqual(len(result1['data']), 0)

    def test_deleteMember_noToken(self):
        """删除班级成员---未传token"""
        params = {'access_token': "", 'class_id': 1079, 'del_user_id': 20392}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_deleteMember_admin(self):
        """删除班级成员---管理员"""
        access_token = Token.get_token_login('sxs15', '123456')
        params = {'access_token': access_token, 'class_id': 1079, 'del_user_id': 20392}
        response = requests.post(self.base_url, params)
        result = response.json()
        print("删除成功", result)
        self.assertEqual(len(result['data']), 0)
        # 删除成功后，添加该成员
        access_tokens = Token.get_token_login('sxs16', '123456')
        params = {'access_token': access_tokens, 'class_id': '1079'}
        response1 = requests.post('http://ke.test.mbalib.com//class/applyJoinClass', params)
        result1 = response1.json()
        print("添加成功", result1)
        self.assertEqual(len(result1['data']), 0)

    def test_deleteMember_normal(self):
        """删除班级成员---普通成员"""
        access_token=Token.get_token_login('sxs16','123456')
        params = {'access_token': access_token, 'class_id': 1079, 'del_user_id': 20392}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'您没有权限进行操作')

    def test_deleteMember_noClassId(self):
        """删除班级成员---未传班级id"""
        params = {'access_token': self.access_token, 'del_user_id': 20392}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'没有找到班级')

    def test_deleteMember_noDelUserId(self):
        """删除班级成员---未传成员id"""
        params = {'access_token': self.access_token, 'class_id': 1079}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')
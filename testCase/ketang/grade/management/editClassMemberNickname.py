#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token

#管理员修改成员昵称
class EditClassMemberNickname(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com//class/editClassMemberNickname"
        self.access_token = Token.get_token_login('sxs14', '123456')

    def test_editClassMemberNickname(self):
        """管理员修改成员昵称"""
        params={'access_token':self.access_token,'class_id':'1079','user_id':'20392','nickname':'接口测试修改昵称'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(len(result['data']),0)

    def test_editClassMemberNickname_noToken(self):
        """管理员修改成员昵称---该用户不是管理员"""
        access_token = Token.get_token_login('sxs16','123456')
        params={'access_token':access_token,'class_id':'1079','user_id':'20392','nickname':'接口测试修改昵称'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'您没有权限进行操作')

    def test_editClassMemberNickname_noClassId(self):
        """管理员修改成员昵称-未传班级id"""
        access_token = Token.get_token_login('sxs15', '123456')
        params={'access_token':access_token,'class_id':'','user_id':'20392','nickname':'接口测试修改昵称'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_editClassMemberNickname_noUserId(self):
        """管理员修改成员昵称-未传user_id"""
        access_token = Token.get_token_login('sxs15','123456')
        params = {'access_token': access_token, 'class_id': '1079', 'user_id': '', 'nickname': '接口测试修改昵称'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_editClassMemberNickname_noNickname(self):
        """管理员修改成员昵称-未传nickname"""
        access_token = Token.get_token_login('sxs15', '123456')
        params = {'access_token': access_token, 'class_id': '1079', 'user_id': '20392', 'nickname': ''}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token

#获取成员/班级的信息
class GetMemberInfo(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/class/getMemberInfo'

    def test_getMemberInfo(self):
        """获取成员/班级的信息"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':'1000','user_id':'19939','member_id':'154'}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)

    def test_getMemberInfo_noToken(self):
        """获取成员/班级的信息---未登录"""
        params = {'access_token': "", 'class_id': '1000', 'user_id': '19939', 'member_id': '154'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')


    def test_getMemberInfo_noClassId(self):
        """获取成员/班级的信息---未传班级Id"""
        access_token=Token.getToken()
        params = {'access_token': access_token, 'user_id': '19939', 'member_id': '154'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'没有找到班级')

    def test_getMemberInfo_noUserId(self):
        """获取成员/班级的信息---未传用户Id"""
        access_token=Token.getToken()
        params = {'access_token': access_token, 'class_id': '1000', 'member_id': '154'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['data']['member_id'],'154')

    def test_getMemberInfo_noMemberId(self):
        """获取成员/班级的信息---未传班级成员Id"""
        access_token = Token.getToken()
        params = {'access_token': access_token, 'class_id': '1000',  'user_id': '19939'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['data']['user_id'], '19939')

    def test_getMemberInfo_noId(self):
        """获取成员/班级的信息---未传班级成员Id和用户Id"""
        access_token = Token.getToken()
        params = {'access_token': access_token, 'class_id': '1000'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print("未传班级成员Id和用户Id,获取的是登录用户的信息")
        self.assertEqual(result['data']['user_id'], '20035')
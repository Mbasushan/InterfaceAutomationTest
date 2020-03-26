#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token


#获取成员分组列表
class GetMemberGroupList(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/getMemberGroupList"
        self.access_token=Token.get_token_login('sxs14','123456')

    def test_getMemberGroupList(self):
        """获取成员分组列表"""
        params={'access_token':self.access_token,'class_id':1079,'user_id':20271}
        response=requests.get(self.base_url,params)
        result=response.json()
        self.assertNotEqual(len(result['data']),0)
        list=len(result['data']['group_list'])
        if list!=0:
            print("该用户存在分组")
        else:
            print("该用户不归属任何分组")
        print(result)

    def test_getMemberGroupList_noToken(self):
        """获取成员分组列表---未传Token"""
        params={'access_token':"",'class_id':1079,'user_id':20271}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],"获取账号信息失败")

    def test_getMemberGroupList_noClassId(self):
        """获取成员分组列表---未传class_id"""
        params = {'access_token': self.access_token, 'user_id': 20271}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], "参数错误")

    def test_getMemberGroupList_noUserId(self):
        """获取成员分组列表---未传user_id"""
        params = {'access_token': self.access_token,'class_id':1079}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], "参数错误")

    def test_getMemberGroupList_errorUserId(self):
        """获取成员分组列表---用户不是该班级成员"""
        params = {'access_token': self.access_token,'class_id':1079,'user_id':20386}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], "找不到成员信息")
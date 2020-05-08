#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token
import testCase.crm.member.base.addMemberBase as addMemberBase
import testCase.crm.member.base.delMemberBase as delMemberBase

#添加成员
class AddMembers(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/member/addMembers'
        self.access_token=Token.getToken()

    def test_addMembers(self):
        """代理商：添加成员"""
        #添加成员
        memberId=addMemberBase.add_member(self,self.access_token)
        #删除成员
        delMemberBase.delete_member(self,memberId)

    def test_addMembers_noToken(self):
        """代理商：添加成员-未传token"""
        response = requests.post(self.base_url, params={'access_token': '', 'mobiles': '17359262064'})
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'令牌错误')

    def test_addMembers_noMobiles(self):
        """代理商：添加成员-未传手机号"""
        response = requests.post(self.base_url, params={'access_token': self.access_token, 'mobiles': ''})
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')
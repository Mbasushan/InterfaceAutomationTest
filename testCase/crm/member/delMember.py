#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token
import testCase.crm.member.base.addMemberBase as addMemberBase
import testCase.crm.member.base.delMemberBase as delMemberBase

#删除成员
class DeleteMember(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/member/deleteMember'
        self.access_token=Token.getToken()

    def test_delMembers(self):
        """代理商：删除成员"""
        #添加成员
        memberId=addMemberBase.add_member(self,self.access_token)
        #删除成员
        delMemberBase.delete_member(self,memberId)

    def test_delMembers_noToken(self):
        """代理商：删除成员-未传token"""
        response = requests.post(self.base_url, params={'access_token': '', 'member_id': '228'})
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'令牌错误')

    def test_delMember_noId(self):
        """代理商：删除成员-未传成员id"""
        response = requests.post(self.base_url, params={'access_token': self.access_token, 'member_id': ''})
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')
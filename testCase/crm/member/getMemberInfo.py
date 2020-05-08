#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token
import testCase.crm.member.base.getMemberList as getMemberList

#成员详情
class GetMemberInfo(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/member/getMemberInfo'
        self.access_token=Token.getToken()

    def test_getMemberInfo(self):
        """成员详情"""
        #获取成员列表
        list=getMemberList.get_member_list(self,self.access_token)
        if list!=None:
            member_id=list[0]['member_id']
            params={'access_token':self.access_token,'member_id':member_id}
            response=requests.post(self.base_url,params)
            result=response.json()
            print(result)

    def test_getMemberInfo_noToken(self):
        """成员详情-未传Token"""
        #获取成员列表
        list=getMemberList.get_member_list(self,self.access_token)
        if list!=None:
            member_id=list[0]['member_id']
            params={'access_token':'','member_id':member_id}
            response=requests.post(self.base_url,params)
            result=response.json()
            print(result)

    def test_getMemberInfo_noMemberId(self):
        """成员详情-未传成员id"""
        params={'access_token':self.access_token,'member_id':''}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')
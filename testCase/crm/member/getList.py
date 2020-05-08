#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token
import testCase.crm.member.base.getMemberList as getMemberList

#获取成员列表
class GetList(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/member/getList'
        self.access_token=Token.getToken()

    def test_getList(self):
        """获取成员列表"""
        list=getMemberList.get_member_list(self,self.access_token)
        print(list)
        print('该代理商成员人数：',len(list))


    def test_getList_keyWords(self):
        """获取成员列表-搜索成员"""
        response = requests.post(self.base_url, params={'access_token': self.access_token,'key_words':'Sxs1'})
        result = response.json()
        print(result)
        print('该代理商成员人数：', result['count'])

#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token
import testCase.crm.apply.base.getApplyList as getApplyList

#获取通知列表
class GetApplyList(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/apply/getList'
        self.access_token=Token.getToken()

    def test_getApplyList(self):
        """获取通知列表-未处理"""
        list=getApplyList.get_apply_list(self,self.access_token,'1')
        if len(list)!=0:
            print("该代理商未处理通知条数为：",len(list))
        else:
            print("该代理商未已处理通知")

    def test_getApplyList_processed(self):
        """获取通知列表-已处理"""
        list=getApplyList.get_apply_list(self,self.access_token,'2')
        if len(list)!=0:
            print("该代理商已处理通知条数为：",len(list))
        else:
            print("该代理商无已处理通知")

    def test_getApplyList_normal(self):
        """获取通知列表-普通成员"""
        list = getApplyList.get_apply_list(self, Token.get_token_login('Sxs15','123456'), '')
        if len(list) != 0:
            print("该成员的通知条数为：", len(list))
        else:
            print("该成员无通知")

    def test_getApplyList_noToken(self):
        """获取通知列表-未传token"""
        response = requests.post(self.base_url, params={'access_token': '', 'state': '1'})
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'令牌错误')
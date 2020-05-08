#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token
import testCase.crm.customer.base.getCustomerList as getCustomerList

#获取客户列表
class GetList(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/customer/getList'
        self.access_token=Token.getToken()

    def test_getList(self):
        """获取客户列表"""
        list=getCustomerList.get_customer_list(self,self.access_token)
        print('该代理商客户人数为：',len(list))

    def test_getList_search(self):
        """获取客户列表-根据昵称搜索客户"""
        response = requests.post(self.base_url, params={'access_token': self.access_token,'key_words':'Sxs1'})
        result = response.json()
        print(result)
        self.assertEqual(result['list'][0]['customer_nickname'],'Sxs1')

    def test_getList_searchMoblie(self):
        """获取客户列表-根据手机号搜索客户"""
        response = requests.post(self.base_url, params={'access_token': self.access_token,'key_words':'15960445986'})
        result = response.json()
        print(result)
        self.assertEqual(result['list'][0]['customer_mobile'],'15960445986')


    def test_getList_noToken(self):
        """获取客户列表-未传token"""
        response = requests.post(self.base_url, params={'access_token': ''})
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'令牌错误')
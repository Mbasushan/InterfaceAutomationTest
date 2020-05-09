#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token
import testCase.crm.order.base.getOrderList as getOrderList
import testCase.crm.member.base.getMemberList as getMemberList
#获取订单列表
class GetList(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/order/getList'
        self.access_token=Token.getToken()

    def test_getOrderList(self):
        """获取订单列表"""
        list = getOrderList.get_order_list(self, self.access_token)
        print('该代理商订单数为：', len(list))

    def test_getList_searchMoblie(self):
        """获取订单列表-根据手机号搜索客户"""
        response = requests.post(self.base_url, params={'access_token': self.access_token,'key_words':'15960445986'})
        result = response.json()
        print(result)
        list=result['list']
        if list==None:
            print('无数据')
        else:
            self.assertEqual(list[0]['customer_mobile'], '15960445986')


    def test_getList_searchMemberId(self):
        """获取订单列表-根据成员id搜索客户"""
        #获取成员列表
        memList=getMemberList.get_member_list(self,self.access_token)
        if memList==None:
            print('无数据')
        else:
            i=0
            for i in range(len(memList)):
                response = requests.post(self.base_url, params={'access_token': self.access_token,'member_id':memList[i]['member_id']})
                result = response.json()
                list=result['list']
                if list==None:
                    print('无数据')
                else:
                    print('有订单数：',result['count'])

    def test_getList_noToken(self):
        """获取订单列表-未传token"""
        response = requests.post(self.base_url, params={'access_token':''})
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '令牌错误')
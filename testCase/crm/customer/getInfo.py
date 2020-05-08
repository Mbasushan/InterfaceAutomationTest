#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token
import testCase.crm.customer.base.getCustomerList as getCustomerList

#获取客户详情
class GetInfo(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/customer/getInfo'
        self.access_token=Token.getToken()

    def test_getInfo(self):
        """获取客户详情"""
        #获取客户列表
        list=getCustomerList.get_customer_list(self,self.access_token)
        if len(list)!=0:
            i=0
            for i in range(len(list)):
                id=list[i]['customer_id']
                response=requests.post(self.base_url,params={'customer_id':id})
                result=response.json()
                print(result)
                self.assertEqual(result['customer_id'],id)
        else:
            print('该代理商没有客户')

    def test_getInfo_noId(self):
        """获取客户详情-未传客户id"""
        response=requests.post(self.base_url,params={'customer_id':''})
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')
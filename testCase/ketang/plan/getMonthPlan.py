#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token


#获取月计划列表(时间选择)
class UserPlanList(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/studyPlan/getMonthPlan'

    def test_getMonthPlan(self):
        """获取月计划列表(时间选择)"""
        access_token=Token.getToken()
        params={'access_token':access_token,'year':2019,'month':6}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']),0)


    def test_getMonthPlan_noToken(self):
        """获取月计划列表(时间选择)---未登录"""
        params={'access_token':"",'year':2019,'month':6}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_getMonthPlan_noYear(self):
        """获取月计划列表(时间选择)---未传year参数"""
        access_token=Token.getToken()
        params={'access_token':access_token,'month':6}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')


    def test_getMonthPlan_noMonth(self):
        """获取月计划列表(时间选择)---未传month参数"""
        access_token=Token.getToken()
        params={'access_token':access_token,'year':2019}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')
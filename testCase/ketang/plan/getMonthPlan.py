#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import datetime


#获取月计划列表(时间选择)
class UserPlanList(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/studyPlan/getMonthPlan'
        self.accsee_token = Token.getToken()

    def test_getMonthPlan(self):
        """获取月计划列表(时间选择)"""
        #获取当前年
        year=datetime.datetime.now().year
        #获取当前月
        month=datetime.datetime.now().month
        params={'access_token':self.accsee_token,'year':year,'month':month}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']),0)


    def test_getMonthPlan_noToken(self):
        """获取月计划列表(时间选择)---未登录"""
        # 获取当前年
        year = datetime.datetime.now().year
        # 获取当前月
        month = datetime.datetime.now().month
        params = {'access_token': '', 'year': year, 'month': month}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_getMonthPlan_noYear(self):
        """获取月计划列表(时间选择)---未传year参数"""
        # 获取当前年
        year = datetime.datetime.now().year
        # 获取当前月
        month = datetime.datetime.now().month
        params = {'access_token': self.accsee_token, 'year': '', 'month': month}
        response = requests.get(self.base_url, params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')


    def test_getMonthPlan_noMonth(self):
        """获取月计划列表(时间选择)---未传month参数"""
        # 获取当前年
        year = datetime.datetime.now().year
        # 获取当前月
        month = datetime.datetime.now().month
        params = {'access_token': self.accsee_token, 'year': year, 'month': ''}
        response = requests.get(self.base_url, params)
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')
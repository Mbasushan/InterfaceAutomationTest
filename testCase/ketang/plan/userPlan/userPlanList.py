#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import unittest
import requests
import testCase.common.getToken as Token


#用户加入的计划列表
class UserPlanList(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/studyPlan/userPlanList'

    def test_userPlanList(self):
        """用户加入的计划列表"""
        access_token=Token.getToken()
        response=requests.get(self.base_url,params={'access_token':access_token})
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']),0)

    def test_userPlanList_page(self):
        """用户加入的计划列表---分页"""
        access_token = Token.getToken()
        start=0
        count=0
        params={'access_token': access_token,'start':start,'num':10}
        response = requests.get(self.base_url, params)
        result = response.json()
        self.assertNotEqual(len(result['data']), 0)
        count=count+len(result['data']['list'])
        i=0
        while len(result['data']['list']) >0:
            i=i+1
            start=start+10
            params = {'access_token': access_token, 'start': start, 'num': 10}
            response = requests.get(self.base_url, params)
            result = response.json()
            count=count+len(result['data']['list'])
        print("总加入计划数：",count)
        print("分页次数：",i)
        self.assertEqual(math.ceil(count/10),i)

    def test_userPlanList_noToken(self):
        """用户加入的计划列表---未登录"""
        response=requests.get(self.base_url)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')
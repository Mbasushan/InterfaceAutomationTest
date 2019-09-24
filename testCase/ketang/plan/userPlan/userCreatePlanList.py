#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import unittest
import requests
import testCase.common.getToken as Token


#用户/班级的创建计划列表
class UserPlanList(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/studyPlan/userCreatePlanList'

    def test_user_createPlanList(self):
        """用户的创建计划列表"""
        access_token=Token.getToken()
        params={'access_token':access_token}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']),0)

    def test_user_createPlanList_noToken(self):
        """用户的创建计划列表---未登录"""
        params={'access_token':""}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_class_createPlanList(self):
        """班级的创建计划列表"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':1000}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']),0)

    def test_class_createPlanList_noToken(self):
        """班级的创建计划列表---未登录"""
        params={'access_token':"",'class_id':1000}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')

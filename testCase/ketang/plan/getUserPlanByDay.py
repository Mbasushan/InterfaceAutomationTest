#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import testCase.common.getTime as getTime


#获取用户某天学习计划
class GetUserPlanByDay(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/studyPlan/getUserPlanByDay'

    def test_getUserPlanByDay(self):
        """获取用户某天学习计划"""
        time=getTime.now_time('%Y-%m-%d')
        params={'access_token':Token.getToken(),'date':time}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']),0)

    def test_getUserPlanByDay_noToken(self):
        """获取用户某天学习计划---未登录"""
        time=getTime.now_time('%Y-%m-%d')
        params={'access_token':"",'date':time}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_getUserPlanByDay_noDay(self):
        """获取用户某天学习计划---未传日期"""
        time=getTime.now_time('%Y-%m-%d')
        params={'access_token':Token.getToken()}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')
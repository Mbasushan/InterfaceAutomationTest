#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token


#计划详情
class UserPlanList(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/studyPlan/planDetail'

    def test_planDetail(self):
        """计划详情"""
        access_token=Token.getToken()
        params={'access_token':access_token,'plan_id':217}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']),0)

    def test_planDetail_noToken(self):
        """计划详情---未登录"""
        params = {'access_token': "", 'plan_id': 217}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertNotEqual(len(result['data']), 0)

    def test_planDetail_noPlanId(self):
        """计划详情---未传计划id"""
        access_token=Token.getToken()
        params={'access_token':access_token}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'计划不存在')

    def test_planDetail_errorPlanId(self):
        """计划详情---不存在的计划id"""
        access_token=Token.getToken()
        params={'access_token':access_token,'plan_id':2}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'计划不存在')
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import testCase.ketang.plan.base.creatPlanBase as creatPlanBase
import testCase.ketang.plan.base.delPlanBase as delPlanBase

#退出学习计划
class ExitPlan(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/studyPlan/exitPlan'

    def test_exitPlan(self):
        """退出学习计划"""
        # 创建学习计划
        planId = creatPlanBase.creat_plan_pass(self)
        # 加入学习计划
        access_token = Token.getToken()
        response = requests.post('http://ke.test.mbalib.com/studyPlan/joinplan', params={'access_token': access_token, 'plan_id': planId})
        result = response.json()
        self.assertEqual(result['state'], 'success')
        #退出学习计划
        response1=requests.post(self.base_url,params={'access_token':access_token,'plan_id':planId})
        result1=response1.json()
        self.assertEqual(len(result1['data']),0)
        # 删除计划
        delPlanBase.delete_plan(str(planId))

    def test_exitPlan_noToken(self):
        """退出学习计划---未登录"""
        # 创建学习计划
        planId = creatPlanBase.creat_plan_pass(self)
        # 加入学习计划
        access_token = Token.getToken()
        response = requests.post('http://ke.test.mbalib.com/studyPlan/joinplan', params={'access_token': access_token, 'plan_id': planId})
        result = response.json()
        self.assertEqual(result['state'], 'success')
        # 退出学习计划
        response1 = requests.post(self.base_url, params={ 'plan_id': planId})
        result1 = response1.json()
        print(result1)
        self.assertEqual(result1['error'], '获取账号信息失败')
        # 删除计划
        delPlanBase.delete_plan(str(planId))

    def test_exitPlan_noPlanId(self):
        """退出学习计划---未传计划Id"""
        access_token = Token.getToken()
        # 退出学习计划
        response = requests.post(self.base_url, params={ 'access_token': access_token})
        result = response.json()
        print(result)
        self.assertEqual(len(result['data']), 0)

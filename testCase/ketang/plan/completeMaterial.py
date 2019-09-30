#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import testCase.common.getTime as getTime
import testCase.ketang.plan.base.creatPlanBase as creatPlanBase
import testCase.ketang.plan.base.delPlanBase as delPlanBase

#完成计划章节
class CompleteMaterial(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/studyPlan/completeMaterial'

    def test_completeMaterial(self):
        """完成计划章节"""
        time=getTime.now_time('%y-%m-%d')
        # 创建学习计划
        planId = creatPlanBase.creat_plan_pass(self)
        # 加入学习计划
        access_token = Token.getToken()
        response = requests.post('http://ke.test.mbalib.com/studyPlan/joinplan',params={'access_token': access_token, 'plan_id': planId})
        result = response.json()
        self.assertEqual(result['state'], 'success')
        #完成计划章节
        params={'access_token':access_token,'plan_item_type':'material','plan_item_id':896,'plan_id':planId,'date':time}
        response1=requests.post(self.base_url,params)
        result1=response1.json()
        print(result1)
        if result1['data']['is_finish']==1:
            print("计划章节学习完成")
            self.assertEqual(result1['data']['is_finish'], 1)
        else:
            print("计划章节未学习完成")
            self.assertEqual(result1['data']['is_finish'], 0)
        #删除计划
        delPlanBase.delete_plan(str(planId))

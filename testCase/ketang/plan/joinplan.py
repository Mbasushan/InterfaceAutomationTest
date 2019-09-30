#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import testCase.ketang.plan.base.creatPlanBase as creatPlanBase
import testCase.ketang.plan.base.delPlanBase as delPlanBase
import db_fixture.mysql_db as mySqlConnect

#加入学习计划
class JoinPlan(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/studyPlan/joinplan'

    def test_joinPlan(self):
        """加入个人学习计划"""
        #创建学习计划
        planId = creatPlanBase.creat_plan_pass(self)
        #加入学习计划
        access_token=Token.getToken()
        response=requests.post(self.base_url,params={'access_token':access_token,'plan_id':planId})
        result=response.json()
        self.assertEqual(result['state'],'success')
        # 删除计划
        delPlanBase.delete_plan(str(planId))
        #删除计划中的成员
        delete(str(planId))

    def test_joinClass_plan(self):
        """加入班级学习计划"""
        #创建学习计划
        planId = creatPlanBase.creat_ClassPlan_pass(self)
        #加入学习计划
        access_token=Token.getToken()
        response=requests.post(self.base_url,params={'access_token':access_token,'plan_id':planId})
        result=response.json()
        self.assertEqual(result['state'],'success')
        # 删除计划
        delPlanBase.delete_plan(str(planId))
        #删除计划中的成员
        delete(str(planId))

    def test_joinClass_plan_noJoin(self):
        """加入班级学习计划---不是该班级成员"""
        #创建学习计划
        planId = creatPlanBase.creat_ClassPlan_pass(self)
        #加入学习计划
        access_token=Token.get_token_login('sxs14','123456')
        response=requests.post(self.base_url,params={'access_token':access_token,'plan_id':planId})
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'您不在此班级内，不能加入该计划')
        # 删除计划
        delPlanBase.delete_plan(str(planId))
        #删除计划中的成员
        delete(str(planId))

    def test_joinClass_plan_repeatJoin(self):
        """加入班级学习计划---重复加入该计划"""
        #创建学习计划
        planId = creatPlanBase.creat_ClassPlan_pass(self)
        #加入学习计划
        access_token=Token.getToken()
        requests.post(self.base_url,params={'access_token':access_token,'plan_id':planId})
        response = requests.post(self.base_url, params={'access_token': access_token, 'plan_id': planId})
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'您已经加入过该计划了')
        # 删除计划
        delPlanBase.delete_plan(str(planId))
        #删除计划中的成员
        delete(str(planId))

    def test_joinPlan_noToken(self):
        """加入个人学习计划---未登录"""
        # 创建学习计划
        planId = creatPlanBase.creat_plan_pass(self)
        # 加入学习计划
        response = requests.post(self.base_url, params={'plan_id': planId})
        result = response.json()
        self.assertEqual(result['error'], '获取账号信息失败')
        # 删除计划
        delPlanBase.delete_plan(str(planId))

    def test_joinPlan_errorPlanId(self):
        """加入个人学习计划---计划不存在"""
        access_token=Token.getToken()
        response=requests.post(self.base_url,params={'access_token':access_token,'plan_id':2})
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'计划不存在')

#删除
def delete(planId):
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "delete FROM ketang_user_plan WHERE up_plan_id='" + planId + "'"
    try:
        cs1.execute(query)
        conn.commit()
    except:
        conn.rollback()
    # 关闭cursor对象
    cs1.close()
    # 关闭connection对象
    conn.close()
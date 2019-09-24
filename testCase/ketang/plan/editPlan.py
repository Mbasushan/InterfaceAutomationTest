#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import json
import unittest
import requests
import testCase.common.getToken as Token
import testCase.common.getTime as getTime
import testCase.ketang.plan.base.creatPlanBase as creatPlanBase
import testCase.ketang.plan.base.delPlanBase as delPlanBase
import db_fixture.mysql_db as mySqlConnect

#创建学习计划
class Editplan(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/studyPlan/editplan'

    def test_creatPlan(self):
        """创建用户个人学习计划---草稿箱"""
        planId=creatPlanBase.creat_plan(self)
        #查询数据库看是否添加成功的是个人计划
        self.assertEqual(select_classId('class_id',str(planId)),0)
        #删除计划
        delPlanBase.delete_plan(str(planId))

    def test_creatPlan_pass(self):
        """创建用户个人学习计划---发布"""
        planId = creatPlanBase.creat_plan_pass(self)
        # 查询数据库看是否添加成功的是个人计划
        self.assertEqual(select_classId('class_id', str(planId)), 0)
        # 删除计划
        delPlanBase.delete_plan(str(planId))

    def test_creatPlan_classPlan(self):
        """创建班级学习计划---草稿箱"""
        planId = creatPlanBase.creat_ClassPlan(self)
        # 查询数据库看是否添加成功的是个人计划
        self.assertEqual(select_classId('class_id', str(planId)), 30)
        # 删除计划
        delPlanBase.delete_plan(str(planId))

    def test_creatPlan_classPlan_pass(self):
        """创建班级学习计划---发布"""
        planId = creatPlanBase.creat_ClassPlan_pass(self)
        # 查询数据库看是否添加成功的是个人计划
        self.assertEqual(select_classId('class_id', str(planId)), 30)
        # 删除计划
        delPlanBase.delete_plan(str(planId))

    def test_creatPlan_noToken(self):
        """创建用户个人学习计划---未登录"""
        time=getTime.now_time('%Y-%m-%d')
        courses='[{ "item_type": "column","item_id": 258,"starttime":"'+time+'","learn_style": "material","learn_duration": 3,"learn_days": "0,1,2,3,4,5,6","task":1}]'
        params={'title':'接口创建学习计划','access_token':"",'courses':courses,'start_time':time}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')


    def test_creatPlan_noCourses(self):
        """创建用户个人学习计划---未传课程"""
        access_token=Token.getToken()
        time=getTime.now_time('%Y-%m-%d')
        params={'title':'接口创建学习计划','access_token':access_token,'start_time':time}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '课程未提交')

    def test_creatPlan_noStartTime(self):
        """创建用户个人学习计划---未登录"""
        access_token = Token.getToken()
        time=getTime.now_time('%Y-%m-%d')
        courses='[{ "item_type": "column","item_id": 258,"starttime":"'+time+'","learn_style": "material","learn_duration": 3,"learn_days": "0,1,2,3,4,5,6","task":1}]'
        params={'title':'接口创建学习计划','access_token':access_token,'courses':courses}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '参数start_time错误')

    def test_creatPlan_image(self):
        """创建用户个人学习计划---传计划封面图"""
        access_token = Token.getToken()
        time = getTime.now_time('%Y-%m-%d')
        courses = '[{ "item_type": "column","item_id": 258,"starttime":"' + time + '","learn_style": "material","learn_duration": 3,"learn_days": "0,1,2,3,4,5,6","task":1}]'
        # 以2进制方式打开图片
        with open('D:/InterfaceAutomationTest/image/1.png', "rb")as f_abs:
            body = {'img': ('1.jpg', f_abs, 'image/jpg')}
            params = {'title': '接口创建学习计划', 'desc': '描述描述', 'state': 'new', 'access_token': access_token,
                      'courses': courses, 'start_time': time}
            response = requests.post(self.base_url, params, files=body)
            result = json.loads(response.text)
            print(result)
            self.assertEqual(result['state'], 'success')
        # 查询数据库看是否添加成功的是个人计划
        self.assertEqual(select_classId('class_id',str(result['plan_id'])), 0)
        # 删除计划
        delPlanBase.delete_plan(str(result['plan_id']))

    def test_creatPlan_classPlan_noJoinClass(self):
        """创建班级学习计划---不是该班级成员"""
        access_token = Token.get_token_login('sxs14','123456')
        time = getTime.now_time('%Y-%m-%d')
        courses = '[{ "item_type": "column","item_id": 258,"starttime":"' + time + '","learn_style": "material","learn_duration": 3,"learn_days": "0,1,2,3,4,5,6","task":1}]'
        params = {'title': '接口创建学习计划', 'desc': '描述描述','class_id':1000,'state':'new','access_token':access_token,'courses':courses,'start_time':time}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '您不是该班级的成员')


    def test_editPlan(self):
        """修改学习计划"""
        planId = creatPlanBase.creat_plan(self)
        # 查询数据库看是否添加成功的是个人计划
        self.assertEqual(select_classId('class_id',str(planId)), 0)
        #修改计划，修改计划标题
        access_token = Token.getToken()
        time = getTime.now_time('%Y-%m-%d')
        courses = '[{ "item_type": "column","item_id": 258,"starttime":"' + time + '","learn_style": "material","learn_duration": 3,"learn_days": "0,1,2,3,4,5,6","task":1}]'
        response=requests.post(self.base_url,params={'access_token':access_token,'plan_id':planId,'title':'修改学习计划标题','courses':courses,'start_time': time})
        result=response.json()
        self.assertEqual(result['state'], 'success')
        # 查询数据库看是否添加成功的是个人计划
        title=select_classId('title',str(planId))
        self.assertEqual('修改学习计划标题',title)
        # 删除计划
        delPlanBase.delete_plan(str(result['plan_id']))

#查询
def select_classId(params,planId):
        # 连接数据库
        conn = mySqlConnect.my_db()
        # 获取cursor对象
        cs1 = conn.cursor()
        # 查询主题信息
        query=''
        if params=='class_id':
            query = "SELECT plan_class_id FROM ketang_plan WHERE plan_id='"+planId+"'"
        elif params=='title':
            query = "SELECT plan_title FROM ketang_plan WHERE plan_id='"+planId+"'"
        cs1.execute(query)
        result = cs1.fetchall()[0][0]
        return result
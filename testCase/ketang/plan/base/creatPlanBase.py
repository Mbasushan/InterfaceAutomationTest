#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import testCase.common.getTime as getTime

#创建个人学习计划-保存未发布
def creat_plan(self):
    url='http://ke.test.mbalib.com/studyPlan/editplan'
    access_token=Token.getToken()
    time=getTime.now_time('%Y-%m-%d')
    courses='[{ "item_type": "column","item_id": 258,"starttime":"'+time+'","learn_style": "material","learn_duration": 3,"learn_days": "0,1,2,3,4,5,6","task":1}]'
    detail = '[{"state": "learn","day": "' + time + '","materials": [{"material_id": 896,"item_type": "column","item_id": 258},{"material_id": 897,"item_type": "column","item_id": 258}]}]'
    params={'title':'接口创建学习计划','desc':'描述描述','state':'new','access_token':access_token,'courses':courses,'start_time':time,'detail':detail}
    response=requests.post(url,params)
    result=response.json()
    print(result)
    self.assertEqual(result['state'], 'success')
    return result['plan_id']

#创建个人学习计划---发布
def creat_plan_pass(self):
    url = 'http://ke.test.mbalib.com/studyPlan/editplan'
    access_token = Token.getToken()
    time = getTime.now_time('%Y-%m-%d')
    courses = '[{ "item_type": "column","item_id": 258,"starttime":"' + time + '","learn_style": "material","learn_duration": 3,"learn_days": "0,1,2,3,4,5,6","task":1}]'
    detail = '[{"state": "learn","day": "' + time + '","materials": [{"material_id": 896,"item_type": "column","item_id": 258},{"material_id": 897,"item_type": "column","item_id": 258}]}]'
    params = {'title': '接口创建学习计划', 'desc': '描述描述', 'state': 'pass', 'access_token': access_token, 'courses': courses,'detail':detail,'start_time': time}
    response = requests.post(url, params)
    result = response.json()
    print(result)
    self.assertEqual(result['state'], 'success')
    return result['plan_id']

#创建班级学习计划-保存未发布
def creat_ClassPlan(self):
    url='http://ke.test.mbalib.com/studyPlan/editplan'
    access_token=Token.getToken()
    time=getTime.now_time('%Y-%m-%d')
    courses='[{ "item_type": "column","item_id": 258,"starttime":"'+time+'","learn_style": "material","learn_duration": 3,"learn_days": "0,1,2,3,4,5,6","task":1}]'
    detail = '[{"state": "learn","day": "' + time + '","materials": [{"material_id": 896,"item_type": "column","item_id": 258},{"material_id": 897,"item_type": "column","item_id": 258}]}]'
    params={'title':'接口创建学习计划','desc':'描述描述','class_id':1000,'state':'new','access_token':access_token,'courses':courses,'start_time':time,'detail':detail}
    response=requests.post(url,params)
    result=response.json()
    print(result)
    self.assertEqual(result['state'], 'success')
    return result['plan_id']

#创建班级学习计划---发布
def creat_ClassPlan_pass(self):
    url = 'http://ke.test.mbalib.com/studyPlan/editplan'
    access_token = Token.getToken()
    time = getTime.now_time('%Y-%m-%d')
    courses = '[{ "item_type": "column","item_id": 258,"starttime":"' + time + '","learn_style": "material","learn_duration": 3,"learn_days": "0,1,2,3,4,5,6","task":1}]'
    detail = '[{"state": "learn","day": "' + time + '","materials": [{"material_id": 896,"item_type": "column","item_id": 258},{"material_id": 897,"item_type": "column","item_id": 258}]}]'
    params = {'title': '接口创建学习计划', 'desc': '描述描述','class_id':1000, 'state': 'pass', 'access_token': access_token, 'courses': courses,'detail':detail,'start_time': time}
    response = requests.post(url, params)
    result = response.json()
    print(result)
    self.assertEqual(result['state'], 'success')
    return result['plan_id']
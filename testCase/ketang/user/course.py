#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import unittest
import requests
import testCase.common.getToken as Token


#用户购买的课程列表（新版）
class Usecourses(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/user/courses"
        self.accsee_token=Token.getToken()

    def test_usecourses_newSignup(self):
        """用户购买的课程列表（新版）--排序：最新购买"""
        #order  排序 signup-最新购买,latestlearn-最近学习
        params = {'access_token': self.accsee_token,'start':0,'num':10,'order':'signup'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)


    def test_usecourses_latestlearn(self):
        """用户购买的课程列表（新版）--排序最近学习"""
        #order  排序 signup-最新购买,latestlearn-最近学习
        params = {'access_token': self.accsee_token,'start':0,'num':10,'order':'latestlearn'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)


    def test_usecourses_sel_type_all(self):
        """用户购买的课程列表（新版）--筛选类型：全部"""
        #order  排序 signup-最新购买,latestlearn-最近学习
        params = {'access_token': self.accsee_token,'start':0,'num':10,'order':'latestlearn','sel_type':'all'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)

    def test_usecourses_sel_type_learn_asc(self):
        """用户购买的课程列表（新版）--筛选类型：未学完课程"""
        #order  排序 signup-最新购买,latestlearn-最近学习
        params = {'access_token': self.accsee_token,'start':0,'num':10,'order':'latestlearn','sel_type':'learn_asc'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)

    def test_usecourses_sel_type_learn_desc(self):
        """用户购买的课程列表（新版）--筛选类型：已学完课程"""
        #order  排序 signup-最新购买,latestlearn-最近学习
        params = {'access_token': self.accsee_token,'start':0,'num':10,'order':'latestlearn','sel_type':'learn_desc'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        print(len(result['data']))

    def test_usecourses_sel_type_task_asc(self):
        """用户购买的课程列表（新版）--筛选类型：未完成作业"""
        #order  排序 signup-最新购买,latestlearn-最近学习
        params = {'access_token': self.accsee_token,'start':0,'num':10,'order':'latestlearn','sel_type':'task_asc'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        print(len(result['data']))

    def test_usecourses_sel_type_task_desc(self):
        """用户购买的课程列表（新版）--筛选类型：已完成作业"""
        #order  排序 signup-最新购买,latestlearn-最近学习
        params = {'access_token': self.accsee_token,'start':0,'num':10,'order':'latestlearn','sel_type':'task_desc'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        print(len(result['data']))

    def test_usecourses_sel_type_certificate_apply(self):
        """用户购买的课程列表（新版）--筛选类型：未领取证书"""
        #order  排序 signup-最新购买,latestlearn-最近学习
        params = {'access_token': self.accsee_token,'start':0,'num':10,'order':'latestlearn','sel_type':'certificate_apply'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        print(len(result['data']))


    def test_usecourses_sel_type_certificate_passed(self):
        """用户购买的课程列表（新版）--筛选类型：已领取证书"""
        #order  排序 signup-最新购买,latestlearn-最近学习
        params = {'access_token': self.accsee_token,'start':0,'num':10,'order':'latestlearn','sel_type':'certificate_passed'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        print(len(result['data']))


    def test_usecourses_sel_type_not_evaluated(self):
        """用户购买的课程列表（新版）--筛选类型：未评价课程"""
        #order  排序 signup-最新购买,latestlearn-最近学习
        params = {'access_token': self.accsee_token,'start':0,'num':10,'order':'latestlearn','sel_type':'not_evaluated'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        print(len(result['data']))


    def test_usecourses_noToken(self):
        """用户购买的课程列表（新版）--未传token"""
        #order  排序 signup-最新购买,latestlearn-最近学习
        params = {'access_token': '','start':0,'num':10,'order':'signup'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')


    def test_usecourses_noStart(self):
        """用户购买的课程列表（新版）--未传start"""
        #order  排序 signup-最新购买,latestlearn-最近学习
        params = {'access_token': self.accsee_token,'num':10,'order':'signup'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)

    def test_usecourses_noNum(self):
        """用户购买的课程列表（新版）--未传num,默认条数为20条"""
        #order  排序 signup-最新购买,latestlearn-最近学习
        params = {'access_token': self.accsee_token,'start':0,'order':'signup'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)

    #循环加载我的课程列表数据
    def test_course_load(self):
        """课堂首页【猜你喜欢】列表-分页"""
        start = 0
        params = {"start": start, "num": 10,"access_token":self.accsee_token,'order':'signup'}
        response = requests.post(self.base_url, params)
        result = response.json()
        size =len(result['data'])
        i = 0
        while len(result['data']) != 0:
            start = start + 10
            params = {"start": start, "num": 10,"access_token":self.accsee_token,'order':'signup'}
            response = requests.post(self.base_url, params)
            result = response.json()
            size = len(result['data']) + size
            i = i + 1
            print("第", str(i) + "页")
        print("总数:", size)
        self.assertEqual(result['count'],size)
       # self.assertEqual(math.ceil(size / 10), i)
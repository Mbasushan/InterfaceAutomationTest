#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math

import requests
import unittest
import testCase.common.getToken as Token
import testCase.ketang.course.base.categoryBase as categoryBase

#获取所有课程
class GetAllCourseList(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/class/getAllCourseList'

    def test_getAllCourseList(self):
        """获取所有课程"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':1000}
        response=requests.get(self.base_url,params)
        result=response.json()
        self.assertNotEqual(len(result['data']),0)

    def test_getAllCourseList_noToken(self):
        """获取所有课程---未传token"""
        params={'access_token':"",'class_id':1000}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']),0)

    def test_getAllCourseList_noClassId(self):
        """获取所有课程---未传classId"""
        access_token=Token.getToken()
        params={'access_token':access_token}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'没有找到班级')

    def test_getAllCourseList_categoryId(self):
        """获取所有课程---根据分类获取课程"""
        access_token = Token.getToken()
        categoryIds=categoryBase.get_categoryId(self)
        for i in range(len(categoryIds)):
            categoryId=categoryIds[i]
            params = {'access_token': access_token,'class_id':1000,'category_id':categoryId}
            response = requests.get(self.base_url, params)
            result = response.json()
            print(result)
            self.assertNotEqual(len(result['data']), 0)

    def test_getAllCourseList_page(self):
        """获取所有课程---分页"""
        access_token=Token.getToken()
        start=0
        params={'access_token':access_token,'class_id':1000,'start':start,'num':10}
        response=requests.get(self.base_url,params)
        result=response.json()
        i=-1
        count=0
        while len(result['data']['list'])>0:
            i=i+1
            start=start+10
            params = {'access_token': access_token, 'class_id': 1000, 'start': start, 'num': 10}
            response = requests.get(self.base_url, params)
            result = response.json()
            count=len(result['data']['list'])+count
        print("总课程数：",count)
        self.assertEqual(math.ceil(count/10),i)
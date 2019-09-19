#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token

#获取成员课程/专栏详情 (课程学习明细)
class GetUserCourseDetail(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/class/getUserCourseDetail'

    def test_course_detail(self):
        """获取成员课程详情 (课程学习明细)"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':1000,'user_id':20035,'type':'course','item_id':8520014}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(len(result['data']),0)

    def test_coloumn_detail(self):
        """获取成员专栏详情 (课程学习明细)"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':1000,'user_id':20035,'type':'column','item_id':258}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(len(result['data']), 0)

    def test_detail_noToken(self):
        """获取成员课程详情 (课程学习明细)---未登录"""
        params = {'access_token': "", 'class_id': 1000, 'user_id': 20035, 'type': 'course','item_id': 8520014}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')

    def test_detail_noClassId(self):
        """获取成员课程详情 (课程学习明细)---未传班级id"""
        access_token=Token.getToken()
        params = {'access_token': access_token, 'user_id': 20035, 'type': 'course','item_id': 8520014}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '操作失败')

    def test_detail_noUserId(self):
        """获取成员课程详情 (课程学习明细)---未传用户id"""
        access_token = Token.getToken()
        params = {'access_token': access_token, 'class_id': 1000, 'type': 'course', 'item_id': 8520014}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '操作失败')

    def test_detail_noType(self):
        """获取成员课程详情 (课程学习明细)---未传课程类型"""
        access_token = Token.getToken()
        params = {'access_token': access_token, 'class_id': 1000,'user_id': 20035, 'item_id': 8520014}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '操作失败')

    def test_detail_noItemId(self):
        """获取成员课程详情 (课程学习明细)---未传课程id"""
        access_token = Token.getToken()
        params = {'access_token': access_token, 'class_id': 1000,'user_id': 20035,'type': 'course'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '操作失败')
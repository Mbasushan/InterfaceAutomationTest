#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token

#获取成员课程/专栏详情 (课程学习明细)
class GetUserCourseDetail(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/class/getUserCourseDetail'
        self.access_token=Token.get_token_login('sxs14','123456')

    def test_course_detail(self):
        """获取成员课程详情 (课程学习明细)"""
        params={'access_token':self.access_token,'class_id':1079,'user_id':20314,'type':'course','item_id':8526372}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']),0)

    def test_coloumn_detail(self):
        """获取成员专栏详情 (课程学习明细)"""
        params={'access_token':self.access_token,'class_id':1079,'user_id':20314,'type':'column','item_id':258}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']), 0)

    def test_detail_noToken(self):
        """获取成员课程详情 (课程学习明细)---未登录"""
        params = {'access_token': "", 'class_id': 1079, 'user_id': 20314, 'type': 'course','item_id': 8526372}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')

    def test_detail_noClassId(self):
        """获取成员课程详情 (课程学习明细)---未传班级id"""
        params = {'access_token': self.access_token, 'user_id': 20314, 'type': 'course','item_id': 8526372}
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
        params = {'access_token': access_token, 'class_id': 1000,'user_id': 20314, 'item_id': 8520014}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '操作失败')

    def test_detail_noItemId(self):
        """获取成员课程详情 (课程学习明细)---未传课程id"""
        params = {'access_token': self.access_token, 'class_id': 1079,'user_id': 20314,'type': 'course'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '操作失败')
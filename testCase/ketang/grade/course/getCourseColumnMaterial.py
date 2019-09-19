#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import unittest


#获取课程/专栏的听课章节详情
class GetCourseColumnMaterial(unittest.TestCase):


    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/class/getCourseColumnMaterial'

    def test_getCourse_material(self):
        """获取课程听课章节详情"""
        params={'type':'course','item_id':8520014,'user_id':20035}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result['data']['list'])
        self.assertNotEqual(len(result['data']),0)

    def test_getColumn_material(self):
        """获取专栏听课章节详情"""
        params={'type':'column','item_id':57,'user_id':20035}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result['data']['list'])
        self.assertNotEqual(len(result['data']),0)

    def test_getCourse_material_noType(self):
        """获取课程/专栏听课章节详情---未传课程类型"""
        params = {'item_id': 8520014, 'user_id': 20035}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_getCourse_material_noItemId(self):
        """获取课程/专栏听课章节详情---未传课程id"""
        params = {'type':'course', 'user_id': 20035}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(len(result['data']['list']), 0)

    def test_getCourse_material_noUserId(self):
        """获取课程/专栏听课章节详情---未传用户id"""
        params = {'type':'course','item_id': 8520014}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

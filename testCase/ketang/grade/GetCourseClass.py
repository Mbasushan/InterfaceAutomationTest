#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token


#获取课程班级信息
class GetCourseClass(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/class/GetCourseClass'

    def test_getCourseClass(self):
        """获取课程班级信息"""
        access_token=Token.getToken()
        params={'item_type':'course','item_id':8520014,'access_token':access_token}
        response=requests.post(self.base_url,params)
        result=response.json()
        size=len(result['data'])
        if size==0:
            print("该课程未添加到任何一个班级")
        else:
            print("该课程有添加到以下班级：")
        print(result)

    def test_getColumnClass(self):
        """获取专栏班级信息"""
        access_token=Token.getToken()
        params={'item_type':'column','item_id':258,'access_token':access_token}
        response=requests.post(self.base_url,params)
        result=response.json()
        size=len(result['data'])
        if size==0:
            print("该专栏未添加到任何一个班级")
        else:
            print("该专栏有添加到以下班级：")
        print(result)

    def test_getPackageClass(self):
        """获取课程包班级信息"""
        access_token=Token.getToken()
        params={'item_type':'package','item_id':1014,'access_token':access_token}
        response=requests.post(self.base_url,params)
        result=response.json()
        size=len(result['data'])
        if size==0:
            print("该课程包未添加到任何一个班级")
        else:
            print("该课程包有添加到以下班级：")
        print(result)

    def test_getCourseClass_noToken(self):
        """获取课程班级信息---未登录"""
        params={'item_type':'course','item_id':8520014}
        response=requests.post(self.base_url,params)
        result=response.json()
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_getCourseClass_noItemType(self):
        """获取课程班级信息---未传课程类型"""
        access_token=Token.getToken()
        params={'access_token':access_token,'item_id':8520014}
        response=requests.post(self.base_url,params)
        result=response.json()
        self.assertEqual(result['error'],'参数错误')

    def test_getCourseClass_noIitemId(self):
        """获取课程班级信息---未传课程类型"""
        access_token = Token.getToken()
        params = {'access_token': access_token, 'item_type':'course'}
        response = requests.post(self.base_url, params)
        result = response.json()
        self.assertEqual(result['error'], '参数错误')
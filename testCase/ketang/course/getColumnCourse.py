#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token

#获取专栏下的课程信息
class GetColumnCourse(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/api/getColumnCourse"

    def test_getColumnCourse(self):
        """获取专栏下的课程信息"""
        response=requests.get(self.base_url,params={'id':258,'access_token':Token.getToken()})
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')

    def test_getColumnCourse_noToken(self):
        """获取专栏下的课程信息---未登录"""
        response=requests.get(self.base_url,params={'id':258})
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')

    def test_getColumnCourse_noId(self):
        """获取专栏下的课程信息---未传专栏id"""
        response=requests.get(self.base_url,params={'access_token':Token.getToken()})
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')
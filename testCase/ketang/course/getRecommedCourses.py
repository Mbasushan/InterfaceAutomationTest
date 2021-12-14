#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token

#随机课程(用于条目主页中显示的课程)
class GetRecommedCourses(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/api/GetRecommedCourses"

    def test_getRecommedCourses(self):
        """随机课程(用于条目主页中显示的课程)	数量（默认5)"""
        response=requests.get(self.base_url,params={'keyword':'MBA智库特邀讲师	','num':5})
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')

    def test_getRecommedCourses_noKeyWord(self):
        """随机课程(用于条目主页中显示的课程)---未传老师的值"""
        response=requests.get(self.base_url,params={'num':5})
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')

    def test_getRecommedCourses_noNum(self):
        """随机课程(用于条目主页中显示的课程)---不传参数"""
        response=requests.get(self.base_url)
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')

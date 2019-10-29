#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token

#单课信息
class CourseDetail(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/api/getcoursedetail'

    def test_courseDetail(self):
        """获取单课信息"""
        access_token=Token.getToken()
        response=requests.post(self.base_url,params={'id':8526372,'access_token':access_token})
        result=response.json()
        self.assertEqual(result['state'],'success')

    def test_columnDetail_noToken(self):
        """获取单课信息---未登录"""
        response = requests.post(self.base_url, params={'id': 8526372})
        result = response.json()
        print(result)
        self.assertEqual(result['state'], 'success')

    def test_columnDetail_noId(self):
        """获取单课信息---未传单课id"""
        response = requests.post(self.base_url, params={})
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_columnDetail_errorId(self):
        """获取单课信息---不存在的单课id"""
        response = requests.post(self.base_url, params={'id':1})
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '当前课程不存在')
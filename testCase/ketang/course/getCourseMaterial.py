#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token

#获取单课章节
class GetCourseMaterial(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/api/getCourseMaterial'

    def test_getCourseMaterial(self):
        """获取单课章节"""
        response=requests.get(self.base_url,params={'id':8520014,'access_token':Token.getToken()})
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')

    def test_getCourseMaterial_noToken(self):
        """获取单课章节---未登录"""
        response=requests.get(self.base_url,params={'id':8520014})
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')

    def test_getCourseMaterial_noId(self):
        """获取单课章节---未传单课id"""
        response=requests.get(self.base_url,params={'access_token':Token.getToken()})
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')
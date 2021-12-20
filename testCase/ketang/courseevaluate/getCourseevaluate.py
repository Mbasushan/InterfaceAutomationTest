#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token

#获取课程评价
class Getcourseevaluate(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/courseevaluate/overview"
        self.accsee_token = Token.getToken()

    def test_getUserInfo_all(self):
        """获取课程评价-专栏课程的所有评价"""
        params={'itemType':'cloumn','itemId':89,'type':'all'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)

    def test_getUserInfo_course(self):
        """获取课程评价-专栏课程的所有评价"""
        params={'itemType':'course','itemId':8526372,'type':'all'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)

    def test_getUserInfo_nocomment(self):
        """获取课程评价-不包含评价内容"""
        params={'itemType':'cloumn','itemId':89,'type':'nocomment'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)

    def test_getUserInfo_person(self):
        """获取课程评价-个人的评价"""
        params={'itemType':'cloumn','itemId':89,'type':'person','access_token':self.accsee_token}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)


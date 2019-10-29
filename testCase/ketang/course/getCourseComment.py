#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import unittest
import requests
import testCase.common.getToken as Token

#获取课程评论
class GetCourseComment(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/api/GetCourseCommentV2"

    def test_getComment_column(self):
        """获取专栏评论"""
        params={'id':12,'type':'column'}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')

    def test_getComment_course(self):
        """获取单课评论"""
        params={'id':8520014,'type':'course'}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')

    def test_getComment_noId(self):
        """获取专栏评论---未传专栏id"""
        params = {'type': 'column'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['state'], 'success')

    def test_getComment_noType(self):
        """获取专栏评论"""
        params = {'id':12}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['state'], 'success')

    def test_getComment_page(self):
        """获取专栏评论---分页"""
        start = 0
        params = {'id': 12, 'type': 'column',"start":start,"num":10}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        size = len(result['data'])
        i = 0
        while len(result['data'])!=0:
            start=start+10
            params = {'id': 12, 'type': 'column',"start": start, "num": 10}
            response = requests.post(self.base_url, params=params)
            result = response.json()
            size=len(result['data'])+size
            i=i+1
            print("第",str(i)+"页")
        print("总数:",size)
        self.assertEqual(math.ceil(size/10),i)

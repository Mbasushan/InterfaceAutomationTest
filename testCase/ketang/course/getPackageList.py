#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import unittest
import requests
import testCase.common.getToken as Token

#课程包列表
class PackageList(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/api/GetPackageList'

    def test_list(self):
        """课程包列表"""
        response=requests.get(self.base_url)
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')

    def test_list_page(self):
        """课程包列表---分页"""
        start = 0
        params = {"start": start, "num": 10}
        response = requests.post(self.base_url, params=params)
        result = response.json()
        size = len(result['data'])
        i = 1
        while len(result['data']) != 0:
            start = start + 10
            params = {"start": start, "num": 10}
            response = requests.post(self.base_url, params=params)
            result = response.json()
            size = len(result['data']) + size
            i = i + 1
        print("总数:", size)
        print("分页:", i-1)
        self.assertEqual(math.ceil(size / 10), i-1 )
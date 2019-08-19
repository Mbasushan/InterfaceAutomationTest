#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#新课上架
import unittest

import requests


class LatestCourse(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/list/GetLatest"

    def test_getLatest(self):
        """课堂首页获取新课上架"""
        response = requests.get(self.base_url)
        result = response.json()
        print("新课上架课程数：",len(result['data']))
        print("结果：", result['data'])
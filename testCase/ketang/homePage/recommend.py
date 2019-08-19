#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#热门推荐
import unittest
import requests


class Recommend(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/list/getRecommend"

    def test_getLatest(self):
        """课堂首页-热门推荐"""
        response = requests.get(self.base_url)
        result = response.json()
        self.assertEqual(result['state'],'success')
        print("热门推荐课程数：",len(result['data']))
        print("结果：", result['data'])
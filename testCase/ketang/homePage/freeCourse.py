#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#免费课程
import math
import unittest
import requests


class FreeCourse(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/list/GetfreeCourse"

    def test_getfreeCourse(self):
        """课堂首页获取免费课程-到第10个数据"""
        params={"start":"0","num":"10"}
        response = requests.post(self.base_url,data=params)
        result = response.json()
        self.assertEqual(len(result['data']),10)

    def test_getfreeCourse_page(self):
        """课堂首页获取免费课程-分页"""
        size=math.ceil(freeCourse_size(self)/10)
        print("总的免费课程数:",freeCourse_size(self))
        print("一页10条，分页次数：",size)
        start = 0
        count=0
        for i in range(size):
            params={"start":start,"num":10}
            response = requests.post(self.base_url,data=params)
            result = response.json()
            start=start+10
            count=len(result['data'])+count
        self.assertEqual(count, freeCourse_size(self))

def freeCourse_size(self):
    params = {"start": "0", "num": "100"}
    response = requests.post(self.base_url, data=params)
    result = response.json()
    return len(result['data'])
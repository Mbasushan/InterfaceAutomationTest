#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import unittest

import requests

#新课上架
class VipCourse(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/list/GetvipCourse"

    def test_getLatest(self):
        """vip专区课程列表-10个数据"""
        params={'start':'0','num':'10'}
        response = requests.get(self.base_url,params=params)
        result = response.json()
        print("vip专区课程数：",len(result['data']))
        print("结果：", result['data'])
        #判断vip专区是否有【封面图】
        if result['info']:
            print("vip专区有封面图")
            print("封面图地址：",result['info']['image'])
        else:
            print("vip专区未有封面图")

    def test_getvipCourse_page(self):
        """课堂首页获取免费课程-分页"""
        size=math.ceil(vipCourse_size(self)/10)
        print("总的vip课程数:",vipCourse_size(self))
        print("一页10条，分页次数：",size)
        start = 0
        count=0
        for i in range(size):
            params={"start":start,"num":10}
            response = requests.post(self.base_url,data=params)
            result = response.json()
            start=start+10
            count=len(result['data'])+count
        self.assertEqual(count, vipCourse_size(self))

def vipCourse_size(self):
    params = {"start": "0", "num": "100"}
    response = requests.post(self.base_url, data=params)
    result = response.json()
    return len(result['data'])
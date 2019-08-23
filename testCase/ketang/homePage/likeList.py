#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import unittest
import requests
import testCase.common.getToken as Token

#猜你喜欢
class LikeList(unittest.TestCase):

    def test_likeList_login(self):
        """课堂首页【猜你喜欢】列表-登录情况下"""
        url='http://ke.test.mbalib.com/list/getlike'
        access_token=Token.getToken()
        params={"access_token":access_token,"start":0,"num":10}
        response = requests.post(url,params=params)
        result = response.json()
        print("总课程数：", len(result['data']))
        print("结果：", result['data'])

    def test_likeList_Nologin(self):
        """课堂首页【猜你喜欢】列表-未登录情况下"""
        url='http://ke.test.mbalib.com/list/getlike'
        params={"start":0,"num":10}
        response = requests.post(url,params=params)
        result = response.json()
        print("总课程数：",len(result['data']))
        print("结果：", result['data'])

    def test_likeList_load(self):
        """课堂首页【猜你喜欢】列表-分页"""
        url='http://ke.test.mbalib.com/list/getlike'
        start=0
        params={"start":start,"num":10}
        response = requests.post(url,params=params)
        result = response.json()
        size=len(result['data'])
        i = 0
        while len(result['data'])!=0:
            start=start+10
            params = {"start": start, "num": 10}
            response = requests.post(url, params=params)
            result = response.json()
            size=len(result['data'])+size
            i=i+1
            print("第",str(i)+"页")
        print("总数:",size)
        self.assertEqual(math.ceil(size/10),i)

#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token

#是否显示评价课程
class ShowValuate(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/courseevaluate/show"
        self.accsee_token = Token.getToken()

    def test_show(self):
        """是否显示评价课程"""
        params = {'itemType': 'cloumn', 'itemId': 89, 'access_token': self.accsee_token}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        if result['show']==0:
            print('该课程不显示课程评价')
        elif result['show']==1:
            print("该课程显示课程评价")
            if result['evaluate']==1:
                print("该用户已评价课程")
            elif result['evaluate']==0:
                print("该用户未评价课程")

    def test_show_noToken(self):
        """是否显示评价课程---未传token"""
        params = {'itemType': 'cloumn', 'itemId': 89, 'access_token':''}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],"获取账号信息失败")


    def test_show_noId(self):
        """是否显示评价课程---未传课程ID"""
        params = {'itemType': 'cloumn', 'access_token':self.accsee_token}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        if result['show'] == 0:
            print('该课程不显示课程评价')
        elif result['show'] == 1:
            print("该课程显示课程评价")
            if result['evaluate'] == 1:
                print("该用户已评价课程")
            elif result['evaluate'] == 0:
                print("该用户未评价课程")

    def test_show_noType(self):
        """是否显示评价课程---未传课程类型"""
        params = {'itemId': 89, 'access_token':self.accsee_token}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        if result['show'] == 0:
            print('该课程不显示课程评价')
        elif result['show'] == 1:
            print("该课程显示课程评价")
            if result['evaluate'] == 1:
                print("该用户已评价课程")
            elif result['evaluate'] == 0:
                print("该用户未评价课程")

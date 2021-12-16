#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import unittest
from datetime import date, timedelta

import requests
import testCase.common.getToken as Token
import time

#用户课程每日学习时长数据
class Courselearninfo(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/user/courselearninfo"
        self.accsee_token=Token.getToken()

    def test_courselearninfo(self):
        """用用户课程每日学习时长数据-专栏"""
        #获取当前日期
        endTime=date.today().strftime("%Y-%m-%d")
        print(endTime)
        #获取当前日期的前7天
        startTime = (date.today() + timedelta(days=-7)).strftime("%Y-%m-%d")
        print(startTime)
        params = {'access_token': self.accsee_token, 'itemType': 'column', 'itemId': 89,'startTime':startTime,'endTime':endTime}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)


    def test_courselearninfo_course(self):
        """用用户课程每日学习时长数据-单课"""
        #获取当前日期
        endTime=date.today().strftime("%Y-%m-%d")
        print(endTime)
        #获取当前日期的前7天
        startTime = (date.today() + timedelta(days=-7)).strftime("%Y-%m-%d")
        print(startTime)
        params = {'access_token': self.accsee_token, 'itemType': 'course', 'itemId': 8526343,'startTime':startTime,'endTime':endTime}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)

    def test_noToken(self):
        """用用户课程每日学习时长数据-未传token"""
        #获取当前日期
        endTime=date.today().strftime("%Y-%m-%d")
        print(endTime)
        #获取当前日期的前7天
        startTime = (date.today() + timedelta(days=-7)).strftime("%Y-%m-%d")
        print(startTime)
        params = {'itemType': 'column', 'itemId': 89,'startTime':startTime,'endTime':endTime}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')

    def test_courselearninfo_noType(self):
        """用用户课程每日学习时长数据-没传课程类型"""
        #获取当前日期
        endTime=date.today().strftime("%Y-%m-%d")
        print(endTime)
        #获取当前日期的前7天
        startTime = (date.today() + timedelta(days=-7)).strftime("%Y-%m-%d")
        print(startTime)
        params = {'access_token': self.accsee_token,'itemId': 89,'startTime':startTime,'endTime':endTime}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        #self.assertEqual(result['error'], '课程不存在')

    def test_courselearninfo_noId(self):
        """用用户课程每日学习时长数据-没传课程类型"""
        #获取当前日期
        endTime=date.today().strftime("%Y-%m-%d")
        print(endTime)
        #获取当前日期的前7天
        startTime = (date.today() + timedelta(days=-7)).strftime("%Y-%m-%d")
        print(startTime)
        params = {'access_token': self.accsee_token,'itemType': 'column','startTime':startTime,'endTime':endTime}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        #self.assertEqual(result['error'], '课程不存在')

    def test_courselearninfo_noStartTime(self):
        """用用户课程每日学习时长数据-没传开始时间"""
        # 获取当前日期
        endTime = date.today().strftime("%Y-%m-%d")
        print(endTime)
        # 获取当前日期的前7天
        startTime = (date.today() + timedelta(days=-7)).strftime("%Y-%m-%d")
        print(startTime)
        params = {'access_token': self.accsee_token, 'itemType': 'column','itemId': 89,'startTime':startTime}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '开始时间或者结束时间未传')

    def test_courselearninfo_noEndTime(self):
        """用用户课程每日学习时长数据-没传结束时间"""
        # 获取当前日期
        endTime = date.today().strftime("%Y-%m-%d")
        print(endTime)
        # 获取当前日期的前7天
        startTime = (date.today() + timedelta(days=-7)).strftime("%Y-%m-%d")
        print(startTime)
        params = {'access_token': self.accsee_token, 'itemType': 'column','itemId': 89,'startTime':startTime}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '开始时间或者结束时间未传')
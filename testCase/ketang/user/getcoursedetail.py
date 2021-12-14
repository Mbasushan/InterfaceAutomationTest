#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import unittest
import requests
import testCase.common.getToken as Token
import db_fixture.mysql_db as mySqlConnect

#用户课程概况
class Usecoursesdetail(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/user/getcoursedetail"
        self.accsee_token=Token.getToken()

    def test_getcoursedetail_column(self):
        """用户课程概况-专栏"""
        params = {'access_token': self.accsee_token, 'itemType': 'column', 'itemId': 89}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        id=result['landingpage']['data']['cid']
        self.assertEqual(id, '89')
        print(id)

    def test_getcoursedetail_course(self):
        """用户课程概况-单课"""
        params = {'access_token': self.accsee_token, 'itemType': 'course', 'itemId': 8526343}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        id=result['landingpage']['data']['cid']
        self.assertEqual(id, '8526343')
        print(id)

    def test_getcoursedetail_noTOken(self):
        """用户课程概况-未传token"""
        params = { 'itemType': 'course', 'itemId': 8526343}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')

    def test_getcoursedetail_noType(self):
        """用户课程概况-未传课程类型"""
        params = {'access_token': self.accsee_token,  'itemId': 89}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '课程不存在')


    def test_getcoursedetail_noId(self):
        """用户课程概况-未传课程id"""
        params = {'access_token': self.accsee_token,  'itemType': 89}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '课程不存在')
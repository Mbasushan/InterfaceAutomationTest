#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import unittest
import requests
import testCase.common.getToken as Token
import db_fixture.mysql_db as mySqlConnect

#用户证书列表
class GetUserCertificate(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/api/GetUserCertificate"
        self.accsee_token=Token.getToken()

    def test_GetUserCertificate(self):
        """用户证书列表"""
        params = {'access_token': self.accsee_token}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['state'], 'success')


    def test_GetUserCertificate_noToken(self):
        """用户证书列表-未传token"""
        params = {}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')

    #循环加载用户证书列表
    def test_course_load(self):
        """用户证书列表-分页"""
        start = 0
        params = {"start": start, "num": 10,"access_token":self.accsee_token}
        response = requests.post(self.base_url, params)
        result = response.json()
        size =len(result['data'])
        i = 0
        while len(result['data']) != 0:
            start = start + 10
            params = {"start": start, "num": 10,"access_token":self.accsee_token}
            response = requests.post(self.base_url, params)
            result = response.json()
            size = len(result['data']) + size
            i = i + 1
            print("第", str(i) + "页")
        print("总数:", size)
        #self.assertEqual(len(result['data']),size)
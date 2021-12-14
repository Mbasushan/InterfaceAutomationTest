#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token

#获取置顶课程 (接口截止 android:版本号 92 , IOS: 282)
class StickList(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/api/getStickList'

    def test_getStickList(self):
        """获取置顶课程"""
        response=requests.get(self.base_url)
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')
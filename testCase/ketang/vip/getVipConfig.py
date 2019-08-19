#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests

#会员配置
class VIPConfig(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/vip/config"

    def test_getVipConfig(self):
        """获取课堂vip会员配置"""
        response = requests.post(self.base_url)
        result = response.json()
        self.assertEqual(result['state'],'success')
        print("会员配置数据如下：")
        print(result['data'])
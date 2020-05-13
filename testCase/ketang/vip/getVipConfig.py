#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.ketang.vip.base.vipConfig as vipConfig

#会员配置
class VIPConfig(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/vip/config"

    def test_getVipConfig(self):
        """获取课堂vip会员配置"""
        vipConfig.get_vipConfig(self)
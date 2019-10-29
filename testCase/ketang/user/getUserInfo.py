#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token

#用户信息
class GetUserInfo(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/api/GetUserInfo"

    def test_getUserInfo(self):
        """用户信息"""
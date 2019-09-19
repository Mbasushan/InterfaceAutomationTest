#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests

#充值班费选项
class Rechargeoptions(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/rechargeoptions"

    def test_recharge_options(self):
        """充值班费选项"""
        response=requests.get(self.base_url)
        result=response.json()
        print(result)
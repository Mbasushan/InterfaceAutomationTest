#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import unittest

#搜索代理商
class SearchAgent(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/agent/search'

    def test_search(self):
        """搜索代理商"""
        response=requests.post(self.base_url,params={'key':'1'})
        result=response.json()
        print(result)
        if len(result)==0:
            self.assertEqual(len(result), 0)
            print("搜索不到代理商")
        else:
            self.assertEqual(result['agent_key'], '1')
            print("搜索到代理商")

    def test_search_noKey(self):
        """搜索代理商---未传代理商key值"""
        response = requests.post(self.base_url)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')
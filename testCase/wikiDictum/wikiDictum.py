#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import unittest
import requests

#每日一词/有句名言
class WikiDictum(unittest.TestCase):

    def setUp(self):
        self.base_url='http://www.mbalib.com/appwiki/WikiDictum'

    def test_wikiDictum_dailyword(self):
        """每日一词-线上数据"""
        params={'type':'dailyword'}
        response = requests.get(self.base_url,params)
        result = response.json()
        print(result)
        self.assertEqual(result['state'],'success')

    def test_wikiDictum_dailyword_page(self):
        """每日一词-分页-线上数据"""
        start = 0
        params = {'num': 10, 'start': start,'type':'dailyword'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        size = len(result['data'])
        i = 0
        while len(result['data']) != 0:
            start = start + 10
            params = {'num': 10, 'start': start,'type':'dailyword'}
            response = requests.get(self.base_url, params)
            result = response.json()
            size = len(result['data']) + size
            i = i + 1
            print("第", str(i) + "页")
        print("总数:", size)
        self.assertEqual(math.ceil(size / 10), i)

    def test_wikiDictum_afamous(self):
        """有句名言"""
        params={'type':'afamous'}
        response = requests.get(self.base_url,params)
        result = response.json()
        print(result)
        self.assertEqual(result['state'],'success')
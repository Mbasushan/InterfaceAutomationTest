#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest

#首页banner广告
import requests


class Banner(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://www.test.mbalib.com/appwiki/ad"

    def test_ios(self):
        """ios课堂首页banner广告"""
        response = requests.get(self.base_url, params={'type': 'ketang_banner', 'channel': 'ios', 'purge': 'ture'})
        text = response.json()
        print(text)

    def test_ios_fresh(self):
        """ios专业版课堂首页banner广告"""
        response = requests.get(self.base_url, params={'type': 'ketang_banner', 'channel': 'ios_fresh', 'purge': 'ture'})
        text = response.json()
        print(text)

    def test_android(self):
        """Android课堂首页banner广告"""
        response = requests.get(self.base_url, params={'type': 'ketang_banner', 'channel': 'android', 'purge': 'ture'})
        text = response.json()
        print(text)

    def test_pc(self):
        """pc课堂首页banner广告"""
        response = requests.get(self.base_url, params={'type': 'ketang_banner', 'channel': 'ke', 'purge': 'ture'})
        text = response.json()
        print(text)
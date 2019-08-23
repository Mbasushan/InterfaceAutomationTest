#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests

#wiki推荐条目：6大分类
class WikiRecommend(unittest.TestCase):

    def setUp(self):
        self.base_url="http://www.test.mbalib.com/appwiki/WikiRecommend"

    def test_getWikiRecommend(self):
        """获取wiki推荐条目-6大分类"""
        response=requests.get(self.base_url)
        result=response.json()
        self.assertNotEqual(result['data'],'')
        print(result['data']['recommend'])
        data=result['data']['recommend']
        print("6大分类的名称：")
        for i in range(len(data)):
            print(data[i]['data']['key'])

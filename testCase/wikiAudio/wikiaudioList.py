#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests

#条目音频列表
class WikiAudioList(unittest.TestCase):

    def setUp(self):
        self.base_url='http://www.test.mbalib.com/appaudio/wikiaudio'

    def test_wikiAudioList(self):
        """条目音频列表"""
        params={"page_name":"七层次领导力","other":1,'course':1}
        response=requests.get(self.base_url,params)
        result=response.json()
        self.assertEqual(result['state'],'success')
        print("本条目相关音频,条数：",len(result['data']))
        print(result['data'])
        print("听听其他条目音频：")
        print(result['other'])
        self.assertEqual(len(result['other']), 3)
        print("推荐课程，数量为：",len(result['course']))
        print(result['course'])
        self.assertEqual(len(result['course']), 5)

    def test_wikiAudioList_noPageName(self):
        """条目音频列表-未传条目名"""
        params={"other":1,'course':1}
        response=requests.get(self.base_url,params)
        result=response.json()
        self.assertEqual(len(result['data']),0)
        print("本条目相关音频,条数：",len(result['data']))
        print(result['data'])
        print("听听其他条目音频：")
        print(result['other'])
        self.assertEqual(len(result['other']), 3)
        print("推荐课程，数量为：",len(result['course']))
        print(result['course'])
        self.assertEqual(len(result['course']), 5)

    def test_wikiAudioList_noAudio(self):
        """条目音频列表-条目未有音频"""
        params={"page_name":"54545","other":1,'course':1}
        response=requests.get(self.base_url,params)
        result=response.json()
        self.assertEqual(len(result['data']),0)
        print("本条目相关音频,条数：",len(result['data']))
        print(result['data'])
        print("听听其他条目音频：")
        print(result['other'])
        self.assertEqual(len(result['other']), 3)
        print("推荐课程，数量为：",len(result['course']))
        print(result['course'])
        self.assertEqual(len(result['course']), 5)

    def test_wikiAudioList_noOther(self):
        """条目音频列表-未传其他条目参数"""
        params={"page_name":"七层次领导力",'course':1}
        response=requests.get(self.base_url,params)
        result=response.json()
        self.assertEqual(result['state'],'success')
        print("本条目相关音频,条数：",len(result['data']))
        print(result['data'])
        if 'other' not in result:
            print("返回参数未有其他条目音频数据")
        print("推荐课程，数量为：",len(result['course']))
        print(result['course'])
        self.assertEqual(len(result['course']), 5)

    def test_wikiAudioList_Other_0(self):
        """条目音频列表-other的值为0，不返回其他音频数据"""
        params={"page_name":"七层次领导力",'other':0,'course':1}
        response=requests.get(self.base_url,params)
        result=response.json()
        self.assertEqual(result['state'],'success')
        print("本条目相关音频,条数：",len(result['data']))
        print(result['data'])
        if 'other' not in result:
            print("返回参数未有其他条目音频数据")
        print("推荐课程，数量为：",len(result['course']))
        print(result['course'])
        self.assertEqual(len(result['course']),5)

    def test_wikiAudioList_noCourse(self):
        """条目音频列表-未传推荐课程参数"""
        params={"page_name":"七层次领导力",'other':1}
        response=requests.get(self.base_url,params)
        result=response.json()
        self.assertEqual(result['state'],'success')
        print("本条目相关音频,条数：",len(result['data']))
        print(result['data'])
        print("听听其他条目音频：")
        print(result['other'])
        self.assertEqual(len(result['other']), 3)
        if 'course' not in result:
            print("返回参数未有推荐课程数据")

    def test_wikiAudioList_noCourse_0(self):
        """条目音频列表-course的值为0，不返回推荐课程数据"""
        params={"page_name":"七层次领导力",'other':1,"course":0}
        response=requests.get(self.base_url,params)
        result=response.json()
        self.assertEqual(result['state'],'success')
        print("本条目相关音频,条数：",len(result['data']))
        print(result['data'])
        print("听听其他条目音频：")
        print(result['other'])
        self.assertEqual(len(result['other']), 3)
        if 'course' not in result:
            print("返回参数未有推荐课程数据")

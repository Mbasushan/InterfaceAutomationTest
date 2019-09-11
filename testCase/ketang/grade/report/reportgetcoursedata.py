#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token


#课程报表曲线图
class Reportgetcoursedata(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/reportgetcoursedata"

    def test_reportgetcoursedata_course(self):
        """课程报表曲线图---课程类型：课程，时间类型为：按日"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':1000,'itemtype':'course','itemid':8520014,'timetype':'day','start':'2019-09-04','end':'2019-09-11'}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']),0)

    def test_report_course_timeType(self):
        """课程报表曲线图---课程类型：课程,时间类型为：按时"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':1000,'itemtype':'course','itemid':8520014,'timetype':'hour','start':'2019-09-11','end':'2019-09-11'}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']),0)

    def test_reportgetcoursedata_coloum(self):
        """课程报表曲线图---课程类型：专栏,时间类型为：按日"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':1000,'itemtype':'column','itemid':258,'timetype':'day','start':'2019-09-04','end':'2019-09-11'}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']),0)

    def test_report_timeExceeded(self):
        """课程报表曲线图---时间筛选超过31天"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':1000,'itemtype':'column','itemid':258,'timetype':'day','start':'2019-08-04','end':'2019-09-11'}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '选择的天数区间不能超过31天')


    def test_report_coloum_timeType(self):
        """课程报表曲线图---课程类型：专栏,时间类型为：按时"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':1000,'itemtype':'column','itemid':258,'timetype':'hour','start':'2019-09-04','end':'2019-09-11'}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']),0)

    def test_report_noToken(self):
        """课程报表曲线图---未传token"""
        params={'class_id':1000,'itemtype':'course','itemid':8520014,'timetype':'day','start':'2019-09-04','end':'2019-09-11'}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']),0)

    def test_report_noClassId(self):
        """课程报表曲线图---未传classId"""
        access_token=Token.getToken()
        params={'access_token':access_token,'itemtype':'course','itemid':8520014,'timetype':'day','start':'2019-09-04','end':'2019-09-11'}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'没有找到班级')

    def test_report_noItemtype(self):
        """课程报表曲线图---未传itemtype"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':1000,'itemid':8520014,'timetype':'day','start':'2019-09-04','end':'2019-09-11'}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']), 0)

    def test_report_noItemid(self):
        """课程报表曲线图---未传itemid"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':1000,'itemtype':'course','timetype':'day','start':'2019-09-04','end':'2019-09-11'}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']), 0)

    def test_report_noTimetype(self):
        """课程报表曲线图---未传timetype"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':1000,'itemtype':'course','itemid':8520014,'start':'2019-09-04','end':'2019-09-11'}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']), 0)

    def test_report_noStart(self):
        """课程报表曲线图---未传start"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':1000,'itemtype':'course','itemid':8520014,'timetype':'day','end':'2019-09-11'}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '选择的天数区间不能超过31天')

    def test_report_noEnnd(self):
        """课程报表曲线图---未传end"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':1000,'itemtype':'course','itemid':8520014,'timetype':'day','start':'2019-09-11'}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']), 0)
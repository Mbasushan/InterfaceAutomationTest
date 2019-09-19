#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token

#班费明细
class GetTradeList(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/ClassTrade/getTradeList"

    def test_getTradeList(self):
        """班费明细"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':1000}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']['list']),0)

    def test_getTradeList_noToken(self):
        """班费明细---未传token"""
        params={'access_token':"",'class_id':1000}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']['list']),0)

    def test_getTradeList_noClassId(self):
        """班费明细---未传classId"""
        access_token=Token.getToken()
        params={'access_token':access_token}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'没有找到班级')

    def test_getTradeList_noJoinClass(self):
        """班费明细---不是该班级成员"""
        access_token=Token.get_token_login('sxs14','123456')
        params={'access_token':access_token,'class_id':1000}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        #self.assertEqual(result['error'],'您没有权限进行操作')
        self.assertNotEqual(len(result['data']['list']), 0)
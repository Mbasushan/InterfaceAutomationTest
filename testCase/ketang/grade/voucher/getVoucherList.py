#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token

#获取班级优惠券列表
class GetVoucherList(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/getVoucherList"

    def test_getVoucherList(self):
        """获取班级优惠券列表"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':1000}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertNotEqual(len(result['data']),0)

    def test_getVoucherList_noToken(self):
        """获取班级优惠券列表---未传token"""
        params={'access_token':"",'class_id':1000}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_getVoucherList_noClassId(self):
        """获取班级优惠券列表---未传class_id"""
        access_token=Token.getToken()
        params={'access_token':access_token}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'没有找到班级')

    def test_getVoucherList_noJoinClass(self):
        """获取班级优惠劵列表---用户不是该班级成员"""
        access_token = Token.getToken()
        params = {'access_token': access_token,'class_id':1079}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(len(result['data']['list']), 0)
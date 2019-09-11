#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token

#退出班级
class ExitClass(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com//class/exitClass"

    def test_exitClass(self):
        """退出班级"""
        access_token=Token.get_token_login('苏珊11','123456')
        params={'access_token':access_token,'class_id':'1000'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(len(result['data']),0)
        #申请加入班级
        params = {'access_token': access_token, 'class_id': '1000'}
        responses = requests.post('http://ke.test.mbalib.com//class/applyJoinClass', params)
        results = responses.json()
        print(results)
        self.assertEqual(len(results['data']), 0)


    def test_exitClass_noClass(self):
        """退出班级--未加入该班级"""
        access_token=Token.get_token_login('苏珊11','123456')
        params={'access_token':access_token,'class_id':'1003'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'操作失败')


    def test_exitClass_noToken(self):
        """退出班级--未有accesss_token"""
        params={'access_token':"",'class_id':'1000'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_exitClass_noClassId(self):
        """退出班级--未传classId"""
        access_token=Token.get_token_login('苏珊11','123456')
        params={'access_token':access_token}
        response=requests.post(self.base_url,params)
        print(response)
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token

#课程评论
class AddComment(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/api/AddComment"
        self.access_token=Token.get_token_login('sxs14','123456')

    def test_addComment(self):
        """课程评论"""
        params={'id':8526372,'comment':'接口测试评论','access_token':self.access_token}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['showInfo'],'评论成功，审核中，请稍候')

    def test_addComment_errorId(self):
        """课程评论---错误的课程Id"""
        params={'id':12,'comment':'接口测试评论','access_token':self.access_token}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'评论失败')

    def test_addComment_noToken(self):
        """课程评论---未登录"""
        params={'id':8526372,'comment':'接口测试评论'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_addComment_noComment(self):
        """课程评论---未传评论数据"""
        params={'id':8526372,'access_token':self.access_token}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_addComment_noSignup(self):
        """课程评论---未报名"""
        params={'id':8521220,'access_token':self.access_token}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_addComment_sensitive_words(self):
        """课程评论---敏感词"""
        params={'id':8526372,'comment':'红灯区','access_token':self.access_token}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'操作失败，含有敏感词')
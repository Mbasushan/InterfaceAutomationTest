#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token


#入班审查详情
class JoinConditionDetail(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/joinConditionDetail"
        self.access_token=Token.get_token_login('sxs14','123456')

    def test_joinConditionDetail(self):
        """入班审查详情"""
        params={'access_token':self.access_token,'class_id':1079}
        response = requests.post(self.base_url, params)
        result = response.json()
        if len(result)==0:
            print('该班级无入班审核条件')
        else:
            print('该班级有入班审核条件')
            print('课程总数:',result['total_course'])
            print(result)

    def test_joinConditionDetail_noToken(self):
        """入班审查详情-未登录"""
        params={'access_token':'','class_id':1079}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')

    def test_joinConditionDetail_noClassId(self):
        """入班审查详情-未传班级id"""
        params={'access_token':self.access_token,'class_id':''}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')
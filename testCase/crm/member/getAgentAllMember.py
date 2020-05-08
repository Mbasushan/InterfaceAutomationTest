#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token

#代理商全部成员
class GetAgentAllMember(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/member/getAgentAllMember'
        self.access_token=Token.getToken()

    def test_getAgentAllMember(self):
        """代理商全部成员"""
        response = requests.post(self.base_url, params = {'access_token': self.access_token})
        result = response.json()
        print(result)

    def test_getAgentAllMember_noToken(self):
        """代理商全部成员-未传token"""
        response = requests.post(self.base_url, params={'access_token': ''})
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'令牌错误')
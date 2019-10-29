#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token
import testCase.crm.agent.base.registerBase as registerBase
import testCase.crm.agent.base.deleteBase as deleteBase



#取消注册
class CancelRegisterAgent(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/agent/cancelRegister'

    def test_cancelRegister(self):
        """取消注册"""
        agent_id=registerBase.register(self)
        response=requests.post(self.base_url,params={'access_token':Token.get_token_login('sxs14','123456')})
        result=response.json()
        self.assertEqual(result['state'],'success')
        #删除
        deleteBase.delete_crm(str(agent_id))

    def test_cancelRegister_noToken(self):
        """取消注册---未登录"""
        response = requests.post(self.base_url)
        result = response.json()
        self.assertEqual(result['error'], '令牌错误')
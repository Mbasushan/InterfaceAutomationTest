#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token
import testCase.crm.agent.base.registerBase as registerBase
import testCase.crm.agent.base.deleteBase as deleteBase

#注册代理商
class RegisterAgent(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/agent/register'

    def test_register(self):
        """注册代理商"""
        agent_id=registerBase.register(self)
        #删除注册
        deleteBase.delete_crm(str(agent_id))

    def test_register_noToken(self):
        """注册代理商---未登录"""
        params = {'access_token': "", 'name': '接口测试-代理商系统', 'contacts': '测试人员', 'mobile': '14655456'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '令牌错误')

    def test_register_noName(self):
        """注册代理商---未传代理商名称"""
        params = {'access_token': Token.get_token_login('sxs14','123456'), 'name': '','contacts': '测试人员', 'mobile': '14655456'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_register_noContacts(self):
        """注册代理商---未传联系人"""
        params = {'access_token': Token.get_token_login('sxs14','123456'), 'name': '接口测试-代理商系统','contacts': '', 'mobile': '14655456'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_register_noMobile(self):
        """注册代理商---未传联系人手机号"""
        params = {'access_token': Token.get_token_login('sxs14','123456'), 'name': '接口测试-代理商系统','contacts': '测试人员', 'mobile': ''}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_register_repeat(self):
        """注册代理商---重复注册"""
        for i in range(2):
            access_token=Token.get_token_login('sxs14','123456')
            params = {'access_token': access_token, 'name': '接口测试-代理商系统', 'contacts': '测试人员', 'mobile': '14655456'}
            response = requests.post(self.base_url, params)
            result = response.json()
            print(result)
            if i==1:
                self.assertEqual(result['error'],'已有申请')
        #查询id
        agent_id = registerBase.select()
        # 删除注册
        deleteBase.delete_crm(str(agent_id))

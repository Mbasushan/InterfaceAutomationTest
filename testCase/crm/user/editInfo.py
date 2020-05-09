#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token

#编辑个人信息
class EditInfo(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/user/editInfo'
        self.access_token=Token.getToken()

    def test_editInfo_nickname(self):
        """编辑个人信息-修改名称"""
        params={'access_token':self.access_token,'type':'nickname','value':'代理商昵称Sxs1'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')

    def test_editInfo_avatar(self):
        """编辑个人信息-修改头像"""
        # 以2进制方式打开图片
        with open('E:/脚本/InterfaceAutomationTest/image/1.png', "rb")as f_abs:
            body = {'value': ('1.jpg', f_abs, 'image/jpg')}
            data = {'access_token': self.access_token, "type": 'avata'}
            response = requests.post(self.base_url, data=data, files=body)
            text = response.json()
            print(text)
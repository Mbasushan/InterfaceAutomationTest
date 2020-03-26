#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import json
import unittest
import requests
import testCase.common.getToken as Token


#设置班级logo
class SetClassLogo(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/class/setClassLogo'
        self.access_token = Token.get_token_login('sxs14', '123456')

    def test_setClassLogo(self):
        """设置班级logo"""
        # 以2进制方式打开图片
        with open('E:/脚本/InterfaceAutomationTest/image/1.png', "rb")as f_abs:
            body = {'logo': ('1.jpg', f_abs, 'image/jpg')}
            params = {'access_token': self.access_token, 'class_id': 1079}
            response = requests.post(self.base_url, params, files=body)
            text = json.loads(response.text)
            print(text)
            self.assertEqual(len(text['data']),0)

    def test_setClassLogo_noToken(self):
        """设置班级logo---未登录"""
        # 以2进制方式打开图片
        with open('E:/脚本/InterfaceAutomationTest/image/1.png', "rb")as f_abs:
            body = {'logo': ('1.jpg', f_abs, 'image/jpg')}
            params = {'access_token': "", 'class_id': 1079}
            response = requests.post(self.base_url, params, files=body)
            text = json.loads(response.text)
            print(text)
            self.assertEqual(text['error'], '获取账号信息失败')

    def test_setClassLogo_noClassId(self):
        """设置班级logo---未传班级Id"""
        # 以2进制方式打开图片
        with open('E:/脚本/InterfaceAutomationTest/image/1.png', "rb")as f_abs:
            body = {'logo': ('1.jpg', f_abs, 'image/jpg')}
            params = {'access_token': self.access_token}
            response = requests.post(self.base_url, params, files=body)
            text = json.loads(response.text)
            print(text)
            self.assertEqual(text['error'], '参数错误')

    def test_setClassLogo_noLogo(self):
        """设置班级logo---未传logo图片"""
        # 以2进制方式打开图片
        with open('E:/脚本/InterfaceAutomationTest/image/1.png', "rb")as f_abs:
            #body = {'logo': ('1.jpg', f_abs, 'image/jpg')}
            params = {'access_token': self.access_token}
            response = requests.post(self.base_url, params)
            text = json.loads(response.text)
            print(text)
            self.assertEqual(text['error'], '参数错误')

    def test_setClassLogo_noJoinClass(self):
        """设置班级logo---不是该班级成员"""
        access_token = Token.get_token_login('苏珊15','123456')
        # 以2进制方式打开图片
        with open('E:/脚本/InterfaceAutomationTest/image/1.png', "rb")as f_abs:
            body = {'logo': ('1.jpg', f_abs, 'image/jpg')}
            params = {'access_token': access_token, 'class_id': 1079}
            response = requests.post(self.base_url, params, files=body)
            text = json.loads(response.text)
            print(text)
            #self.assertEqual(text['error'], '您没有权限进行操作')

    def test_setClassLogo_normal(self):
        """设置班级logo---普通成员"""
        access_token = Token.get_token_login('sxs15','123456')
        # 以2进制方式打开图片
        with open('E:/脚本/InterfaceAutomationTest/image/1.png', "rb")as f_abs:
            body = {'logo': ('1.jpg', f_abs, 'image/jpg')}
            params = {'access_token': access_token, 'class_id': 1079}
            response = requests.post(self.base_url, params, files=body)
            text = json.loads(response.text)
            print(text)
            #self.assertEqual(text, "{'data': {}}")
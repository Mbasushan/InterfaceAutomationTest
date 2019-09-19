#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import db_fixture.mysql_db as mySqlConnect

#设置班级成员权限
class SetClassManager(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/setClassManager"

    def test_setClassManager_admin(self):
        """设置班级成员权限---设置为管理员"""
        access_token = Token.getToken()
        params = {'access_token': access_token, 'class_id': 1000, 'set_user_id': 20061,'role':'admin'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        role=select_role()
        self.assertEqual('admin',role)

    def test_setClassManager_creator(self):
        """设置班级成员权限---移交创建者"""
        access_token = Token.getToken()
        params = {'access_token': access_token, 'class_id': 1000, 'set_user_id': 20061,'role':'creator'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        role=select_role()
        self.assertEqual('creator',role)
        #设置原来的用户为创建者
        token=Token.get_token_login('苏珊13','123456')
        response1 = requests.post(self.base_url, {'access_token': token, 'class_id': 1000, 'set_user_id': 20035,'role':'creator'})
        result1 = response1.json()
        print(result1)
        print("移交创建者成功")

    def test_setClassManager_normal(self):
        """设置班级成员权限---设置为普通成员"""
        access_token = Token.getToken()
        params = {'access_token': access_token, 'class_id': 1000, 'set_user_id': 20061,'role':'normal'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        role=select_role()
        self.assertEqual('normal',role)

    def test_setClassManager_nomalSet(self):
        """设置班级成员权限---普通成员设置权限"""
        access_token = Token.get_token_login('苏珊15','123456')
        params = {'access_token': access_token, 'class_id': 1000, 'set_user_id': 20061, 'role': 'normal'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'您没有权限进行操作')

    def test_setClassManager_noToken(self):
        """设置班级成员权限---未传token"""
        params = {'access_token': "", 'class_id': 1000, 'set_user_id': 20061, 'role': 'normal'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_setClassManager_noClassId(self):
        """设置班级成员权限---未传班级id"""
        access_token=Token.getToken()
        params = {'access_token': access_token, 'set_user_id': 20061, 'role': 'normal'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'没有找到班级')

    def test_setClassManager_noSetUserId(self):
        """设置班级成员权限---未成员id"""
        access_token=Token.getToken()
        params = {'access_token': access_token,'class_id':1000, 'role': 'normal'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_setClassManager_noRole(self):
        """设置班级成员权限---未传权限"""
        access_token=Token.getToken()
        params = {'access_token': access_token,'class_id':1000,'set_user_id': 20061}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

#查询
def select_role():
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "SELECT member_role FROM ketang_class_member WHERE member_user_id='20061' AND member_class_id=30"
    cs1.execute(query)
    isjoin = cs1.fetchall()
    return isjoin[0][0]
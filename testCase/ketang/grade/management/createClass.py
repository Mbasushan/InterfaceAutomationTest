#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import db_fixture.mysql_db as mySqlConnect

#申请创建班级
class CreateClass(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com//class/createClass"

    def test_createClass(self):
        """申请创建班级"""
        access_token=Token.getToken()
        params={"access_token":access_token,"name":'接口测试创建班级','contact':"测试",'mobile':'13106445986','organization':'测试创建班级-组织名称'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print("申请创建班级成功",result)
        class_id=select()
        self.assertNotEqual(class_id,0)

    def test_createClass_repeat(self):
        """申请创建班级---已存在申请中的班级"""
        access_token = Token.getToken()
        params = {"access_token": access_token, "name": '接口测试创建班级', 'contact': "测试", 'mobile': '13106445986','organization': '测试创建班级-组织名称'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'您已经有一个在申请中的班级')
        #删除该申请中的班级
        class_id = select()
        delete(str(class_id))

    def test_createClass_noToken(self):
        """申请创建班级---未传token"""
        params = {"access_token": "", "name": '接口测试创建班级', 'contact': "测试", 'mobile': '13106445986',
                  'organization': '测试创建班级-组织名称'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')

    def test_createClass_noName(self):
        """申请创建班级---未传name"""
        access_token=Token.getToken()
        params = {"access_token": access_token, 'contact': "测试", 'mobile': '13106445986',
                  'organization': '测试创建班级-组织名称'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_createClass_noContact(self):
        """申请创建班级---未传contact"""
        access_token=Token.getToken()
        params = {"access_token": access_token, 'name': "测试", 'mobile': '13106445986',
                  'organization': '测试创建班级-组织名称'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_createClass_noMobile(self):
        """申请创建班级---未传mobile"""
        access_token=Token.getToken()
        params = {"access_token": access_token, 'name': "测试", 'contact': '13106445986',
                  'organization': '测试创建班级-组织名称'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')


    def test_createClass_noOrganization(self):
        """申请创建班级---未传organization"""
        access_token=Token.getToken()
        params = {"access_token": access_token, 'name': "测试", 'mobile': '13106445986',
                  'contact': '测试创建班级'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')


#查询该申请的班级是否成功
def select():
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "SELECT class_id FROM ketang_class c JOIN ketang_class_member m ON c.`class_id`=m.`member_class_id` WHERE c.class_state = 'audit' AND  m.member_user_id = '20035' "
    cs1.execute(query)
    isjoin = cs1.fetchall()
    return isjoin[0][0]

#删除
def delete(classId):
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    #
    query = "DELETE FROM ketang_class WHERE class_id="+classId
    try:
        cs1.execute(query)
        conn.commit()
    except:
        conn.rollback()

    sql="DELETE FROM ketang_class_member WHERE member_class_id="+classId
    try:
        cs1.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    # 关闭cursor对象
    cs1.close()
    # 关闭connection对象
    conn.close()
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
        self.access_token=Token.get_token_login('sxs14','123456')

    def test_createClass(self):
        """申请创建班级"""
        params={"access_token":self.access_token,"name":'接口测试创建班级','contact':"测试",'mobile':'13106445986','organization':'测试创建班级-组织名称'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print("申请创建班级成功",result)
        key=result['class_key']
        class_id=select(key)
        self.assertNotEqual(class_id,0)
        #删除创建班级
        delete(str(class_id))

    # def test_createClass_repeat(self):
    #现在需求改为创建，班级直接通过，不用审核
    #     """申请创建班级---已存在申请中的班级"""
    #     access_token = Token.getToken()
    #     params = {"access_token": access_token, "name": '接口测试创建班级', 'contact': "测试", 'mobile': '13106445986','organization': '测试创建班级-组织名称'}
    #     response = requests.post(self.base_url, params)
    #     result = response.json()
    #     print(result)
    #     self.assertEqual(result['error'],'您已经有一个在申请中的班级')
    #     #删除该申请中的班级
    #     class_id = select()
    #     delete(str(class_id))

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
        params = {"access_token": self.access_token, 'contact': "测试", 'mobile': '13106445986',
                  'organization': '测试创建班级-组织名称'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_createClass_noContact(self):
        """申请创建班级---未传contact"""
        params = {"access_token": self.access_token, 'name': "测试", 'mobile': '13106445986',
                  'organization': '测试创建班级-组织名称'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_createClass_noMobile(self):
        """申请创建班级---未传mobile"""
        params = {"access_token": self.access_token, 'name': "测试", 'contact': '13106445986',
                  'organization': '测试创建班级-组织名称'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')


    def test_createClass_noOrganization(self):
        """申请创建班级---未传organization"""
        params = {"access_token": self.access_token, 'name': "测试", 'mobile': '13106445986',
                  'contact': '测试创建班级'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')


#查询该申请的班级是否成功
def select(key):
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "SELECT class_id FROM ketang_class where  class_key="+key
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
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as getToken
import db_fixture.mysql_db as mySqlConnect

#vip免费听
class Vipsignup(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/vipsignup/signup"

    def test_vipsingup_course(self):
        """课堂单课-vip免费听"""
        access_token=getToken.getToken()
        params={'item_type':'course','item_id':'8520014','access_token':access_token}
        response=requests.post(self.base_url,params)
        reslut=response.json()
        print(reslut)
        id='660'
        vs_id=get_vs_id(id)
        self.assertNotEqual(vs_id,0)
        #删除vip免费听表
        delete_vipsingup(str(vs_id))
        #删除报名表
        delete_course_singup(id)

    def test_vipsingup_column(self):
        """课堂专栏-vip免费听"""
        access_token=getToken.getToken()
        id = '258'
        params={'item_type':'column','item_id':id,'access_token':access_token}
        response=requests.post(self.base_url,params)
        reslut=response.json()
        print(reslut)
        vs_id = get_vs_id(id)
        self.assertNotEqual(vs_id, 0)
        # 删除vip免费听表
        delete_vipsingup(str(vs_id))
        # 删除报名表
        delete_course_singup(id)

    def test_vipsingup_package(self):
        """课堂课程包-vip免费听"""
        access_token=getToken.getToken()
        id='1002'
        params={'item_type':'package','item_id':id,'access_token':access_token}
        response=requests.post(self.base_url,params)
        reslut=response.json()
        print(reslut)
        vs_id = get_vs_id(id)
        self.assertNotEqual(vs_id, 0)
        # 删除vip免费听表
        delete_vipsingup(str(vs_id))
        # 删除报名表
        delete_course_singup(id)

    def test_vipsingup_course_noToke(self):
        """课堂单课-vip免费听:未传token"""
        params={'item_type':'course','item_id':'8520014'}
        response=requests.post(self.base_url,params)
        reslut=response.json()
        print(reslut)
        self.assertEqual(reslut['error'],'获取账号信息失败')

    def test_vipsingup_column_noToke(self):
        """课堂专栏-vip免费听:未传token"""
        params={'item_type':'column','item_id':'258'}
        response=requests.post(self.base_url,params)
        reslut=response.json()
        print(reslut)
        self.assertEqual(reslut['error'],'获取账号信息失败')

    def test_vipsingup_package_noToke(self):
        """课堂课程包-vip免费听:未传token"""
        params={'item_type':'package','item_id':'1002'}
        response=requests.post(self.base_url,params)
        reslut=response.json()
        print(reslut)
        self.assertEqual(reslut['error'],'获取账号信息失败')

    def test_vipsingup_course_noID(self):
        """课堂单课-vip免费听:未传单课id"""
        access_token = getToken.getToken()
        params={'item_type':'course','access_token':access_token}
        response=requests.post(self.base_url,params)
        reslut=response.json()
        print(reslut)
        self.assertEqual(reslut['error'],'该课程不符合条件')

    def test_vipsingup_column_noID(self):
        """课堂专栏-vip免费听:未传专栏id"""
        access_token = getToken.getToken()
        params={'item_type':'column','access_token':access_token}
        response=requests.post(self.base_url,params)
        reslut=response.json()
        print(reslut)
        self.assertEqual(reslut['error'],'该课程不符合条件')

    def test_vipsingup_package_noID(self):
        """课堂课程包-vip免费听:未传课程包id"""
        access_token = getToken.getToken()
        params = {'item_type': 'package', 'access_token': access_token}
        response = requests.post(self.base_url, params)
        reslut = response.json()
        print(reslut)
        self.assertEqual(reslut['error'], '该课程不符合条件')

    def test_vipsingup_course_noItem_type(self):
        """课堂单课-vip免费听:未传课程类型"""
        access_token = getToken.getToken()
        params={'item_id':'8520014','access_token':access_token}
        response=requests.post(self.base_url,params)
        reslut=response.json()
        print(reslut)
        self.assertEqual(reslut['error'],'该课程不符合条件')

    def test_vipsingup_column_noItem_type(self):
        """课堂专栏-vip免费听:未传专栏类型"""
        access_token = getToken.getToken()
        params={'item_id':'8520014','access_token':access_token}
        response=requests.post(self.base_url,params)
        reslut=response.json()
        print(reslut)
        self.assertEqual(reslut['error'],'该课程不符合条件')

    def test_vipsingup_package_noItem_type(self):
        """课堂专栏-vip免费听:未传专栏类型"""
        access_token = getToken.getToken()
        params = {'item_id': '8520014', 'access_token': access_token}
        response = requests.post(self.base_url, params)
        reslut = response.json()
        print(reslut)
        self.assertEqual(reslut['error'], '该课程不符合条件')

#查询数据库，获取id
def get_vs_id(id):
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "SELECT vs_id FROM ketang_vip_signup WHERE vs_user_id='20035' AND vs_item_id='"+id+"'"
    cs1.execute(query)
    vs_id = cs1.fetchone()[0]
    return vs_id

#删除vip免费听
def delete_vipsingup(id):
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "delete  FROM ketang_vip_signup WHERE vs_id='" + id + "'"
    try:
        cs1.execute(query)
        conn.commit()
    except:
        conn.rollback()
    # 关闭cursor对象
    cs1.close()
    # 关闭connection对象
    conn.close()

#删除报名表
def delete_course_singup(id):
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "delete  FROM ketang_course_signup WHERE signup_user_id = '20035' AND signup_course_id='" + id + "'"
    try:
        cs1.execute(query)
        conn.commit()
    except:
        conn.rollback()
    # 关闭cursor对象
    cs1.close()
    # 关闭connection对象
    conn.close()
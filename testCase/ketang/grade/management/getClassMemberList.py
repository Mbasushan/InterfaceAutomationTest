#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import unittest
import requests
import testCase.common.getToken as Token
import db_fixture.mysql_db as mySqlConnect

#获取班级成员列表
class GetClassMemberList(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/getClassMemberList"
        self.access_token = Token.get_token_login('sxs14', '123456')

    def test_getClassMemberList(self):
        """获取班级成员列表"""
        params={'access_token':self.access_token,'class_id':1079,"start":0,"num":10}
        response=requests.get(self.base_url,params)
        result=response.json()
        size=len(result['data']['member_list'])
        self.assertNotEqual(result['data'],'')
        #判断接口获取的数量与数据库获取的是否一致
        length=count()
        self.assertEqual(size,length)

    def test_getClassMemberList_noToken(self):
        """获取班级成员列表---未传token"""
        params={'access_token':"",'class_id':1079}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_getClassMemberList_noClassId(self):
        """获取班级成员列表---未传班级id"""
        params={'access_token':self.access_token}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'没有找到班级')


    def test_keyword(self):
        """获取班级成员列表---搜索关键词"""
        params = {'access_token': self.access_token,'class_id':1079,'keyword':'珊丫头'}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertNotEqual(result['data'],'')

    # def test_getClassMemberList_page(self):
    #     """获取班级成员列表---分页"""
    #     access_token = Token.getToken()
    #     length = count()
    #     size = math.ceil(length / 10)
    #     start = 0
    #     counts = 0
    #     for i in range(size):
    #         params = {'access_token': access_token, 'class_id': 1000, "start": start, "num": 10}
    #         response = requests.get(self.base_url, params)
    #         result = response.json()
    #         print(len(result['data']['member_list']))
    #         start = start + 10
    #         counts = len(result['data']['member_list']) + counts
    #     self.assertEqual(counts, length)

#获取数据库中的班级成员列表条数
def count():
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "SELECT COUNT(*) FROM ketang_class_member WHERE member_class_id='140' AND member_state='pass'"
    cs1.execute(query)
    length = cs1.fetchall()[0][0]
    return length
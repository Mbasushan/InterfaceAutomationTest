#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token
import db_fixture.mysql_db as mySqlConnect



#获取班级课程列表
class GetClassCourseList(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/class/getClassCourseList'

    def test_getClassCourseList(self):
        """获取班级课程列表"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':1000}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        size=len(result['data']['package_list'])+len(result['data']['course_list'])+len(result['data']['column_list'])
        count=countCourse()
        self.assertEqual(size,count)

    def test_getClassCourseList_noToken(self):
        """获取班级课程列表---未传token"""
        params={'access_token':"",'class_id':1000}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        size=len(result['data']['package_list'])+len(result['data']['course_list'])+len(result['data']['column_list'])
        count=countCourse()
        self.assertEqual(size,count)

    def test_getClassCourseList_noClassID(self):
        """获取班级课程列表---未传clasId"""
        access_token=Token.getToken()
        params={'access_token':access_token}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

#查询数据库中课程数
def countCourse():
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "SELECT COUNT(*) FROM ketang_class_course WHERE cc_class_id=30"
    cs1.execute(query)
    result = cs1.fetchall()[0][0]
    return result
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import db_fixture.mysql_db as mySqlConnect


#提交评价
class Subcourseevaluate(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/courseevaluate/sub"
        self.accsee_token = Token.getToken()

    def test_sub(self):
        """提交评价"""
        # 提交前如果有评价，先删除评价
        delete(self)
        #评价内容
        comment='接口测试评价内容、接口测试评价内容'
        params={'itemType':'cloumn','itemId':89,'access_token':self.accsee_token,'teacherScore':5,'courseScore':5,'learnScore':5,'comment':comment}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')
        #提交评价成功后删除评价
        delete(self)

    def test_sub_noType(self):
        """提交评价-未传课程类型"""
        # 提交前如果有评价，先删除评价
        delete(self)
        #评价内容
        comment='接口测试评价内容、接口测试评价内容'
        params={'itemType':'','itemId':89,'access_token':self.accsee_token,'teacherScore':5,'courseScore':5,'learnScore':5,'comment':comment}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'课程未指定')

    def test_sub_noId(self):
        """提交评价-未传课程id"""
        # 提交前如果有评价，先删除评价
        delete(self)
        #评价内容
        comment='接口测试评价内容、接口测试评价内容'
        params={'itemType':'column','itemId':'','access_token':self.accsee_token,'teacherScore':5,'courseScore':5,'learnScore':5,'comment':comment}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'课程未指定')

    def test_sub_noToken(self):
        """提交评价-未传token"""
        # 提交前如果有评价，先删除评价
        delete(self)
        #评价内容
        comment='接口测试评价内容、接口测试评价内容'
        params={'itemType':'column','itemId':89,'access_token':'','teacherScore':5,'courseScore':5,'learnScore':5,'comment':comment}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_sub_noTeacherScore(self):
        """提交评价-未传教师授课得分"""
        # 提交前如果有评价，先删除评价
        delete(self)
        #评价内容
        comment='接口测试评价内容、接口测试评价内容'
        params={'itemType':'column','itemId':89,'access_token':self.accsee_token,'teacherScore':'','courseScore':5,'learnScore':5,'comment':comment}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '评分选未提交完整')

    def test_sub_noCourseScore(self):
        """提交评价-未传课程内容得分 """
        # 提交前如果有评价，先删除评价
        delete(self)
        #评价内容
        comment='接口测试评价内容、接口测试评价内容'
        params={'itemType':'column','itemId':89,'access_token':self.accsee_token,'teacherScore':'5','courseScore':'','learnScore':5,'comment':comment}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '评分选未提交完整')


    def test_sub_noLearnScore(self):
        """提交评价-未传学习收获得分 """
        # 提交前如果有评价，先删除评价
        delete(self)
        #评价内容
        comment='接口测试评价内容、接口测试评价内容'
        params={'itemType':'column','itemId':89,'access_token':self.accsee_token,'teacherScore':'5','courseScore':'5','learnScore':'','comment':comment}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '评分选未提交完整')

    def test_sub_noComment(self):
        """提交评价-未传评价内容 """
        # 提交前如果有评价，先删除评价
        delete(self)
        #评价内容
        comment='接口测试评价内容、接口测试评价内容'
        params={'itemType':'column','itemId':89,'access_token':self.accsee_token,'teacherScore':'5','courseScore':'5','learnScore':'5','comment':''}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '评价内容未提交')

#删除评价
def delete(self):
     # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "DELETE FROM ketang_course_evaluate WHERE evaluate_item_id =89 and evaluate_user_id=20035"
    try:
        cs1.execute(query)
        conn.commit()
    except:
        conn.rollback()
    # 关闭cursor对象
    cs1.close()
    # 关闭connection对象
    conn.close()
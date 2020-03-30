#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import db_fixture.mysql_db as mySqlConnect

#评论 点赞
class ClickLike(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/api/ClickLike"
        self.access_token = Token.get_token_login('sxs14', '123456')

    def test_clickLike(self):
        """点赞评论"""
        #创建评论
        params = {'id': 8526372, 'comment': '接口测试评论', 'access_token': self.access_token}
        response = requests.post('http://ke.test.mbalib.com/api/AddComment', params)
        result1 = response.json()
        print(result1)
        id=select('698','20271')
        #点赞评论
        params={'type':'comment','id':id,'access_token':self.access_token}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')
        #删除评论
        delete_comment(str(id))

    def test_clickLike_repeat(self):
        """重复点赞评论"""
        # 创建评论
        params = {'id': 8526372, 'comment': '接口测试评论', 'access_token':Token.get_token_login('Sxs15','123456')}
        response = requests.post('http://ke.test.mbalib.com/api/AddComment', params)
        result1 = response.json()
        print(result1)
        id = select('698','20314')
        # 点赞评论
        for i in range(2):
            params = {'type': 'comment', 'id': id, 'access_token': self.access_token}
            response = requests.post(self.base_url, params)
            result = response.json()
            if i==1:
                print(result)
                self.assertEqual(result['error'],'已经赞过了')
        #删除评论
        delete_comment(str(id))

    def test_clickLike_noToken(self):
        """点赞评论---未登录"""
        params={'type':'comment','id':35}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_clickLike_noId(self):
        """点赞评论---未传评论id"""
        params={'type':'comment','access_token':self.access_token}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

#查询
def select(id,userId):
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "SELECT comment_id FROM ketang_course_comment WHERE comment_course_id="+id+" and comment_user_id="+userId
    cs1.execute(query)
    result = cs1.fetchall()[0][0]
    return result

#删除评论
def delete_comment(id):
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "delete FROM ketang_course_comment WHERE comment_id='"+id+"'"
    try:
        cs1.execute(query)
        conn.commit()
    except:
        conn.rollback()
    # 关闭cursor对象
    cs1.close()
    # 关闭connection对象
    conn.close()
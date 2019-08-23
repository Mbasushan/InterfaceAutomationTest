#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import db_fixture.mysql_db as mySqlConnect

#百科大咖投票
class WikiVote(unittest.TestCase):

    def setUp(self):
        self.base_url="http://www.test.mbalib.com/appwiki/WikiVote"

    def test_vikiVote(self):
        """百科大咖投票"""
        ids='4,7'
        page_name= "七层次领导力"
        count=isVote(page_name,ids)
        if count!=0:
            delete(page_name,ids)
        params = {"num": 6, 'page_name':page_name, "teacher_ids":ids}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result['data'])
        self.assertEqual(result['state'], 'success')
        #判断投票是否成功
        vote=isVote(page_name,ids)
        self.assertNotEqual(vote,0)

    def test_vikiVote_repeat(self):
        """百科大咖投票-重复投票不重复计算"""
        ids='4,7'
        page_name= "七层次领导力"
        count=isVote(page_name,ids)
        if count!=0:
            params = {"num": 6, 'page_name':page_name, "teacher_ids":ids}
            response = requests.get(self.base_url, params)
            result = response.json()
            print(result['data'])
            self.assertEqual(result['state'], 'success')
            #判断投票是否成功
            vote=isVote(page_name,ids)
            self.assertEqual(vote,count)
        else:
            print("未投票过")

    def test_vikiVote_noTeacherId(self):
        """百科大咖投票-未选择大咖投票，返回投票结果"""
        ids=''
        page_name= "七层次领导力"
        params = {"num": 6, 'page_name':page_name, "teacher_ids":ids}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result['data'])
        self.assertEqual(result['state'], 'success')

    def test_vikiVote_noPageName(self):
        """百科大咖投票-未传条目名，返回投票结果"""
        ids='4'
        page_name= ""
        params = {"num": 6, 'page_name':page_name, "teacher_ids":ids}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result['data'])
        self.assertEqual(result['state'], 'success')

#查询是否已经投票过
def isVote(pageName,ids):
    ids=ids.replace(',',"','")
    #连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "SELECT count(*) FROM wiki_vote where vote_page_name='"+pageName+"' and vote_user_id=0 and vote_teacher_id in ('"+ids+"')"
    cs1.execute(query)
    count = cs1.fetchall()[0][0]
    return count

#删除
def delete(pageName,ids):
    ids = ids.replace(',', "','")
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "delete FROM wiki_vote where vote_page_name='" + pageName + "' and vote_user_id=0 and vote_teacher_id in ('" + ids + "')"
    try:
        cs1.execute(query)
        conn.commit()
    except:
        conn.rollback()
    # 关闭cursor对象
    cs1.close()
    # 关闭connection对象
    conn.close()
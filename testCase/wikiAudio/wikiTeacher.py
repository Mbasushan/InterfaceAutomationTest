#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import db_fixture.mysql_db as mySqlConnect

#随机获取百科大咖列表
class WikiTeacher(unittest.TestCase):

    def setUp(self):
        self.base_url="http://www.test.mbalib.com/appwiki/WikiTeacher"

    def test_getWikiTeacher(self):
        """随机获取百科大咖列表"""
        params={"num":10,'page_name':"七层次领导力","sort":0}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result['data'])
        self.assertEqual(result['state'],'success')

    def test_getWikiTeacher_sort(self):
        """随机获取百科大咖列表-按热度排序"""
        params={"num":6,'page_name':"七层次领导力","sort":1}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result['data'])
        self.assertEqual(result['state'],'success')
        size=len(result['data'])
        for i in range(size):
            self.assertIsNotNone(result['data'][i]['vote'])
            print("教师名字：",result['data'][i]['teacher_name'],",投票数为：",result['data'][i]['vote'])


    def test_getWikiTeacher_noPageName(self):
        """随机获取百科大咖列表-未传条目名-排序值为true无用"""
        params={"num":6,"sort":1}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result['data'])
        self.assertEqual(result['state'],'success')
        size=len(result['data'])
        for i in range(size):
            self.assertIsNotNone(result['data'][i]['vote'])
            print("教师名字：",result['data'][i]['teacher_name'],",投票数为：",result['data'][i]['vote'])


    def test_getWikiTeacher_NoNum(self):
        """随机获取百科大咖列表-未传返回大咖数量值，返回数量默认为6条"""
        params={'page_name':"七层次领导力","sort":0}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result['data'])
        self.assertEqual(result['state'],'success')
        size=select_num()
        print("总条数：", size)
        if size >6:
            self.assertEqual(len(result['data']),6)
        else:
            self.assertEqual(len(result['data']),size)


#查询数据库中总的大咖数
def  select_num():
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "SELECT count(*) FROM wiki_teacher"
    cs1.execute(query)
    count = cs1.fetchall()[0][0]
    return count
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import db_fixture.mysql_db as mySqlConnect

#入口的大咖场景列表
class SceneList(unittest.TestCase):

    def setUp(self):
        self.base_url='http://www.test.mbalib.com/appaudio/scene'

    def test_sceneList(self):
        """大咖场景列表"""
        response=requests.get(self.base_url)
        result=response.json()
        print("大咖场景数量：",len(result['data']))
        size=select_num()
        print("数据库中场景数量为：",size)
        self.assertEqual(len(result['data']),size)

def select_num():
    #查询数据中大咖场景数量
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "SELECT count(*) FROM wiki_audio_scene WHERE as_show=1"
    cs1.execute(query)
    count= cs1.fetchall()[0][0]
    return count
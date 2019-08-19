#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest

import requests

import db_fixture.mysql_db as mySqlConnect
#主题列表

class ThemeList(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/theme/getcontent"

    def test_category(self):
        """课堂首页分类入口"""
        data = list("entrance")
        if len(data)==0:
            # 连接数据库
            conn = mySqlConnect.my_db()
            # 获取cursor对象
            cs1 = conn.cursor()
            # 查询主题信息
            query = "update  ketang_theme set theme_state='enable' WHERE theme_key='entrance'"
            try:
                cs1.execute(query)
                conn.commit()
            except:
                conn.rollback()
            # 关闭cursor对象
            cs1.close()
            # 关闭connection对象
            conn.close()
        response = requests.get(self.base_url,params={"key":"entrance","purge":"ture"})
        result = response.json()
        print("结果：", result['data'])

    def test_01_category_null(self):
        """课堂首页分类入口-无数据"""
        data=list("entrance")
        if len(data)!=0:
            # 连接数据库
            conn = mySqlConnect.my_db()
            # 获取cursor对象
            cs1 = conn.cursor()
            # 查询主题信息
            query = "update  ketang_theme set theme_state='disable' WHERE theme_key='entrance'"
            try:
                cs1.execute(query)
                conn.commit()
            except:
                conn.rollback()
            # 关闭cursor对象
            cs1.close()
            # 关闭connection对象
            conn.close()
        response = requests.get(self.base_url, params={"key":"entrance","purge":"ture"})
        result = response.json()
        print("结果：", result['data'])
        self.assertEqual(len(result['data']), 0)

    def test_stage(self):
        """课堂首页学习阶梯入口-有数据"""
        data = list("stage")
        if len(data) == 0:
            # 连接数据库
            conn = mySqlConnect.my_db()
            # 获取cursor对象
            cs1 = conn.cursor()
            # 查询主题信息
            query = "update  ketang_theme set theme_state='enable' WHERE theme_key='stage'"
            try:
                cs1.execute(query)
                conn.commit()
            except:
                conn.rollback()
            # 关闭cursor对象
            cs1.close()
            # 关闭connection对象
            conn.close()
        response = requests.get(self.base_url, params={"key": "stage", "purge": "ture"})
        result = response.json()
        print("结果：", result['data'])

    def test_01_stage_null(self):
        """课堂首页学习阶梯入口-无数据"""
        data = list("stage")
        if len(data) != 0:
            # 连接数据库
            conn = mySqlConnect.my_db()
            # 获取cursor对象
            cs1 = conn.cursor()
            # 查询主题信息
            query = "update  ketang_theme set theme_state='disable' WHERE theme_key='stage'"
            try:
                cs1.execute(query)
                conn.commit()
            except:
                conn.rollback()
            # 关闭cursor对象
            cs1.close()
            # 关闭connection对象
            conn.close()
        response = requests.get(self.base_url, params={"key": "stage", "purge": "ture"})
        result = response.json()
        print("结果：", result['data'])
        self.assertEqual(len(result['data']), 0)


    def test_scene(self):
        """课堂首页主题场景列表-有数据"""
        data = list("scene")
        if len(data) == 0:
            # 连接数据库
            conn = mySqlConnect.my_db()
            # 获取cursor对象
            cs1 = conn.cursor()
            # 查询主题信息
            query = "update  ketang_theme set theme_state='enable' WHERE theme_key like 'scene%'"
            try:
                cs1.execute(query)
                conn.commit()
            except:
                conn.rollback()
            # 关闭cursor对象
            cs1.close()
            # 关闭connection对象
            conn.close()
        size=len(data)
        print("总的主题场景数：",size)
        url='http://ke.test.mbalib.com/theme/getscene'
        response = requests.get(url, params={"purge": "ture"})
        result = response.json()
        print("结果：", result['data'])

#查询
def list(theme_key):
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    if theme_key!='scene':
        query = "SELECT * FROM ketang_theme WHERE theme_key='"+theme_key+"' and theme_state='enable'"
    else:
        query="SELECT * FROM ketang_theme WHERE theme_key like 'scene%' and theme_state='enable'"
    cs1.execute(query)
    data = cs1.fetchall()
    return data

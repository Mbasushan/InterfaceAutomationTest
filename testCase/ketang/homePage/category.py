#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#获取分类
import unittest
import requests

class Category(unittest.TestCase):

    def test_getCategory(self):
        """课堂首页获取分类数据"""
        response = requests.post("http://ke.test.mbalib.com/theme/getcontent",params={'key':"entrance"})
        result = response.json()
        print(result['data'])

    def test_gerCategory_courseList(self):
        """课堂首页对应分类的课程列表"""
        """课堂首页获取分类数据"""
        url="http://ke.test.mbalib.com/list/GetCategoryCourse"
        #获取所有分类的id
        response = requests.post("http://ke.test.mbalib.com/theme/getcontent", params={'key': "entrance"})
        result = response.json()
        idList = ""
        nameList=''
        for i in range(len(result['data'])):
            tids=result['data'][i]['data']
            if len(result['data'][i]['data'])!=0:
                idList=idList+","+tids['tid']
                nameList = nameList+","+result['data'][i]['title']
        cid=idList.split(',')[1:]
        name=nameList.split(',')[1:]
        for x in range(len(cid)):
            category_id=cid[x]
            title=name[x]
            params={"category_id":category_id,"start":0,"num":10}
            response = requests.post(url,params)
            result = response.json()
            print("分类id："+category_id+",分类标题："+title+"，课程总数：",len(result['data']))
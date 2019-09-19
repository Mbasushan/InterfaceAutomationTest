#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import json
import requests
import testCase.common.getToken as Token
import db_fixture.mysql_db as mySqlConnect

def delete_course(self):
    url='http://ke.test.mbalib.com/class/delCourse'
    list=json.dumps(selece_courseId())
    access_token=Token.getToken()
    params={'access_token':access_token,'class_id':1002,'cc_list':list}
    response=requests.post(url,params)
    result=response.json()
    print(result)
    self.assertEqual(len(result['data']),0)

#查询课程id
def selece_courseId():
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "SELECT cc_id FROM ketang_class_course WHERE cc_class_id=41"
    cs1.execute(query)
    result = cs1.fetchall()
    list = []
    for row in result:
        list.append(row[0])
    print(list)
    return list
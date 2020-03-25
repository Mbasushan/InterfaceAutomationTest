#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import testCase.common.getToken as Token
import db_fixture.mysql_db as mySqlConnect

# 获取分组列表
def getGroupList(self,access_token):
    url='http://ke.test.mbalib.com/class/getGroupList'
    params = {'access_token': access_token, 'class_id': 1003}
    response = requests.get(url, params)
    result = response.json()
    print(result)
    count = select()
    print("分组数量：", count)
    self.assertEqual(len(result['data']['group_list']), count)
    return result['data']['group_list']

#查询
def select():
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "SELECT count(*) FROM ketang_class_group WHERE group_class_id=43"
    cs1.execute(query)
    result = cs1.fetchall()[0][0]
    return result
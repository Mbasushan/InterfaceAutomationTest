#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import testCase.common.getToken as Token
import db_fixture.mysql_db as mySqlConnect

#添加成员
def add_member(self,access_token):
    url = 'http://crm.test.mbalib.com/member/addMembers'
    response = requests.post(url, params={'access_token': access_token,'mobiles':'17359262064'})
    result = response.json()
    print(result)
    #查找该成员的成员id
    id=selectId('17359262064')
    return id

#查找是否加入班级
def selectId(mobiles):
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "SELECT member_id FROM crm_member WHERE member_mobile="+mobiles+" AND member_agent_id=97"
    cs1.execute(query)
    Id = cs1.fetchall()
    if "," in str(Id):
        Id = Id[0][0]
        print(Id)
    return Id
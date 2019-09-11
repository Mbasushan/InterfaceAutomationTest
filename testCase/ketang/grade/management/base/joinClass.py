#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import testCase.common.getToken as Token
import db_fixture.mysql_db as mySqlConnect

def join_class(self):
    url='http://ke.test.mbalib.com//class/applyJoinClass'
    access_token = Token.get_token_login('苏珊11', '123456')
    params = {'access_token': access_token, 'class_id': '1003'}
    flag = isJoin()
    if flag:
        print("已加入班级")
        # 删除该条数据
        delete()
    response = requests.post(url, params)
    result = response.json()
    print(result)
    self.assertEqual(len(result['data']), 0)

#查找是否加入班级
def isJoin():
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "SELECT member_state FROM ketang_class_member WHERE member_user_id='20059' AND member_class_id=43"
    cs1.execute(query)
    isjoin = cs1.fetchall()
    print(isjoin)
    if "," in str(isjoin):
        isjoin = isjoin[0][0]
        print(isjoin)
        if isjoin == 'pass':
            return True
        else:
            return False
    else:
        return False

#删除已加入班级的数据
def delete():
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "delete FROM ketang_class_member WHERE member_user_id='20059' AND member_class_id=43"
    try:
        cs1.execute(query)
        conn.commit()
    except:
        conn.rollback()
    # 关闭cursor对象
    cs1.close()
    # 关闭connection对象
    conn.close()
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import testCase.common.getToken as Token
import db_fixture.mysql_db as mySqlConnect

#删除成员
def delete_member(self,member_id):
    url='http://crm.test.mbalib.com/member/deleteMember'
    access_token=Token.getToken()
    response=requests.post(url,params={'access_token':access_token,'member_id':member_id})
    result=response.json()
    print(result)
    self.assertEqual(result['state'], 'success')
    #删除数据
    delete(str(member_id))

def delete(member_id):
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "delete FROM crm_member WHERE member_id="+member_id
    try:
        cs1.execute(query)
        conn.commit()
    except:
        conn.rollback()
    # 关闭cursor对象
    cs1.close()
    # 关闭connection对象
    conn.close()
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import testCase.common.getToken as Token
import db_fixture.mysql_db as mySqlConnect


#注册代理商
def register(self):
    url='http://crm.test.mbalib.com/agent/register'
    access_token=Token.get_token_login('sxs14','123456')
    params={'access_token':access_token,'name':'接口测试-代理商系统','contacts':'测试人员','mobile':'14655456'}
    response=requests.post(url,params)
    result=response.json()
    print(result)
    self.assertEqual(result['state'], 'success')
    #查询数据库返回代理商id
    agent_id=select()
    return agent_id

#查询
def select():
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    sql = "select agent_id FROM crm_agent WHERE agent_name='接口测试-代理商系统'"
    cs1.execute(sql)
    agent_id = cs1.fetchone()[0]
    return agent_id
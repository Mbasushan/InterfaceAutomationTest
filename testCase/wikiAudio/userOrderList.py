#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as getToken
import db_fixture.mysql_db as mySqlConnect

#用户大咖讲百科-订单列表
class UserOrderList(unittest.TestCase):

    def setUp(self):
        self.base_url='http://www.test.mbalib.com/appaudio/userorder'

    def test_getWikiOrderLisst(self):
        """用户大咖讲百科-订单列表"""
        access_token=getToken.getToken()
        params={"access_token":access_token}
        response=requests.get(self.base_url,params)
        result=response.json()
        size=getCount()
        print("数据库中总条数：",size)
        if size <=20:
            self.assertEqual(len(result['data']),size)
        else:
            self.assertEqual(len(result['data']),20)


    def test_getWikiOrderLisst_noToken(self):
        """用户大咖讲百科-订单列表-未传access_token"""
        params={"access_token":""}
        response=requests.get(self.base_url,params)
        result=response.json()
        self.assertEqual(len(result['data']),0)

#获取该用户在数据库中的大咖订单总数
def getCount():
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "SELECT count(*) FROM mbalib_order WHERE order_user_id='6191349' AND order_state='paid' AND order_event_type LIKE 'audio%'"
    cs1.execute(query)
    count = cs1.fetchall()[0][0]
    return count
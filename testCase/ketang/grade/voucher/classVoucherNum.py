#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import testCase.common.getTime as getTime
import db_fixture.mysql_db as mySqlConnect

#班级优惠券数量
class GetVoucher(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/classVoucherNum"

    def test_classVoucherNum(self):
        """班级优惠券数量"""
        access_token=Token.getToken()
        params={'access_token':access_token,'class_id':1000}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        #查询数据库获取数量
        count=select_data()
        self.assertEqual(result['data']['voucher_num'],count)

#查询
def select_data():
    time=getTime.now_time('%Y%m%d%H%M%S')
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "SELECT COUNT(*) FROM ketang_voucher WHERE voucher_number <> voucher_used_number AND voucher_class_id = 30 AND voucher_endtime >='"+time+"'"
    cs1.execute(query)
    count1 = cs1.fetchall()[0][0]
    sql = "SELECT COUNT(*) FROM ketang_voucher WHERE voucher_number <> voucher_used_number AND voucher_class_id = 30 AND voucher_endtime =''"
    cs1.execute(sql)
    count2 = cs1.fetchall()[0][0]
    count=count1+count2
    return count
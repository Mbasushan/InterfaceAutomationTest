#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import db_fixture.mysql_db as mySqlConnect

#修改用户信息
class UserEdit(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/api/UserEdit"

    def test_edit_rname(self):
        """修改用户信息---名称"""
        access_token=Token.get_token_login('sxs14','123456')
        params={'access_token':access_token,'rname':'修改名称'}
        respsonse=requests.post(self.base_url,params)
        #查询数据
        rname=select('data_real_name')
        self.assertEqual(rname,'修改名称')
        #删除数据
        delete_comment()

    def test_edit_job(self):
        """修改用户信息---职务"""
        access_token = Token.get_token_login('sxs14', '123456')
        params = {'access_token': access_token, 'rname': '测试'}
        respsonse = requests.post(self.base_url, params)
        # 查询数据
        rname = select('data_position')
        self.assertEqual(rname, '测试')
        # 删除数据
        delete_comment()

    def test_edit_company(self):
        """修改用户信息---企业"""
        access_token = Token.get_token_login('sxs14', '123456')
        params = {'access_token': access_token, 'company': 'MBA'}
        respsonse = requests.post(self.base_url, params)
        # 查询数据
        rname = select('data_company')
        self.assertEqual(rname, 'MBA')
        # 删除数据
        delete_comment()

    def test_edit_area(self):
        """修改用户信息---地区"""
        access_token = Token.get_token_login('sxs14', '123456')
        params = {'access_token': access_token, 'area': '350000,350200,350203'}
        respsonse = requests.post(self.base_url, params)
        # 查询数据
        rname = select('data_province,data_city,data_country')
        self.assertEqual(rname, '350000,350200,350203')
        # 删除数据
        delete_comment()

    def test_edit_noParams(self):
        """修改用户信息---未传参数"""
        access_token = Token.get_token_login('sxs14', '123456')
        params = {'access_token': access_token}
        respsonse = requests.post(self.base_url, params)
        result=respsonse.json()
        self.assertEqual(result['error'], '参数错误')

    def test_edit_noToken(self):
        """修改用户信息---未登录"""
        params = {'access_token': ''}
        respsonse = requests.post(self.base_url, params)
        result=respsonse.json()
        self.assertEqual(result['error'], '获取账号信息失败')

#查询
def select(params):
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "SELECT "+params+" FROM mbalib_user_data WHERE data_user_id='6191496'"
    cs1.execute(query)
    results = cs1.fetchall()
    print(cs1.fetchone())
    for row in results:
        province = row[0]
        city = row[1]
        country = row[2]
    result=province+','+city+','+country
    return result

#删除数据
def delete_comment():
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "delete FROM mbalib_user_data WHERE data_user_id='6191496'"
    try:
        cs1.execute(query)
        conn.commit()
    except:
        conn.rollback()
    # 关闭cursor对象
    cs1.close()
    # 关闭connection对象
    conn.close()
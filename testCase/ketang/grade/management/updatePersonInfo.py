#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import db_fixture.mysql_db as mySqlConnect


#修改个人信息
class UpdatePersonInfo(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/updatePersonInfo"

    def test_updatePersonInfo(self):
        """修改个人信息---修改姓名"""
        access_token = Token.getToken()
        name = 'Sxs1'
        params = {'access_token': access_token, 'class_id': '1000', 'nickname': name}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)



    def test_updatePersonInfo_name(self):
        """修改个人信息---修改姓名"""
        access_token = Token.getToken()
        name = '苏珊'
        params = {'access_token': access_token, 'class_id': '1000', 'name': name}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        nickname = select_data('data_real_name')
        self.assertEqual(nickname, name)
        #删除
        delete()

    def test_updatePersonInfo_company(self):
        """修改个人信息---修改企业"""
        access_token = Token.getToken()
        company = 'MBA'
        params = {'access_token': access_token, 'class_id': '1000', 'company': company}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        data_company = select_data('data_company')
        self.assertEqual(data_company, company)
        #删除
        delete()

    def test_updatePersonInfo_job(self):
        """修改个人信息---修改岗位"""
        access_token = Token.getToken()
        job = '测试'
        params = {'access_token': access_token, 'class_id': '1000', 'job': job}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        data_position = select_data('data_position')
        self.assertEqual(data_position, job)
        #删除
        delete()

    def test_updatePersonInfo_noToken(self):
        """修改个人信息---未传token"""
        params = {'access_token': "", 'class_id': '1000', 'nickname': "Sxs1"}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_updatePersonInfo_noClassId(self):
        """修改个人信息---未传classId"""
        access_token = Token.getToken()
        params = {'access_token': access_token, 'nickname': "Sxs1"}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_updatePersonInfo_noParams(self):
        """修改个人信息---未传参数"""
        access_token = Token.getToken()
        params = {'access_token': access_token, 'class_id': "1000"}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(len(result['data']), 0)

#查询
def select_data(params):
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "SELECT "+params+" FROM mbalib_user_data WHERE data_user_id='6191349'"
    cs1.execute(query)
    result = cs1.fetchall()[0][0]
    return result

#删除已加入班级的数据
def delete():
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "delete FROM mbalib_user_data WHERE data_user_id='6191349'"
    try:
        cs1.execute(query)
        conn.commit()
    except:
        conn.rollback()
    # 关闭cursor对象
    cs1.close()
    # 关闭connection对象
    conn.close()
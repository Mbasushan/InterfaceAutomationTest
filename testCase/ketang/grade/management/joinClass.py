#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import db_fixture.mysql_db as mySqlConnect
import testCase.ketang.grade.management.base.joinClass as joinClass

#申请加入班级
class JoinClass(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com//class/applyJoinClass"
        self.access_token = Token.get_token_login('sxs14', '123456')

    def test_joinClass(self):
        """申请加入班级"""
        joinClass.join_class(self)


    def test_joinClass_joining(self):
        """申请加入班级--已申请"""
        access_token = Token.get_token_login('sxs16', '123456')
        params = {'access_token': access_token, 'class_id': '1079'}
        flag = isJoin('20059','43')
        if flag:
            print("已加入班级")
        else:
            response1 = requests.post(self.base_url, params)
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '您已申请加入班级或已是班级成员')


    def test_joinClass_joined(self):
        """申请加入班级--已是班级成员"""
        params = {'access_token': self.access_token, 'class_id': '1079'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '您已申请加入班级或已是班级成员')

    def test_joinClass_NoClass(self):
        """申请加入班级--未传classId"""
        access_token = Token.get_token_login('苏珊11', '123456')
        params = {'access_token': access_token, 'class_id': ''}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_joinClass_remark(self):
        """申请加入班级-填写备注"""
        access_token = Token.get_token_login('sxs16', '123456')
        params = {'access_token': access_token, 'class_id': '1079','remark':'备注'}
        flag = isJoin('20392','140')
        if flag:
            print("已加入班级")
            # 删除该条数据
            delete()
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(len(result['data']), 0)

#查找是否加入班级
def isJoin(userId,classId):
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "SELECT member_state FROM ketang_class_member WHERE member_user_id='"+userId+"' AND member_class_id='"+classId+"'"
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
    query = "delete FROM ketang_class_member WHERE member_user_id='20392' AND member_class_id=140"
    try:
        cs1.execute(query)
        conn.commit()
    except:
        conn.rollback()
    # 关闭cursor对象
    cs1.close()
    # 关闭connection对象
    conn.close()
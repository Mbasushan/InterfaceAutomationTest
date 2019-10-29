#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import db_fixture.mysql_db as mySqlConnect
import testCase.crm.member.base.delMemberBase as delMemberBase


#加入代理商申请
class MemberApply(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/agent/memberApply'

    def test_memberApply(self):
        """加入代理商申请"""
        access_token=Token.get_token_login('sxs14','123456')
        params={'access_token':access_token,'id':'32'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['state'],'success')
        #删除
        member_id=select()
        print(member_id)
        delete(str(member_id))

    def test_memberApply_noToken(self):
        """加入代理商申请---未登录"""
        params = {'access_token': "", 'id': '32'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '令牌错误')

    def test_memberApply_noId(self):
        """加入代理商申请---未传代理商id"""
        access_token=Token.get_token_login('sxs14','123456')
        params = {'access_token': access_token, 'id': ''}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_memberApply_repeat(self):
        """加入代理商申请---重复申请"""
        for i in range(2):
            access_token = Token.get_token_login('sxs14', '123456')
            params = {'access_token': access_token, 'id': '32'}
            response = requests.post(self.base_url, params)
            result = response.json()
            print(result)
            if i==1:
                self.assertEqual(result['error'], '已有申请')
        # 删除
        member_id = select()
        print(member_id)
        delete(str(member_id))


#查询获取 成员id
def select():
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    sql = "select member_id FROM crm_member WHERE member_user_name='M_id_2a431885c9d690006e355b5cfdbcc93d' and member_agent_id='32'"
    cs1.execute(sql)
    member_id = cs1.fetchone()[0]
    return member_id

def delete(memberId):
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "delete FROM crm_member WHERE member_id='" + memberId + "'"
    try:
        cs1.execute(query)
        conn.commit()
    except:
        conn.rollback()

        # 查询主题信息
    sql = "delete FROM crm_member_apply WHERE apply_member_id='" + memberId + "'"
    try:
        cs1.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    # 关闭cursor对象
    cs1.close()
    # 关闭connection对象
    conn.close()
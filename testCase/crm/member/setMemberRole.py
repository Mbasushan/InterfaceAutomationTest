#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token
import testCase.crm.member.base.getMemberList as getMemberList
import db_fixture.mysql_db as mySqlConnect

#设置成员角色
class SetMemberRole(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/member/setMemberRole'
        self.access_token=Token.getToken()

    def test_setRole_creator(self):
        """设置成员角色-创建者设置成员角色"""
        #获取成员列表
        list=getMemberList.get_member_list(self,self.access_token)
        if len(list)!=0:
            i=0
            for i in range(len(list)):
                id=list[i]['member_id']
                oldRole=selectSole(id)
                role=''
                if oldRole=='creator':
                    print('该成员的角色是【创建者】，设置为【管理员】')
                    role='admin'
                elif oldRole=='admin':
                    print('该成员的角色是【管理员】，设置为【普通成员】')
                    role = 'normal'
                elif oldRole=='normal':
                    print('该成员的角色是【普通成员】,设置为【管理员】')
                    role = 'admin'
                params={'access_token':self.access_token,'member_id':id,'role':role}
                response=requests.post(self.base_url,params)
                result=response.json()
                print(result)
                self.assertEqual(result['state'],'success')
                #还原角色状态
                update_role(str(id),oldRole)
        else:
            print('该代理商未有成员')

    def test_setRole_admin(self):
        """设置成员角色-管理员设置成员角色"""
        #获取成员列表
        list=getMemberList.get_member_list(self,self.access_token)
        if len(list)!=0:
            i=0
            for i in range(len(list)):
                id = list[i]['member_id']
                if id=='236':
                    continue
                else:
                    oldRole=selectSole(id)
                    role=''
                    if oldRole=='creator':
                        print('该成员的角色是【创建者】，没有权限设置角色')
                        role='admin'
                    elif oldRole=='admin':
                        print('该成员的角色是【管理员】，没有权限设置角色')
                        role = 'normal'
                    elif oldRole=='normal':
                        print('该成员的角色是【普通成员】,设置为【管理员】')
                        role = 'admin'
                    params={'access_token':Token.get_token_login('Sxs16','123456'),'member_id':id,'role':role}
                    response=requests.post(self.base_url,params)
                    result=response.json()
                    print(result)
                    self.assertEqual(result['error'], '没有权限')
        else:
            print('该代理商未有成员')

    def test_setRole_normal(self):
        """设置成员角色-普通成员设置成员角色"""
        # 获取成员列表
        list = getMemberList.get_member_list(self, self.access_token)
        if len(list) != 0:
            i = 0
            for i in range(len(list)):
                id = list[i]['member_id']
                if id == '236':
                    continue
                else:
                    oldRole = selectSole(id)
                    role = ''
                    if oldRole == 'creator':
                        print('该成员的角色是【创建者】，没有权限设置角色')
                        role = 'admin'
                    elif oldRole == 'admin':
                        print('该成员的角色是【管理员】，没有权限设置角色')
                        role = 'normal'
                    elif oldRole == 'normal':
                        print('该成员的角色是【普通成员】,设置为【管理员】')
                        role = 'admin'
                    params = {'access_token': Token.get_token_login('Sxs15', '123456'), 'member_id': id,'role': role}
                    response = requests.post(self.base_url, params)
                    result = response.json()
                    print(result)
                    self.assertEqual(result['error'], '没有权限')
        else:
            print('该代理商未有成员')

    def test_setRole_noToken(self):
        """设置成员角色-未传token"""
        params = {'access_token': '', 'member_id': '236', 'role': 'admin'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '令牌错误')

    def test_setRole_noId(self):
        """设置成员角色-未传成员id"""
        params = {'access_token': self.access_token, 'member_id': '', 'role': 'admin'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

    def test_setRole_noRole(self):
        """设置成员角色-未传成员id"""
        params = {'access_token': self.access_token, 'member_id': '236', 'role': ''}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

#查询成员角色
def selectSole(memberId):
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "SELECT member_role FROM crm_member WHERE member_id=" + memberId
    cs1.execute(query)
    role = cs1.fetchall()
    if "," in str(role):
        role = role[0][0]
    return role

#修改角色
def update_role(id,role):
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "update crm_member set member_role='"+role+"' WHERE member_id=" + id
    try:
        cs1.execute(query)
        conn.commit()
    except:
        conn.rollback()
    # 关闭cursor对象
    cs1.close()
    # 关闭connection对象
    conn.close()
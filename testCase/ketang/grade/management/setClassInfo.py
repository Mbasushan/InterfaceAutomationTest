#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import db_fixture.mysql_db as mySqlConnect

#设置班级信息
class SetClassInfo(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/setClassInfo"

    def test_setClassInfo_name(self):
        """设置班级信息---班级昵称"""
        access_token=Token.getToken()
        name='厦门众创智库管理咨询有限公司-接口测试'
        params={'access_token':access_token,'class_id':'1000','name':name}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        className=select_data('class_name')
        self.assertEqual(className,name)

    def test_setClassInfo_contact(self):
        """设置班级信息---班级联系人"""
        access_token=Token.getToken()
        contact='测试'
        params={'access_token':access_token,'class_id':'1000','contact':contact}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        className=select_data('class_contact')
        self.assertEqual(className,contact)

    def test_setClassInfo_contact_mobile(self):
        """设置班级信息---班级联系人手机号"""
        access_token=Token.getToken()
        contact_mobile='15960445986'
        params={'access_token':access_token,'class_id':'1000','contact_mobile':contact_mobile}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        class_contact_mobile=select_data('class_contact_mobile')
        self.assertEqual(class_contact_mobile,contact_mobile)

    def test_setClassInfo_join_type(self):
        """设置班级信息---班级加入方式"""
        access_token=Token.getToken()
        type=select_data('class_join_type')
        if type==1:
            join_type=2
            print("当前班级的加入方式为【全部通过】，修改为【人工审核】")
        else:
            join_type=1
            print("当前班级的加入方式为【人工审核】，修改为【全部通过】")
        params={'access_token':access_token,'class_id':'1000','join_type':join_type}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        class_join_type=select_data('class_join_type')
        self.assertEqual(class_join_type,join_type)


    def test_setClassInfo_organization(self):
        """设置班级信息---班级组织名称"""
        access_token=Token.getToken()
        organization='测试班级组织名称'
        params={'access_token':access_token,'class_id':'1000','organization':organization}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        class_organization=select_data('class_organization')
        self.assertEqual(class_organization,organization)

    def test_setClassInfo_quota(self):
        """设置班级信息---班费个人限制金额"""
        access_token=Token.getToken()
        quota=float(100)
        params={'access_token':access_token,'class_id':'1000','quota':quota}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        class_member_quota=select_data('class_member_quota')
        self.assertEqual(class_member_quota,quota)

    def test_setClassInfo_paramsNull(self):
        """设置班级信息---不传参数"""
        access_token = Token.getToken()
        params = {'access_token': access_token, 'class_id': '1000'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_setClassInfo_TokenNull(self):
        """设置班级信息---token为空"""
        params = {'access_token': "", 'class_id': '1000'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')

    def test_setClassInfo_NoJoinClass(self):
        """设置班级信息---不是该班级成员"""
        access_token=Token.get_token_login('Marvel23','123456')
        params = {'access_token': access_token, 'class_id': '1000','name':'测试'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '您没有权限进行操作')

    def test_setClassInfo_normal(self):
        """设置班级信息---普通成员"""
        access_token=Token.get_token_login('苏珊15','123456')
        params = {'access_token': access_token, 'class_id': '1000','name':'测试'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '您没有权限进行操作')

    def test_setClassInfo_admin(self):
        """设置班级信息---管理员修改班级昵称"""
        access_token=Token.get_token_login('冰辰羽','123456')
        params = {'access_token': access_token, 'class_id': '1000','name':'测试'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        className = select_data('class_name')
        self.assertEqual(className, '测试')

    def test_setClassInfo_ClassIdNull(self):
        """设置班级信息---班级id为空"""
        access_token = Token.getToken()
        params = {'access_token': access_token, 'class_id': ''}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')

#查询
def select_data(params):
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "SELECT "+params+" FROM ketang_class WHERE class_key='1000'"
    cs1.execute(query)
    result = cs1.fetchall()[0][0]
    return result
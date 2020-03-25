#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import json
import unittest
import requests
import testCase.common.getToken as Token
import testCase.ketang.grade.group.base.getGroupListBase as getGroupListBase

#设置成员分组
class SetMemberGroup(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/setMemberGroup"
        self.access_token = Token.get_token_login('sxs14', '123456')

    def test_setMemberGroup(self):
        """设置成员分组"""
        group_ids=getGroupListBase.getGroupList(self,self.access_token)
        list=[]
        for i in range(len(group_ids)):
             list.append(group_ids[i]['group_id'])
        list=json.dumps(list)
        print(list)
        params={'access_token':self.access_token,'class_id':1003,'set_user_id':20271,'group_ids':list}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['data']['result'],1)
        #清空该成员分组
        clear_group(self)


    def test_setMemberGroup_noToken(self):
        """设置成员分组---未传token"""
        group_ids=getGroupListBase.getGroupList(self,self.access_token)
        list=[]
        for i in range(len(group_ids)):
             list.append(group_ids[i]['group_id'])
        list=json.dumps(list)
        params={'access_token':"",'class_id':1003,'set_user_id':20271,'group_ids':list}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],"获取账号信息失败")

    def test_setMemberGroup_noClassId(self):
        """设置成员分组---未传classId"""
        group_ids=getGroupListBase.getGroupList(self,self.access_token)
        list=[]
        for i in range(len(group_ids)):
             list.append(group_ids[i]['group_id'])
        list=json.dumps(list)
        params={'access_token':self.access_token,'set_user_id':20271,'group_ids':list}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],"参数错误")

    def test_setMemberGroup_noUserId(self):
        """设置成员分组---未传成员id"""
        group_ids=getGroupListBase.getGroupList(self,self.access_token)
        list=[]
        for i in range(len(group_ids)):
             list.append(group_ids[i]['group_id'])
        list=json.dumps(list)
        params={'access_token':self.access_token,'class_id':1003,'group_ids':list}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],"参数错误")

    def test_setMemberGroup_noGroupIds(self):
        """设置成员分组---未传成员groupIds,清掉该成员分组"""
        clear_group(self)

    def test_setMemberGroup_errorGroupId(self):
        """设置成员分组---该班级未有该分组"""
        params={'access_token':self.access_token,'set_user_id':20271,'group_ids':'["1"]'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],"参数错误")

#清除成员分组
def clear_group(self):
    params = {'access_token': self.access_token, 'class_id': 1003, 'set_user_id': 20271}
    response = requests.post(self.base_url, params)
    result = response.json()
    print(result)
    self.assertEqual(result['data']['result'], 2)
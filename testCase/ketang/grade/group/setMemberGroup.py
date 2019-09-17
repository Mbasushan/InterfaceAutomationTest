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

    def test_setMemberGroup(self):
        """设置成员分组"""
        access_token=Token.getToken()
        group_ids=getGroupListBase.getGroupList(self)
        list=[]
        for i in range(len(group_ids)):
             list.append(group_ids[i]['group_id'])
        list=json.dumps(list)
        print(list)
        params={'access_token':access_token,'class_id':1000,'set_user_id':20061,'group_ids':list}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['data']['result'],1)
        #清空该成员分组
        clear_group(self)


    def test_setMemberGroup_noToken(self):
        """设置成员分组---未传token"""
        group_ids=getGroupListBase.getGroupList(self)
        list=[]
        for i in range(len(group_ids)):
             list.append(group_ids[i]['group_id'])
        list=json.dumps(list)
        params={'access_token':"",'class_id':1000,'set_user_id':20061,'group_ids':list}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],"获取账号信息失败")

    def test_setMemberGroup_noClassId(self):
        """设置成员分组---未传classId"""
        access_token = Token.getToken()
        group_ids=getGroupListBase.getGroupList(self)
        list=[]
        for i in range(len(group_ids)):
             list.append(group_ids[i]['group_id'])
        list=json.dumps(list)
        params={'access_token':access_token,'set_user_id':20061,'group_ids':list}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],"参数错误")

    def test_setMemberGroup_noUserId(self):
        """设置成员分组---未传成员id"""
        access_token = Token.getToken()
        group_ids=getGroupListBase.getGroupList(self)
        list=[]
        for i in range(len(group_ids)):
             list.append(group_ids[i]['group_id'])
        list=json.dumps(list)
        params={'access_token':access_token,'class_id':1000,'group_ids':list}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],"参数错误")

    def test_setMemberGroup_noGroupIds(self):
        """设置成员分组---未传成员groupIds,清掉该成员分组"""
        clear_group(self)

#清除成员分组
def clear_group(self):
    access_token = Token.getToken()
    params = {'access_token': access_token, 'class_id': 1000, 'set_user_id': 20061}
    response = requests.post(self.base_url, params)
    result = response.json()
    print(result)
    self.assertEqual(result['data']['result'], 2)
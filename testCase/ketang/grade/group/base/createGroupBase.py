#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import testCase.common.getToken as Token

#创建分组
def create_group(self,access_token):
    url = 'http://ke.test.mbalib.com/class/createGroup'
    params = {'access_token': access_token,'class_id':1079, 'name': '测试'}
    response=requests.post(url,params)
    result=response.json()
    print(result)
    self.assertNotEqual(result['data']['group_id'], 0)
    groupId=result['data']['group_id']
    return groupId
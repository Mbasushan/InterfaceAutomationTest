#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import testCase.common.getToken as Token

#删除分组
def delete_group(self,id):
    url = 'http://ke.test.mbalib.com/class/delGroup'
    access_token = Token.getToken()
    params = {'access_token': access_token,'class_id':1000, 'group_id': id}
    response=requests.post(url,params)
    result=response.json()
    print(result)
    self.assertEqual(result['data']['result'], 1)
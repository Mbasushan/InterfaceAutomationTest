#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import testCase.common.getToken as Token

#删除分组
def delete_group(self,id,access_token):
    url = 'http://ke.test.mbalib.com/class/delGroup'
    params = {'access_token': access_token,'class_id':1003, 'group_id': id}
    response=requests.post(url,params)
    result=response.json()
    print(result)
    self.assertEqual(result['data']['result'], 1)
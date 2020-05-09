#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import testCase.common.getToken as Token

#获取通知列表
def get_apply_list(self,access_token,state):
    url = 'http://crm.test.mbalib.com/apply/getList'
    response = requests.post(url, params={'access_token': access_token,'state':state})
    result = response.json()
    print(result)
    if result['count'] == 0:
        print('该代理商无通知')
        list=None
    else:
        list=result['list']

    return list
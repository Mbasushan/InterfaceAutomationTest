#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import testCase.common.getToken as Token

#获取成员列表
def get_member_list(self,access_token):
    url = 'http://crm.test.mbalib.com/member/getList'
    response = requests.post(url, params={'access_token': access_token})
    result = response.json()
    print(result)
    if result['count'] == 0:
        print('该代理商无成员')
        list=None
    else:
        list=result['list']

    return list
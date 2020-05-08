#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import testCase.common.getToken as Token

#获取客户列表
def get_customer_list(self,access_token):
    url = 'http://crm.test.mbalib.com/customer/getList'
    response = requests.post(url, params={'access_token': access_token})
    result = response.json()
    print(result)
    if result['count'] == 0:
        print('该代理商无客户')
        list=None
    else:
        list=result['list']

    return list
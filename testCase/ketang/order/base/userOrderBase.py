#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import testCase.common.getToken as Token

#获取课堂用户订单列表
def userOrderList(name):
    url='http://ke.test.mbalib.com/order/userorder'
    params={'access_token':Token.get_token_login(name,'123456')}
    response=requests.get(url,params)
    result=response.json()
    if len(result['data']) == 0:
        return None
    else:
        orderNum=result['data'][0]['order_number']
        return orderNum
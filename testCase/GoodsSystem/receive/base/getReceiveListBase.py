#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import testCase.common.getToken as Token

#获取地址列表
def get_receiveList(self):
    url='http://www.test.mbalib.com/goods/receive/getReceiveList'
    access_token=Token.getToken()
    response = requests.post(url,params={'access_token':access_token})
    result = response.json()
    print(result)
    return result
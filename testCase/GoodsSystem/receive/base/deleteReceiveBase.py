#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import testCase.common.getToken as Token

#删除收货地址
def deleteReceive(self,id):
    url='http://www.test.mbalib.com/goods/receive/delReceive'
    access_token=Token.getToken()
    response = requests.post(url,params={'access_token':access_token,'receive_id':id})
    result = response.json()
    print("删除收货地址成功")
    print(result)
    return result
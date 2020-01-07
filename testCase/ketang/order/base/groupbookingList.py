#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token

#拼团列表
def groupBookingList(self,name,id,type):
    base_url='http://ke.test.mbalib.com/GroupbookingApi/list'
    access_token=Token.get_token_login(name,'123456')
    params={'id':id,'type':type,'access_token':access_token}
    response=requests.get(base_url,params)
    result=response.json()
    return result['data']['list']
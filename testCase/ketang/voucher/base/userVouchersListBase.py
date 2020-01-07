#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token

#优惠券列表
def userVoucherList(self):
    base_url = "http://ke.test.mbalib.com/api/userVouchersList"
    access_token = Token.get_token_login('sxs14', '123456')
    response=requests.get(base_url,params={'access_token':access_token})
    result=response.json()
    print(result)
    self.assertEqual(result['state'],'success')
    keys=""
    nouseKeys=""
    hKeys=""
    if len(result['data']['nouse'])!=0:
        for i in range(len(result['data']['nouse'])):
            nouseKeys=result['data']['nouse'][i]['voucher_key']+","+nouseKeys
    if len(result['data']['history'])!=0:
        for r in range(len(result['data']['history'])):
            print(result['data']['history'][0]['voucher_key'])
            hKeys=result['data']['history'][r]['voucher_key']+","+hKeys
    #合并
    keys=(hKeys+','+nouseKeys).split(',')
    print(keys)
    return keys
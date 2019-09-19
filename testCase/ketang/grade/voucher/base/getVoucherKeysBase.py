#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import testCase.common.getToken as Token

#获取未领取的优惠券key
def getVoucherKey_canreceive(self):
    url='http://ke.test.mbalib.com/class/getVoucherList'
    access_token = Token.getToken()
    params = {'access_token': access_token, 'class_id': 1000}
    response = requests.get(url, params)
    result = response.json()
    keys=[]
    for i in range(len(result['data']['list'])):
        data=result['data']['list']
        if data[i]['voucher_state']=='canreceive':
            keys.append(data[i]['voucher_key'])
    return keys

#获取优惠券：已领取未使用
def getVoucherKey_nouse(self):
    url='http://ke.test.mbalib.com/class/getVoucherList'
    access_token = Token.getToken()
    params = {'access_token': access_token, 'class_id': 1000}
    response = requests.get(url, params)
    result = response.json()
    print(result)
    keys=[]
    for i in range(len(result['data']['list'])):
        data=result['data']['list']
        if data[i]['voucher_state']=='nouse':
            keys.append(data[i]['voucher_key'])
    print(keys)
    return keys

#获取优惠券：已使用
def getVoucherKey_used(self):
    url='http://ke.test.mbalib.com/class/getVoucherList'
    access_token = Token.getToken()
    params = {'access_token': access_token, 'class_id': 1000}
    response = requests.get(url, params)
    result = response.json()
    print(result)
    keys=[]
    for i in range(len(result['data']['list'])):
        data=result['data']['list']
        if data[i]['voucher_state']=='used':
            keys.append(data[i]['voucher_key'])
    print(keys)
    return keys

#获取优惠券：已领完
def getVoucherKey_broughtup(self):
    url='http://ke.test.mbalib.com/class/getVoucherList'
    access_token = Token.getToken()
    params = {'access_token': access_token, 'class_id': 1000}
    response = requests.get(url, params)
    result = response.json()
    print(result)
    keys=[]
    for i in range(len(result['data']['list'])):
        data=result['data']['list']
        if data[i]['voucher_state']=='broughtup':
            keys.append(data[i]['voucher_key'])
    print(keys)
    return keys
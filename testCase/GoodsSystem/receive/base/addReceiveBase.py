#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import testCase.common.getToken as Token

#添加收货地址
def addReceive(self):
    url='http://www.test.mbalib.com/goods/receive/saveReceive'
    access_token=Token.getToken()
    # 表单
    # 姓名
    name = '接口测试'
    # 电话
    mobile = '11111111111'
    # 省
    province = '350000'
    # 市
    city = '350200'
    # 区
    county = '350203'
    # 详细地址
    address = '软件园二期望海路59号之一'
    # 是否默认地址
    is_default = 0
    params = {'access_token': access_token, 'name': name, 'mobile': mobile, 'province': province, 'city': city,
              'county': county, 'address': address, 'is_default': is_default}
    response = requests.post(url, params)
    result = response.json()
    print(result)
    print("添加收货地址成功")
    self.assertNotEqual(len(result['data']), 0)
    receive_id = result['data']['receive_id']
    return receive_id
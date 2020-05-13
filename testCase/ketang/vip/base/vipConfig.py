#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import testCase.common.getToken as Token


def get_vipConfig(self):
    response = requests.post('http://ke.test.mbalib.com/vip/config')
    result = response.json()
    self.assertEqual(result['state'],'success')
    print("会员配置数据如下：")
    print(result['data'])
    return result['data']
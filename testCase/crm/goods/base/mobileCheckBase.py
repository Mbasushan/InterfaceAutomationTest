#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import testCase.common.getToken as Token
import testCase.crm.agent.base.getGoodsListBase as getGoodsListBase

#手机号验证
def mobile_check(self,access_token):
    url='http://crm.test.mbalib.com/goods/MobileCheck'
    list = getGoodsListBase.getGoodsList(self)
    if len(list) != 0:
        id = list[0]['goods_id']
        params = {'access_token': access_token, 'goods_id': id, 'mobiles': '15960445986,17359262064,565656'}
        response = requests.post(url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['total'], 3)
        list=result['list']
    else:
        print('该代理商没有商品')
        list=''
    return list
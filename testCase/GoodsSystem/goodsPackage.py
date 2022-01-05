#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import testCase.common.getToken as Token

#获取商品列表中第一个商品的套餐信息
def get_gp(self):
    url='http://www.test.mbalib.com/goods/goods/getGoodsListNew'
    response = requests.post(url)
    result = response.json()
    print(result)
    id=result['data'][0]['goods_id']
    goodurl='http://www.test.mbalib.com/goods/goods/getGoodsDetail'
    params = {'access_token':Token.getToken(), 'goods_id': id}
    esponse = requests.post(goodurl,params)
    gps = esponse.json()
    print(gps)
    return gps['data']['goods_package']
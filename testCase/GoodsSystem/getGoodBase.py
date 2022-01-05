#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests

#获取商品列表中第一个商品
def get_goods(self):
    url='http://www.test.mbalib.com/goods/goods/getGoodsListNew'
    response = requests.post(url)
    result = response.json()
    print(result)
    id=result['data'][0]['goods_id']
    return id
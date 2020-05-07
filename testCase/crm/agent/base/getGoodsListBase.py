import requests
import unittest
import testCase.common.getToken as Token

def getGoodsList(self):
    """获取商品列表"""
    url='http://crm.test.mbalib.com/goods/getGoodsList'
    start = 0
    params = {"start": start, "num": 10, 'access_token': Token.getToken()}
    response = requests.post(url, params=params)
    result = response.json()
    print(result)
    return result
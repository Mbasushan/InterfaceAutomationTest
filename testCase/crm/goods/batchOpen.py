#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token
import testCase.crm.agent.base.getGoodsListBase as getGoodsListBase
import testCase.crm.goods.base.mobileCheckBase as mobileCheckBse

#批量授权
class BatchOpen(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/goods/batchOpen'
        self.access_token=Token.get_token_login('sxs15','123456')

    def test_batchOpen(self):
        """批量授权"""
        # 查看该代理商是否有商品
        list = getGoodsListBase.getGoodsList(self)
        if len(list) != 0:
            id = list[0]['goods_id']
            #授权手机号验证
            #mobile_list=mobileCheckBse.mobile_check(self,self.access_token)
            mobile_list='[{"mobile":"15960445986","result":"success"},{"mobile":"17359262064","result":"unregistered"},{"mobile":"565656","result":"illegal"}]'
            params = {'access_token': self.access_token, 'number':'2','goods_id': id, 'mobile_list': mobile_list}
            response = requests.post(self.base_url, params)
            result = response.json()
            print(result)
            self.assertEqual(result['success_count'], 1)
        else:
            print('该代理商没有商品')
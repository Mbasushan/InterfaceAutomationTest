#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token
import testCase.crm.agent.base.getGoodsListBase as getGoodsListBase

#生成海报
class CreatePoster(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/goods/createPoster'
        self.access_token=Token.get_token_login('sxs15','123456')

    def test_createPoster(self):
        """生成海报"""
        list = getGoodsListBase.getGoodsList(self)
        if len(list)!=0:
            id=list[0]['goods_id']
            params = {'access_token':self.access_token, 'goods_id':id,'template':'0'}
            response=requests.post(self.base_url,params)
            result=response.json()
            print(result)
            self.assertNotEqual(len(result['poster_src']),0)
        else:
            print('该代理商没有商品')

    def test_createPoster_noToken(self):
        """生成海报-未传token"""
        list = getGoodsListBase.getGoodsList(self)
        if len(list)!=0:
            id=list[0]['goods_id']
            params = {'access_token':'', 'goods_id':id,'template':'0'}
            response=requests.post(self.base_url,params)
            result=response.json()
            print(result)
            self.assertEqual(result['error'],'令牌错误')
        else:
            print('该代理商没有商品')

    def test_createPoster_noTemplate(self):
        """生成海报-未传海报模板序号"""
        list = getGoodsListBase.getGoodsList(self)
        if len(list)!=0:
            id=list[0]['goods_id']
            params = {'access_token':self.access_token, 'goods_id':id,'template':''}
            response=requests.post(self.base_url,params)
            result=response.json()
            print(result)
            self.assertNotEqual(len(result['poster_src']), 0)
        else:
            print('该代理商没有商品')

    def test_createPoster_noID(self):
        """生成海报-未传商品id"""
        params = {'access_token':self.access_token, 'goods_id':'','template':'0'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

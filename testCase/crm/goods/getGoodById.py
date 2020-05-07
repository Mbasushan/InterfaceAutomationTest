#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token
import testCase.crm.agent.base.getGoodsListBase as getGoodsListBase

#获取商品详情
class GetGoodById(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/goods/getGoodById'
        self.access_token=Token.getToken()

    def test_getGoodById(self):
        """获取商品详情"""
        #查看该代理商是否有商品
        list=getGoodsListBase.getGoodsList(self)
        if len(list)!=0:
            id=list[0]['goods_id']
            response=requests.post(self.base_url,params={'access_token':self.access_token,'goods_id':id})
            result=response.json()
            print(result)
            self.assertEqual(result['goods_id'],id)
        else:
            print('该代理商没有商品')

    def test_noToken(self):
        """获取商品详情-未登录"""
        #查看该代理商是否有商品
        list=getGoodsListBase.getGoodsList(self)
        if len(list)!=0:
            id=list[0]['goods_id']
            response=requests.post(self.base_url,params={'access_token':'','goods_id':id})
            result=response.json()
            print(result)
            self.assertEqual(result['error'],'令牌错误')
        else:
            print('该代理商没有商品')

    def test_noId(self):
        """获取商品详情-未传商品id"""
        #查看该代理商是否有商品
        response=requests.post(self.base_url,params={'access_token':self.access_token,'goods_id':''})
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')
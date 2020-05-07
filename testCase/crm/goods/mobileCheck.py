#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token
import testCase.crm.agent.base.getGoodsListBase as getGoodsListBase
import testCase.crm.goods.base.mobileCheckBase as mobileCheckBse

#授权手机号验证
class MobileCheck(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/goods/MobileCheck'
        self.access_token=Token.get_token_login('sxs15','123456')

    def test_mobileCheck(self):
        """授权手机号验证"""
        mobileCheckBse.mobile_check(self,self.access_token)

    def test_mobileCheck_noToken(self):
        """授权手机号验证-未传token"""
        # 查看该代理商是否有商品
        list = getGoodsListBase.getGoodsList(self)
        if len(list)!=0:
            id=list[0]['goods_id']
            params = {'access_token':'', 'goods_id':id,'mobiles':'15960445986,17359262064,565656'}
            response=requests.post(self.base_url,params)
            result=response.json()
            print(result)
            self.assertEqual(result['error'], '令牌错误')
        else:
            print('该代理商没有商品')

    def test_mobileCheck_noMobiles(self):
        """授权手机号验证-未传手机号"""
        # 查看该代理商是否有商品
        list = getGoodsListBase.getGoodsList(self)
        if len(list)!=0:
            id=list[0]['goods_id']
            params = {'access_token':self.access_token, 'goods_id':id,'mobiles':''}
            response=requests.post(self.base_url,params)
            result=response.json()
            print(result)
            self.assertEqual(result['error'], '参数错误')
        else:
            print('该代理商没有商品')

    def test_mobileCheck_noGId(self):
        """授权手机号验证-未传商品id"""
        # 查看该代理商是否有商品
        list = getGoodsListBase.getGoodsList(self)
        if len(list)!=0:
            id=list[0]['goods_id']
            params = {'access_token':self.access_token, 'goods_id':'','mobiles':'15960445986,17359262064,565656'}
            response=requests.post(self.base_url,params)
            result=response.json()
            print(result)
            self.assertEqual(result['error'], '参数错误')
        else:
            print('该代理商没有商品')
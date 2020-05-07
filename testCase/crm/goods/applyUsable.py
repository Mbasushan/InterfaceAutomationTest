#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token
import testCase.crm.agent.base.getGoodsListBase as getGoodsListBase

#授权数申请
class ApplyUsable(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/goods/applyUsable'
        self.access_token=Token.get_token_login('sxs15','123456')

    def test_applyUsable(self):
        """授权数申请-普通成员申请"""
        # 查看该代理商是否有商品
        list = getGoodsListBase.getGoodsList(self)
        if len(list)!=0:
            id=list[0]['goods_id']
            usable_number=list[0]['ag_usable_number']
            num=1
            params = {'access_token':self.access_token, 'goods_id':id,'num':num}
            response=requests.post(self.base_url,params)
            result=response.json()
            print(result)
            if int(usable_number)<num:
                self.assertEqual(result['error'],'授权数不足')
            else:
                self.assertEqual(result['state'], 'success')
        else:
            print('该代理商没有商品')

    def test_applyUsable_admin(self):
        """授权数申请-管理员申请"""
        # 查看该代理商是否有商品
        list = getGoodsListBase.getGoodsList(self)
        if len(list)!=0:
            id=list[0]['goods_id']
            num=1
            params = {'access_token':Token.getToken(), 'goods_id':id,'num':num}
            response=requests.post(self.base_url,params)
            result=response.json()
            print(result)
            self.assertEqual(result['error'],'管理员无需申请，可直接授权')
        else:
            print('该代理商没有商品')

    def test_applyUsable_noJoin(self):
        """授权数申请-不是该代理商成员"""
        # 查看该代理商是否有商品
        list = getGoodsListBase.getGoodsList(self)
        if len(list) != 0:
            id = list[0]['goods_id']
            num = 1
            params = {'access_token': Token.get_token_login('sxs14','123456'), 'goods_id': id, 'num': num}
            response = requests.post(self.base_url, params)
            result = response.json()
            print(result)
            self.assertEqual(result['error'], '未加入代理商')
        else:
            print('该代理商没有商品')

    def test_applyUsable_noToken(self):
        """授权数申请-未传token"""
        # 查看该代理商是否有商品
        list = getGoodsListBase.getGoodsList(self)
        if len(list) != 0:
            id = list[0]['goods_id']
            num = 1
            params = {'access_token': '', 'goods_id': id, 'num': num}
            response = requests.post(self.base_url, params)
            result = response.json()
            print(result)
            self.assertEqual(result['error'], '令牌错误')
        else:
            print('该代理商没有商品')

    def test_applyUsable_noGoodsId(self):
        """授权数申请-未传商品id"""
        # 查看该代理商是否有商品
        list = getGoodsListBase.getGoodsList(self)
        if len(list) != 0:
            id = list[0]['goods_id']
            num = 1
            params = {'access_token': self.access_token, 'goods_id': '', 'num': num}
            response = requests.post(self.base_url, params)
            result = response.json()
            print(result)
            self.assertEqual(result['error'], '参数错误')
        else:
            print('该代理商没有商品')

    def test_applyUsable_noNum(self):
        """授权数申请-未传申请数量"""
        # 查看该代理商是否有商品
        list = getGoodsListBase.getGoodsList(self)
        if len(list) != 0:
            id = list[0]['goods_id']
            params = {'access_token': self.access_token, 'goods_id': id, 'num': ''}
            response = requests.post(self.base_url, params)
            result = response.json()
            print(result)
            self.assertEqual(result['error'], '参数错误')
        else:
            print('该代理商没有商品')
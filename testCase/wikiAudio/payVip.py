#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import testCase.wikiAudio.base.getVipPrices as getVipPrices
import testCase.common.virtualPayment as virtualPayment


#开通大咖VIP
class AudioVip_pay(unittest.TestCase):

    def setUp(self):
        self.base_url="http://passport.test.mbalib.com/api2/RechargeWealth"
        self.access_token=Token.getToken()

    def test_h5_audioVip_pay(self):
        """h5开通大咖VIP支付"""
        #获取商品项
        memberPrices=getVipPrices.getVip_prices(self,'h5')
        if memberPrices!=None:
            params={'access_token':self.access_token,'member':memberPrices[0]['key'],'amount':memberPrices[0]['price'],'key':memberPrices[0]['key'],'origin':'web_activity','type':'audio_member','pay_type':'weixin'}
            response=requests.post(self.base_url,params)
            result=response.json()
            self.assertEqual(result['state'],'success')
            #虚拟支付
            trade=result['order_number']
            fee=result['amount']
            virtualPayment.audio_pay(self,trade,fee)
        else:
            print("大咖会员配置为空")


    def test_ios_audioVip_pay(self):
        """ios普通版-开通大咖VIP支付"""
        #获取商品项
        memberPrices=getVipPrices.getVip_prices(self,'wiki')
        if memberPrices!=None:
            header = {'User-Agent': 'MBALIB-WIKI-APP/6.7.1(iPhone 8 Plus;iOS 12.3.2;mbalibnormal;zh-cn;Build/374;Device/7740195D-701F-4026-9A05-C05954C2AFEC;)'}
            params={'access_token':self.access_token,'member':memberPrices[0]['key'],'amount':memberPrices[0]['price'],'key':memberPrices[0]['key'],'origin':'wiki','type':'audio_member','pay_type':'weixin'}
            response=requests.post(self.base_url,data=params,headers=header)
            result=response.json()
            self.assertEqual(result['state'],'success')
            #虚拟支付
            trade=result['order_number']
            fee=memberPrices[0]['price']
            virtualPayment.audio_pay(self,trade,fee)
        else:
            print("大咖会员配置为空")

    def test_iosFresh_audioVip_pay(self):
        """ios专业版-开通大咖VIP支付"""
        #获取商品项
        memberPrices=getVipPrices.getVip_prices(self,'wikifresh')
        if memberPrices!=None:
            header = {'User-Agent': 'MBALIB-WIKI-APP/6.7.1(iPhone 8 Plus;iOS 12.3.2;mbalibfresh;zh-cn;Build/374;Device/7740195D-701F-4026-9A05-C05954C2AFEC;)'}
            params={'access_token':self.access_token,'member':memberPrices[0]['key'],'amount':memberPrices[0]['price'],'key':memberPrices[0]['key'],'origin':'wikifresh','type':'audio_member','pay_type':'weixin'}
            response=requests.post(self.base_url,headers=header,data=params)
            result=response.json()
            self.assertEqual(result['state'],'success')
            #虚拟支付
            trade=result['order_number']
            fee=memberPrices[0]['price']
            virtualPayment.audio_pay(self,trade,fee)
        else:
            print("大咖会员配置为空")

    def test_Android_audioVip_pay(self):
        """Android-开通大咖VIP支付"""
        #获取商品项
        memberPrices=getVipPrices.getVip_prices(self,'android')
        if memberPrices!=None:
            header = {'User-Agent': 'MBALIB-WIKI-APP/6.9.7(CLT-AL00; Android 9;zh-cn;Build/113;Device/ffffffff-ad36-96e3-ad36-96e300000000;)'}
            params={'access_token':self.access_token,'member':memberPrices[0]['key'],'amount':memberPrices[0]['price'],'key':memberPrices[0]['key'],'origin':'androidwiki','type':'audio_member','pay_type':'weixin'}
            response=requests.post(self.base_url,data=params,headers=header)
            result=response.json()
            self.assertEqual(result['state'],'success')
            #虚拟支付
            trade=result['order_number']
            fee=memberPrices[0]['price']
            virtualPayment.audio_pay(self,trade,fee)
        else:
            print("Android未有大咖讲百科VIP配置")
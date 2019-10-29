#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as getToken
import testCase.common.virtualPayment as virtualPayment
import db_fixture.mysql_db as mySqlConnect

#开通会员
class Recharge(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/vip/recharge"

    def test_getVipConfig_noType(self):
        """开通会员-未传会员类型"""
        #paytype:weixin,alipay,mb
        access_toke=getToken.getToken()
        params={"paytype":"weixin","access_token":access_toke}
        response = requests.post(self.base_url,params=params)
        result = response.json()
        self.assertEqual(result['error'],'参数错误')

    def test_getVipConfig_noPayType(self):
        """开通会员-未传支付类型"""
        #paytype:weixin,alipay,mb
        access_toke=getToken.getToken()
        params={"type":"ketang_vip_year","access_token":access_toke}
        response = requests.post(self.base_url,params=params)
        result = response.json()
        print(result)
        self.assertEqual(result['state'],'success')
        print("未传支付类型，则默认为微信支付，所以发起开通会员成功")

    def test_getVipConfig_noAccessToke(self):
        """开通会员-未传用户令牌"""
        #paytype:weixin,alipay,mb
        params={"type":"ketang_vip_year","paytype":'weixin',"access_token":''}
        response = requests.post(self.base_url,params=params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_getVipConfig_weixin(self):
        """开通会员-微信支付"""
        #paytype:weixin,alipay,mb
        print("发起订单")
        access_toke = getToken.getToken()
        params={"type":"ketang_vip_year","paytype":'weixin',"access_token":access_toke}
        response = requests.post(self.base_url,params=params)
        result = response.json()
        print(result)
        self.assertEqual(result['state'],'success')
        trade=result['order_number']
        fee=getFee(str(result['id']))
        print(fee)
        #虚拟支付接口
        virtualPayment.test_virtualPaymentKetang(self,trade,fee)


    def test_getVipConfig_alipay(self):
        """开通会员-支付宝"""
        #paytype:weixin,alipay,mb
        print("发起订单")
        access_toke = getToken.getToken()
        params={"type":"ketang_vip_year","paytype":'alipay',"access_token":access_toke}
        response = requests.post(self.base_url,params=params)
        result = response.json()
        print(result)
        self.assertEqual(result['state'],'success')
        trade = result['order_number']
        fee = getFee(str(result['id']))
        print(fee)
        # 虚拟支付接口
        virtualPayment.test_virtualPaymentKetang(self, trade, fee)

    def test_getVipConfig_mb(self):
        """开通会员-M币"""
        #paytype:weixin,alipay,mb
        print("发起订单")
        access_toke = getToken.getToken()
        params={"type":"ketang_vip_year","paytype":'mb',"access_token":access_toke}
        response = requests.post(self.base_url,params=params)
        result = response.json()
        print(result)
        if 'state' in result:
            self.assertEqual(result['state'], 'success')
        else:
            self.assertEqual(result['error'],'余额不足')



def getType(self):
    response = requests.post('http://ke.test.mbalib.com/vip/config')
    result = response.json()
    self.assertEqual(result['state'], 'success')
    type=result['data']['key']
    print(type)
    return type

#根据订单id获取订单金额
def getFee(id):
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "SELECT order_amount FROM ketang_order WHERE order_id='" + id + "'"
    cs1.execute(query)
    fee = cs1.fetchone()[0]
    return fee
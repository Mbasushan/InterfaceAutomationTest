#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import db_fixture.mysql_db as mySqlConnect
import testCase.ketang.grade.voucher.base.getVoucherKeysBase as getVourcherBase

#领取班级优惠券
class GetVoucher(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/class/getVoucher"

    def test_getVoucher(self):
        """领取班级优惠券"""
        access_token=Token.getToken()
        keys=getVourcherBase.getVoucherKey_canreceive(self)
        if keys==[]:
            print("班级优惠券已都领取")
        else:
            params={'access_token':access_token,'key':keys[0]}
            response=requests.get(self.base_url,params)
            result=response.json()
            print(result)
            self.assertEqual(len(result['data']),0)
            print("领取班级优惠券成功")
            #删除领取优惠券记录
            delete_getVoucher(keys[0])

    def test_getVoucher_broughtup(self):
        """领取优惠券---已领完"""
        access_token = Token.getToken()
        keys = getVourcherBase.getVoucherKey_broughtup(self)
        if keys == []:
            print("班级优惠券已都领取")
        else:
            params = {'access_token': access_token, 'key': keys[0]}
            response = requests.get(self.base_url, params)
            result = response.json()
            print(result)
            self.assertEqual(result['error'], '已被领完了')

    def test_getVoucher_nouse(self):
        """领取优惠券---已领取未使用"""
        access_token = Token.getToken()
        keys = getVourcherBase.getVoucherKey_nouse(self)
        if keys == []:
            print("班级优惠券已都领取")
        else:
            for i in range(len(keys)):
                params = {'access_token': access_token, 'key': keys[i]}
                response = requests.get(self.base_url, params)
                result = response.json()
                print(result)


    def test_getVoucher_noToken(self):
        """领取班级优惠券---未传token"""
        params={'access_token':"",'key':'d9cac4c1b8e811f34b0acd4fe46e10c9'}
        response=requests.get(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')

    def test_getVoucher_noKey(self):
        """领取班级优惠券---未传优惠券key"""
        params = {'access_token': Token.getToken(),'key':''}
        response = requests.get(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '您已领取优惠券')

    def test_getVoucher_noJoinClass(self):
        """领取班级优惠券---用户不是该班级成员"""
        access_token = Token.get_token_login('Sxs14','123456')
        keys = getVourcherBase.getVoucherKey_canreceive(self)
        if keys == []:
            print("班级优惠券已都领取")
        else:
            params = {'access_token': access_token, 'key': keys[0]}
            response = requests.get(self.base_url, params)
            result = response.json()
            print(result)
            self.assertEqual(result['error'], '领取失败')


#删除领取优惠券记录
def delete_getVoucher(key):
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "DELETE FROM ketang_voucher_user WHERE vu_voucher_id =(SELECT voucher_id FROM ketang_voucher WHERE voucher_key='"+key+"' )"
    try:
        cs1.execute(query)
        conn.commit()
    except:
        conn.rollback()
    # 关闭cursor对象
    cs1.close()
    # 关闭connection对象
    conn.close()
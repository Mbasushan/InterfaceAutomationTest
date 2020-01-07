#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import testCase.ketang.order.base.previewBase as previewBase
import testCase.common.virtualPayment as virtualPayment
import testCase.ketang.order.base.getOrderFee as getOrderFee
import testCase.ketang.order.base.delSign as delSign
import testCase.ketang.order.base.deleteOrder as deleteOrder


#课程支付
class CoursePay(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/api/CoursePay"
        self.access_token = Token.get_token_login('sxs14', '123456')

    def test_columnPay(self):
        """pc报名专栏"""
        params={'id':259,'type':'column','access_token':self.access_token,'from':'pc','from_source':'jiekou'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        order_number=''
        self.assertEqual(result['state'],'success')
        if result['state']=='success':
            order_number=result['order_number']
            fee= getOrderFee.getFee(str(result['id']))
            print(fee)
            #虚拟支付
            virtualPayment.ketang_pay(self,order_number,fee)
            #删除报名
            delSign.delete('20271', '259')
            # 删除订单
            deleteOrder.delete(order_number)

    def test_coursePay(self):
        """pc报名单课"""
        params={'id':8520014,'type':'signup','access_token':self.access_token,'from':'pc','from_source':'jiekou'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        order_number=''
        self.assertEqual(result['state'],'success')
        if result['state']=='success':
            order_number=result['order_number']
            fee= getOrderFee.getFee(str(result['id']))
            print(fee)
            #虚拟支付
            virtualPayment.ketang_pay(self,order_number,fee)
            #删除报名
            delSign.delete('20271', '660')
            # 删除订单
            deleteOrder.delete(order_number)

    def test_packagePay(self):
        """pc报名课程包"""
        params={'id':1017,'type':'package','access_token':self.access_token,'from':'pc','from_source':'jiekou'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        order_number=''
        self.assertEqual(result['state'],'success')
        if result['state']=='success':
            order_number=result['order_number']
            fee= getOrderFee.getFee(str(result['id']))
            print(fee)
            #虚拟支付
            virtualPayment.ketang_pay(self,order_number,fee)
            #删除报名
            delSign.delete('20271', '1017')
            # 删除订单
            deleteOrder.delete(order_number)

    def test_gift_course(self):
        """单课赠礼"""
        params = {'id': 8520014, 'type': 'gift', 'access_token': self.access_token, 'from': 'pc', 'from_source': 'jiekou'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        order_number = ''
        self.assertEqual(result['state'], 'success')
        if result['state'] == 'success':
            order_number = result['order_number']
            fee = getOrderFee.getFee(str(result['id']))
            print(fee)
            # 虚拟支付
            virtualPayment.ketang_pay(self, order_number, fee)
            # 删除订单
            deleteOrder.delete(order_number)

    def test_gift_column(self):
        """专栏赠礼"""
        params = {'id': 259, 'type': 'gift_column', 'access_token': self.access_token, 'from': 'pc', 'from_source': 'jiekou'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        order_number = ''
        self.assertEqual(result['state'], 'success')
        if result['state'] == 'success':
            order_number = result['order_number']
            fee = getOrderFee.getFee(str(result['id']))
            print(fee)
            # 虚拟支付
            virtualPayment.ketang_pay(self, order_number, fee)
            # 删除订单
            deleteOrder.delete(order_number)

    def test_gift_package(self):
        """课程包赠礼"""
        params = {'id': 1017, 'type': 'gift_package', 'access_token': self.access_token, 'from': 'pc', 'from_source': 'jiekou'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        order_number = ''
        self.assertEqual(result['state'], 'success')
        if result['state'] == 'success':
            order_number = result['order_number']
            fee = getOrderFee.getFee(str(result['id']))
            print(fee)
            # 虚拟支付
            virtualPayment.ketang_pay(self, order_number, fee)
            # 删除订单
            deleteOrder.delete(order_number)

    def test_gifts_column(self):
        """专栏赠礼-多份"""
        params = {'id': 259, 'type': 'gift_column', 'access_token': self.access_token,'num':3, 'from': 'pc', 'from_source': 'jiekou'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        order_number = ''
        self.assertEqual(result['state'], 'success')
        if result['state'] == 'success':
            order_number = result['order_number']
            fee = getOrderFee.getFee(str(result['id']))
            print(fee)
            # 虚拟支付
            virtualPayment.ketang_pay(self, order_number, fee)
            # 删除订单
            deleteOrder.delete(order_number)

    def test_course_voucher(self):
        """课程报名使用优惠券"""
        #获取支付页
        result = previewBase.course_preview(self)
        vouchers=result['vouchers']
        #判断是否有优惠券
        if vouchers==[]:
            print('该课程未有优惠券')
        else:
            #获取优惠券
            voucher_id=vouchers[0]['id']
            params = {'id': 8520014, 'type': 'signup', 'access_token': self.access_token,'voucher_id':voucher_id, 'from': 'pc', 'from_source': 'jiekou'}
            response = requests.post(self.base_url, params)
            result = response.json()
            print(result)
            order_number = ''
            self.assertEqual(result['state'], 'success')
            if result['state'] == 'success':
                order_number = result['order_number']
                fee = getOrderFee.getFee(str(result['id']))
                print(fee)
                 # 虚拟支付
                virtualPayment.ketang_pay(self, order_number, fee)
                # 删除报名
                delSign.delete('20271','660')
                # 删除订单
                deleteOrder.delete(order_number)

    def test_column_voucher(self):
        """专栏报名使用优惠券"""
        #获取支付页
        result=previewBase.column_preview(self)
        vouchers=result['vouchers']
        #判断是否有优惠券
        if vouchers==[]:
            print('该专栏未有优惠券')
        else:
            #获取优惠券
            voucher_id=vouchers[0]['id']
            params = {'id': 259, 'type': 'signup', 'access_token': self.access_token,'voucher_id':voucher_id, 'from': 'pc', 'from_source': 'jiekou'}
            response = requests.post(self.base_url, params)
            result = response.json()
            print(result)
            order_number = ''
            self.assertEqual(result['state'], 'success')
            if result['state'] == 'success':
                order_number = result['order_number']
                fee = getOrderFee.getFee(str(result['id']))
                print(fee)
                 # 虚拟支付
                virtualPayment.ketang_pay(self, order_number, fee)
                # 删除报名
                delSign.delete('20271','259')
                # 删除订单
                deleteOrder.delete(order_number)

    def test_package_voucher(self):
        """课程包报名使用优惠券"""
        #获取支付页
        result=previewBase.package_preview(self)
        vouchers=result['vouchers']
        #判断是否有优惠券
        if vouchers==[]:
            print('该课程包未有优惠券')
        else:
            #获取优惠券
            voucher_id=vouchers[0]['id']
            params = {'id': 1017, 'type': 'signup', 'access_token': self.access_token,'voucher_id':voucher_id, 'from': 'pc', 'from_source': 'jiekou'}
            response = requests.post(self.base_url, params)
            result = response.json()
            print(result)
            order_number = ''
            self.assertEqual(result['state'], 'success')
            if result['state'] == 'success':
                order_number = result['order_number']
                fee = getOrderFee.getFee(str(result['id']))
                print(fee)
                 # 虚拟支付
                virtualPayment.ketang_pay(self, order_number, fee)
                # 删除报名
                delSign.delete('20271','1017')
                # 删除订单
                deleteOrder.delete(order_number)

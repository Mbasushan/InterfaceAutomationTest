#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import testCase.ketang.order.base.previewBase as previewBase
import testCase.common.virtualPayment as virtualPayment
import testCase.ketang.order.base.getOrderFee as getOrderFee
import testCase.ketang.order.base.deleteGroupBooking as deleteGroupBooking
import testCase.ketang.order.base.deleteOrder as deleteOrder
import testCase.ketang.order.base.groupbookingList as groupbookingList
import testCase.ketang.order.base.delSign as delSign

#课程拼团
class GroupBooking(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/groupbookingapi/pay"
        self.access_token = Token.get_token_login('sxs14', '123456')

    def test_create_groupbooking(self):
        """单课开团"""
        #获取支付页
        result = previewBase.course_groupbooking(self)
        gid=result['item']['groupbooking_set_id']
        price=result['item']['price']
        # 拼团发起支付
        params={'access_token': self.access_token,'type':'create','gid':gid,'price':price,'payInstru':'weixin'}
        response=requests.post(self.base_url,params)
        re = response.json()
        self.assertEqual(re['state'],'success')
        if re['state']=='success':
            order_number=re['order_number']
            fee= getOrderFee.getFee(str(re['id']))
            print(fee)
            #虚拟支付
            virtualPayment.ketang_pay(self,order_number,fee)
            #删除拼团
            deleteGroupBooking.delete('20271', '660')
            #删除订单
            deleteOrder.delete(order_number)

    def test_column_create_groupbooking(self):
        """专栏开团"""
        #获取支付页
        result = previewBase.column_groupbooking(self)
        gid=result['item']['groupbooking_set_id']
        price=result['item']['price']
        # 拼团发起支付
        params={'access_token': self.access_token,'type':'create','gid':gid,'price':price,'payInstru':'weixin'}
        response=requests.post(self.base_url,params)
        re = response.json()
        self.assertEqual(re['state'],'success')
        if re['state']=='success':
            order_number=re['order_number']
            fee= getOrderFee.getFee(str(re['id']))
            print(fee)
            #虚拟支付
            virtualPayment.ketang_pay(self,order_number,fee)
            #删除拼团
            deleteGroupBooking.delete('20271', '57')
            #删除订单
            deleteOrder.delete(order_number)

    def test_package_create_groupbooking(self):
        """课程包开团"""
        #获取支付页
        result = previewBase.package_groupbooking(self)
        gid=result['item']['groupbooking_set_id']
        price=result['item']['price']
        # 拼团发起支付
        params={'access_token': self.access_token,'type':'create','gid':gid,'price':price,'payInstru':'weixin'}
        response=requests.post(self.base_url,params)
        re = response.json()
        self.assertEqual(re['state'],'success')
        if re['state']=='success':
            order_number=re['order_number']
            fee= getOrderFee.getFee(str(re['id']))
            print(fee)
            #虚拟支付
            virtualPayment.ketang_pay(self,order_number,fee)
            #删除拼团
            deleteGroupBooking.delete('20271', '1017')
            #删除订单
            deleteOrder.delete(order_number)

    def test_course_join_groupbooking(self):
        """课程参团"""
        order_number1=''
        #开团
        # 获取支付页
        result = previewBase.course_groupbooking(self)
        gid = result['item']['groupbooking_set_id']
        price = result['item']['price']
        # 开团发起支付
        params = {'access_token': self.access_token, 'type': 'create', 'gid': gid, 'price': price,
                  'payInstru': 'weixin'}
        response = requests.post(self.base_url, params)
        re = response.json()
        self.assertEqual(re['state'], 'success')
        if re['state'] == 'success':
            order_number1 = re['order_number']
            fee = getOrderFee.getFee(str(re['id']))
            print(fee)
            # 虚拟支付
            virtualPayment.ketang_pay(self, order_number1, fee)
        #获取开团id
        gList=groupbookingList.groupBookingList(self,'苏珊15','8520014','course')
        item_id=gList[0]['gid']
        #参团支付页
        joinRs = previewBase.course_join_groupbooking(self,item_id)
        price = joinRs['item']['price']
        #拼团发起支付
        params = {'access_token': Token.get_token_login('苏珊15','123456'), 'type': 'join', 'gid': item_id, 'price': price,
                  'payInstru': 'weixin'}
        response = requests.post(self.base_url, params)
        res = response.json()
        self.assertEqual(res['state'], 'success')
        if res['state'] == 'success':
            order_number = res['order_number']
            fee = getOrderFee.getFee(str(res['id']))
            print(fee)
            # 虚拟支付
            virtualPayment.ketang_pay(self, order_number, fee)
            # 删除拼团
            deleteGroupBooking.delete('20271', '660')
            # 删除订单
            deleteOrder.delete(order_number)
            # 删除报名
            delSign.delete('20271', '660')
            delSign.delete('20064', '660')
            #删除拼团成员

        deleteOrder.delete(order_number1)

    def test_column_join_groupbooking(self):
        """专栏参团"""
        order_number1=''
        #开团
        # 获取支付页
        result = previewBase.column_groupbooking(self)
        gid = result['item']['groupbooking_set_id']
        price = result['item']['price']
        # 开团发起支付
        params = {'access_token': self.access_token, 'type': 'create', 'gid': gid, 'price': price,
                  'payInstru': 'weixin'}
        response = requests.post(self.base_url, params)
        re = response.json()
        self.assertEqual(re['state'], 'success')
        if re['state'] == 'success':
            order_number1 = re['order_number']
            fee = getOrderFee.getFee(str(re['id']))
            print(fee)
            # 虚拟支付
            virtualPayment.ketang_pay(self, order_number1, fee)
        #获取开团id
        gList=groupbookingList.groupBookingList(self,'苏珊15','57','column')
        item_id=gList[0]['gid']
        #参团支付页
        joinRs = previewBase.column_join_groupbooking(self,item_id)
        price = joinRs['item']['price']
        #拼团发起支付
        params = {'access_token': Token.get_token_login('苏珊15','123456'), 'type': 'join', 'gid': item_id, 'price': price,
                  'payInstru': 'weixin'}
        response = requests.post(self.base_url, params)
        res = response.json()
        self.assertEqual(res['state'], 'success')
        if res['state'] == 'success':
            order_number = res['order_number']
            fee = getOrderFee.getFee(str(res['id']))
            print(fee)
            # 虚拟支付
            virtualPayment.ketang_pay(self, order_number, fee)
            # 删除拼团
            deleteGroupBooking.delete('20271', '57')
            # 删除订单
            deleteOrder.delete(order_number)
             # 删除报名
            delSign.delete('20271', '57')
            delSign.delete('20064', '57')
        deleteOrder.delete(order_number1)

    def test_package_join_groupbooking(self):
        """课程包参团"""
        order_number1=''
        #开团
        # 获取支付页
        result = previewBase.package_groupbooking(self)
        gid = result['item']['groupbooking_set_id']
        price = result['item']['price']
        # 开团发起支付
        params = {'access_token': self.access_token, 'type': 'create', 'gid': gid, 'price': price,
                  'payInstru': 'weixin'}
        response = requests.post(self.base_url, params)
        re = response.json()
        self.assertEqual(re['state'], 'success')
        if re['state'] == 'success':
            order_number1 = re['order_number']
            fee = getOrderFee.getFee(str(re['id']))
            print(fee)
            # 虚拟支付
            virtualPayment.ketang_pay(self, order_number1, fee)
        #获取开团id
        gList=groupbookingList.groupBookingList(self,'苏珊15','1017','package')
        item_id=gList[0]['gid']
        #参团支付页
        joinRs = previewBase.package_join_groupbooking(self,item_id)
        price = joinRs['item']['price']
        #拼团发起支付
        params = {'access_token': Token.get_token_login('苏珊15','123456'), 'type': 'join', 'gid': item_id, 'price': price,
                  'payInstru': 'weixin'}
        response = requests.post(self.base_url, params)
        res = response.json()
        self.assertEqual(res['state'], 'success')
        if res['state'] == 'success':
            order_number = res['order_number']
            fee = getOrderFee.getFee(str(res['id']))
            print(fee)
            # 虚拟支付
            virtualPayment.ketang_pay(self, order_number, fee)
            # 删除拼团
            deleteGroupBooking.delete('20271', '1017')
            # 删除订单
            deleteOrder.delete(order_number)
             # 删除报名
            delSign.delete('20271', '1017')
            delSign.delete('20064', '1017')
        deleteOrder.delete(order_number1)
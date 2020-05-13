#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import testCase.common.getToken as Token
import testCase.ketang.vip.base.vipConfig as vipConfig

base_url='http://ke.test.mbalib.com/order/preview'
access_token = Token.get_token_login('sxs14', '123456')

#单课支付页
def course_preview(self):
    params = {'access_token': access_token, 'type': 'signup', 'item_type': 'course', 'item_id': '8520014'}
    response = requests.post(base_url, params)
    result = response.json()
    self.assertNotEqual(len(result['item']), 0)
    return result


#专栏支付页
def column_preview(self):
    params={'access_token':access_token,'type':'signup','item_type':'column','item_id':'259'}
    response=requests.post(base_url,params)
    result=response.json()
    print(result)
    self.assertNotEqual(len(result['item']),0)
    return result

#课程包支付页
def package_preview(self):
    params={'access_token':access_token,'type':'signup','item_type':'package','item_id':'1017'}
    response=requests.post(base_url,params)
    result=response.json()
    print(result)
    self.assertNotEqual(len(result['item']),0)
    return result

#单课赠礼支付页
def gift_course_preview(self):
    params = {'access_token': access_token, 'type': 'gift', 'item_type': 'course', 'item_id': '8520014'}
    response = requests.post(base_url, params)
    result = response.json()
    print(result)
    self.assertNotEqual(len(result['item']), 0)
    return result

#专栏赠礼支付页
def gift_column_preview(self):
    params = {'access_token': access_token, 'type': 'gift', 'item_type': 'column', 'item_id': '259'}
    response = requests.post(base_url, params)
    result = response.json()
    print(result)
    self.assertNotEqual(len(result['item']), 0)
    return result

#课程包赠礼支付页
def gift_package_preview(self):
    params = {'access_token': access_token, 'type': 'gift', 'item_type': 'package', 'item_id': '1017'}
    response = requests.post(base_url, params)
    result = response.json()
    print(result)
    self.assertNotEqual(len(result['item']), 0)
    return result

#课堂VIP会员支付页
def vip_preview(self):
    #获取会员配置
    data=vipConfig.get_vipConfig(self)
    if data!=None:
        item_id=data[0]['event_id']
        params = {'access_token': access_token, 'type': 'vip', 'item_type': 'package', 'item_id':item_id}
        response = requests.post(base_url, params)
        result = response.json()
        print(result)
        self.assertNotEqual(len(result['item']), 0)
        return result
    else:
        print('未有会员配置')
        return None

#单课开团支付页
def course_groupbooking(self):
    params = {'access_token': access_token, 'type': 'create_groupbooking', 'item_type': 'course', 'item_id': '8520014 '}
    response = requests.post(base_url, params)
    result = response.json()
    print(result)
    self.assertNotEqual(len(result['item']), 0)
    return result

#专栏开团支付页
def column_groupbooking(self):
    params = {'access_token': access_token, 'type': 'create_groupbooking', 'item_type': 'column', 'item_id': '57 '}
    response = requests.post(base_url, params)
    result = response.json()
    print(result)
    self.assertNotEqual(len(result['item']), 0)
    return result

#课程包开团支付页
def package_groupbooking(self):
    params = {'access_token': access_token, 'type': 'create_groupbooking', 'item_type': 'package', 'item_id': '1017 '}
    response = requests.post(base_url, params)
    result = response.json()
    print(result)
    self.assertNotEqual(len(result['item']), 0)
    return result

#单课参团支付页
def course_join_groupbooking(self,id):
    #参团
    params1 = {'access_token': Token.get_token_login('苏珊15','123456'), 'type': 'join_groupbooking', 'item_type': 'course', 'item_id': id}
    response = requests.post(base_url, params1)
    result1 = response.json()
    print(result1)
    self.assertNotEqual(len(result1['item']), 0)
    return result1

#专栏参团支付页
def column_join_groupbooking(self,id):
    #参团
    params1 = {'access_token': Token.get_token_login('sxs15','123456'), 'type': 'join_groupbooking', 'item_type': 'column', 'item_id': id}
    response = requests.post(base_url, params1)
    result1 = response.json()
    print(result1)
    self.assertNotEqual(len(result1['item']), 0)
    return result1

#专栏参团支付页
def package_join_groupbooking(self,id):
    #参团
    params1 = {'access_token': Token.get_token_login('苏珊15','123456'), 'type': 'join_groupbooking', 'item_type': 'package', 'item_id': id}
    response = requests.post(base_url, params1)
    result1 = response.json()
    print(result1)
    self.assertNotEqual(len(result1['item']), 0)
    return result1
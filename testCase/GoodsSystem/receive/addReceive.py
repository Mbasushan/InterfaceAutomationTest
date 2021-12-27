#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import testCase.GoodsSystem.receive.base.deleteReceiveBase as deleteReceiveBase
import testCase.GoodsSystem.receive.base.addReceiveBase as addReceiveBase
import testCase.GoodsSystem.receive.base.getReceiveListBase as getReceiveListBase

#添加收货地址
class AddReceive(unittest.TestCase):

    def setUp(self):
        self.base_url='http://www.test.mbalib.com/goods/receive/saveReceive'
        self.access_token = Token.getToken()

    def test_addReceive(self):
        """添加收货地址"""
        #添加收货地址
        receive_id=addReceiveBase.addReceive(self)
        #删除收货地址
        deleteReceiveBase.deleteReceive(self, receive_id)

    def test_saveReceive_noToken(self):
        """添加收货地址-未传token"""
        # 表单
        # 姓名
        name = '接口测试'
        # 电话
        mobile = '11111111111'
        # 省
        province = '350000'
        # 市
        city = '350200'
        # 区
        county = '350203'
        # 详细地址
        address = '软件园二期望海路59号之一'
        # 是否默认地址
        is_default = 0
        params = {'access_token': '', 'name': name, 'mobile': mobile, 'province': province, 'city': city,
                  'county': county, 'address': address, 'is_default': is_default}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'令牌错误')


    def test_saveReceive_noName(self):
        """添加收货地址-未传name"""
        # 表单
        # 姓名
        name = ''
        # 电话
        mobile = '11111111111'
        # 省
        province = '350000'
        # 市
        city = '350200'
        # 区
        county = '350203'
        # 详细地址
        address = '软件园二期望海路59号之一'
        # 是否默认地址
        is_default = 0
        params = {'access_token': self.access_token, 'name': name, 'mobile': mobile, 'province': province, 'city': city,
                  'county': county, 'address': address, 'is_default': is_default}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_saveReceive_noMobile(self):
        """添加收货地址-未传手机"""
        # 表单
        # 姓名
        name = '接口测试'
        # 电话
        mobile = ''
        # 省
        province = '350000'
        # 市
        city = '350200'
        # 区
        county = '350203'
        # 详细地址
        address = '软件园二期望海路59号之一'
        # 是否默认地址
        is_default = 0
        params = {'access_token': self.access_token, 'name': name, 'mobile': mobile, 'province': province, 'city': city,
                  'county': county, 'address': address, 'is_default': is_default}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_saveReceive_noProvince(self):
        """添加收货地址-未传省"""
        # 表单
        # 姓名
        name = '接口测试'
        # 电话
        mobile = '111111111'
        # 省
        province = ''
        # 市
        city = '350200'
        # 区
        county = '350203'
        # 详细地址
        address = '软件园二期望海路59号之一'
        # 是否默认地址
        is_default = 0
        params = {'access_token': self.access_token, 'name': name, 'mobile': mobile, 'province': province, 'city': city,
                  'county': county, 'address': address, 'is_default': is_default}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_saveReceive_noCity(self):
        """添加收货地址-未传市"""
        # 表单
        # 姓名
        name = '接口测试'
        # 电话
        mobile = '111111111'
        # 省
        province = '350000'
        # 市
        city = ''
        # 区
        county = '350203'
        # 详细地址
        address = '软件园二期望海路59号之一'
        # 是否默认地址
        is_default = 0
        params = {'access_token': self.access_token, 'name': name, 'mobile': mobile, 'province': province, 'city': city,
                  'county': county, 'address': address, 'is_default': is_default}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_saveReceive_noCounty(self):
        """添加收货地址-未传区"""
        # 表单
        # 姓名
        name = '接口测试'
        # 电话
        mobile = '111111111'
        # 省
        province = '350000'
        # 市
        city = '350200'
        # 区
        county = ''
        # 详细地址
        address = '软件园二期望海路59号之一'
        # 是否默认地址
        is_default = 0
        params = {'access_token': self.access_token, 'name': name, 'mobile': mobile, 'province': province, 'city': city,
                  'county': county, 'address': address, 'is_default': is_default}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_saveReceive_noAddress(self):
        """添加收货地址-未传详细地址"""
        # 表单
        # 姓名
        name = '接口测试'
        # 电话
        mobile = '111111111'
        # 省
        province = '350000'
        # 市
        city = '350200'
        # 区
        county = '350203'
        # 详细地址
        address = ''
        # 是否默认地址
        is_default = 0
        params = {'access_token': self.access_token, 'name': name, 'mobile': mobile, 'province': province, 'city': city,
                  'county': county, 'address': address, 'is_default': is_default}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_saveReceive_nois_default(self):
        """添加收货地址-未传是否默认地址"""
        # 表单
        # 姓名
        name = '接口测试'
        # 电话
        mobile = '11111111111'
        # 省
        province = '350000'
        # 市
        city = '350200'
        # 区
        county = '350203'
        # 详细地址
        address = '软件园二期望海路59号之一'
        # 是否默认地址
        is_default = 0
        params = {'access_token': self.access_token, 'name': name, 'mobile': mobile, 'province': province, 'city': city,
                  'county': county, 'address': address, 'is_default': ''}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        print("未传是否默认地址参数值，则默认为否")
        # 删除收货地址
        deleteReceiveBase.deleteReceive(self, result['data']['receive_id'])



    def test_saveReceive_errorMobile(self):
        """添加收货地址-输入错误的手机位数"""
        # 表单
        # 姓名
        name = '接口测试'
        # 电话
        mobile = '111111111'
        # 省
        province = '350000'
        # 市
        city = '350200'
        # 区
        county = '350203'
        # 详细地址
        address = '软件园二期望海路59号之一'
        # 是否默认地址
        is_default = 0
        params = {'access_token': self.access_token, 'name': name, 'mobile': mobile, 'province': province, 'city': city,
                  'county': county, 'address': address, 'is_default': ''}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'手机号码格式有误')

    def test_saveReceive(self):
        """修改收货地址"""
        #查找收货地址列表第一个地址
        receive = getReceiveListBase.get_receiveList(self)
        receive_id=''
        if len(receive['data']['list']) != 0:
            receive_id = receive['data']['list'][0]['receive_id']
        else:
            receive_id=addReceiveBase.addReceive(self)
        #修改姓名
        # 表单
        # 姓名
        name = '修改收货地址接口测试'
        # 电话
        mobile = '11111111111'
        # 省
        province = '350000'
        # 市
        city = '350200'
        # 区
        county = '350203'
        # 详细地址
        address = '软件园二期望海路59号之一'
        # 是否默认地址
        is_default = 0
        params = {'access_token': self.access_token, 'receive_id':receive_id,'name': name, 'mobile': mobile, 'province': province, 'city': city,
                  'county': county, 'address': address, 'is_default': is_default}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        savereceive = getReceiveListBase.get_receiveList(self)
        self.assertEqual(savereceive['data']['list'][0]['name'],'修改收货地址接口测试')

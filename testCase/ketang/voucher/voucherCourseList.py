#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as Token
import testCase.ketang.voucher.base.userVouchersListBase as userVouchersListBase

#优惠券下可用的课程列表
class VoucherCourseList(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/api/voucherCourseList"
        self.access_token=Token.get_token_login('sxs14','123456')

    def test_voucherExcept(self):
        """优惠券下可用的课程列表"""
        keys=userVouchersListBase.userVoucherList(self)
        for i in range(len(keys)):
            response=requests.get(self.base_url,params={'key':keys[i]})
            result=response.json()
            self.assertEqual(result['state'],'success')
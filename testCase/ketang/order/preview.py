#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import unittest
import requests
import testCase.common.getToken as Token
import testCase.ketang.order.base.previewBase as previewBase


#支付页
class Preview(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/order/preview"

    def test_course_preview(self):
        """单课支付页"""
        result=previewBase.course_preview(self)


    def test_column_preview(self):
        """专栏支付页"""
        result =previewBase.column_preview(self)

    def test_package_preview(self):
        """课程包支付页"""
        result =previewBase.package_preview(self)

    def test_gift_course_preview(self):
        """单课赠礼支付页"""
        result =previewBase.gift_course_preview(self)

    def test_gift_column_preview(self):
        """专栏赠礼支付页"""
        result =previewBase.gift_column_preview(self)

    def test_gift_package_preview(self):
        """课程包赠礼支付页"""
        result =previewBase.gift_package_preview(self)

    def test_vip_preview(self):
        """课堂VIP会员支付页"""
        result =previewBase.vip_preview(self)

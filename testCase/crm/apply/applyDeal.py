#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token
import testCase.crm.apply.base.getApplyList as getApplyList

#通知处理
class ApplyDeal(unittest.TestCase):

    def setUp(self):
        self.base_url='http://crm.test.mbalib.com/apply/applyDeal'
        self.access_token=Token.getToken()

    def test_apply_deal(self):
        """通知处理-处理通过"""
        #获取未处理通知
        list=getApplyList.get_apply_list(self,self.access_token,'1')
        if list!=None:
            i=0
            for i in range(len(list)):
                id=list[i]['apply_id']
                params={'access_token':self.access_token,'apply_id':id,'result':'pass'}
                response=requests.post(self.base_url,params)
                result=response.json()
                print(result)
                self.assertEqual(result['state'],'success')

        else:
            print('未有未处理通知')

    def test_apply_deal_noToken(self):
        """通知处理-未传token"""
        params={'access_token':'','apply_id':1,'result':'pass'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'令牌错误')

    def test_apply_deal_noId(self):
        """通知处理-未传id"""
        params={'access_token':self.access_token,'apply_id':'','result':'pass'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_apply_deal_noResult(self):
        """通知处理-未传result"""
        params={'access_token':self.access_token,'apply_id':'1','result':''}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')
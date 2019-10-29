#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import testCase.common.getToken as Token

#删除成员
def delete_member(self,member_id):
    url='http://crm.test.mbalib.com/member/deleteMember'
    access_token=Token.getToken()
    response=requests.post(url,params={'access_token':access_token,'member_id':member_id})
    result=response.json()
    print(result)
    self.assertEqual(result['state'], 'success')
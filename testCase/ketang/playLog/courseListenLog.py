#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as getToken
#课程播放日志

class CourseListen(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://ke.test.mbalib.com/api/CourseListen"

    def test_courseListen_log(self):
        """课程播放日志"""
        access_token=getToken.getToken()
        params={"access_token":access_token,"id":639}
        response=requests.post(self.base_url,params=params)
        result=response
        print("因为未有返回值")
        print(result)

    def test_courseListen_log_noToke(self):
        """课程播放日志-未有token"""
        params={"id":639}
        response=requests.post(self.base_url,params=params)
        result=response
        print("因为未有返回值")
        print(result)

    def test_courseListen_log_noID(self):
        """课程播放日志-未有课程id"""
        access_token = getToken.getToken()
        params = {"access_token": access_token}
        response=requests.post(self.base_url,params=params)
        result=response
        print("因为未有返回值")
        print(result)
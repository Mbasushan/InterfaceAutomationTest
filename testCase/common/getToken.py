#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#获取登录的token
import json

import requests


def getToken():
    url = 'http://passport.test.mbalib.com/api/login'
    header = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    data = {'username': 'Sxs1', 'password': '123456'}
    response = requests.post(url, headers=header, data=data)
    your_dict = json.loads(response.text)
    # 返回token
    token = your_dict["access_token"]
    return token


#输入账号，密码获取token
def get_token_login(username,password):
    url = 'http://passport.test.mbalib.com/api/login'
    header = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    data = {'username': username, 'password':password}
    response = requests.post(url, headers=header, data=data)
    your_dict = json.loads(response.text)
    # 返回token
    token = your_dict["access_token"]
    return token
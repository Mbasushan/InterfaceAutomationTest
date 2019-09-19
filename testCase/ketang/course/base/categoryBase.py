#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests

#获取课程分类
def get_categoryId(self):
    url='http://ke.test.mbalib.com/api/getcategory'
    response=requests.get(url)
    result=response.json()
    ids=[]
    for i in range(len(result['data'])):
        if i>0:
            ids.append(result['data'][i]['cid'])
    self.assertEqual(result['state'],'success')
    return ids
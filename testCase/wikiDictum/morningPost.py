#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.isValidImge as isValidImage

#智库早报-线上数据
class MorningPost(unittest.TestCase):

    def setUp(self):
        self.base_url='http://news.mbalib.com/api/articleList'

    def test_morningPost(self):
        """智库早报-线上数据"""
        params={'type':'morningPost'}
        response = requests.get(self.base_url,params)
        result = response.json()
        print(result)
        size=len(result['data'])
        #判断获取到的数据是否是早报,取10条数据就可以
        i = 0
        data=result['data']
        for i in range(10) :
            category=data[i]['category']
            if category=='早报':
                print("该资讯是早报")
                #获取分享图片
                imge=data[i]['article_image']
                print("生成的图片地址：",imge)
                #判断图片是否损坏
                flag=isValidImage.is_valid(imge)
                print("判断图片是否损坏:",flag)
                i=i+1
                self.assertEqual(flag,False)
            else:
                print("该资讯不是早报")
                break


#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as geToken
import db_fixture.mysql_db as mySqlConnect
import datetime

#大咖会员开通配置
class MemberPrice(unittest.TestCase):

    def setUp(self):
        self.base_url="http://www.test.mbalib.com/appaudio/MemberPrice"

    def test_getMemberPrice_H5(self):
        """大咖会员开通配置-客户端:h5"""
        origin='h5'
        response=requests.get(self.base_url,params={'origin':origin})
        result=response.json()
        self.assertEqual(result['state'],'success')
        print("客户端：h5的会员配置项数量：", len(result['data']))
        size=count(origin)
        self.assertEqual(len(result['data']), size)

    def test_getMemberPrice_ios_wiki(self):
        """大咖会员开通配置-客户端:wiki"""
        origin='wiki'
        response=requests.get(self.base_url,params={'origin':origin})
        result=response.json()
        self.assertEqual(result['state'],'success')
        print("客户端：ios-普通版的会员配置项数量：", len(result['data']))
        size=count(origin)
        self.assertEqual(len(result['data']), size)

    def test_getMemberPrice_ios_wikifresh(self):
        """大咖会员开通配置-客户端:wikifresh"""
        origin='wikifresh'
        response=requests.get(self.base_url,params={'origin':origin})
        result=response.json()
        self.assertEqual(result['state'],'success')
        print("客户端：ios-专业版的会员配置项数量：", len(result['data']))
        size=count(origin)
        self.assertEqual(len(result['data']), size)

    def test_getMemberPrice_android(self):
        """大咖会员开通配置-客户端:android"""
        origin='android'
        response=requests.get(self.base_url,params={'origin':origin})
        result=response.json()
        self.assertEqual(result['state'],'success')
        print("客户端：Android的会员配置项数量：",len(result['data']))
        size=count(origin)
        self.assertEqual(len(result['data']), size)

    def test_getMemberPrice_noOrigin(self):
        """大咖会员开通配置-未传客户端"""
        response=requests.get(self.base_url)
        result=response.json()
        self.assertEqual(result['state'],'success')
        print(len(result['data']))
        size=count('')
        self.assertEqual(len(result['data']), size)

#获取会员配置在数据库中的总数
def count(origin):
    #获取当前时间
    time=datetime.datetime.now().strftime('%Y-%m-%d hh:mm:ss')
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query=''
    if origin=="":
        query = "SELECT COUNT(*) FROM wiki_audio_member_config WHERE mc_state=1 AND mc_endtime>='"+time+"'"
    elif origin=="wiki" or origin=='wikifresh':
        query="SELECT COUNT(*) FROM wiki_audio_member_config WHERE mc_state=1 AND mc_client=2 and mc_endtime>='"+time+"'"
    elif origin=='android':
        query="SELECT COUNT(*) FROM wiki_audio_member_config WHERE mc_state=1 AND mc_client=3 and mc_endtime>='"+time+"'"
    elif origin=='h5':
        query = "SELECT COUNT(*) FROM wiki_audio_member_config WHERE mc_state=1 AND mc_client=4 and mc_endtime>='"+time+"'"
    cs1.execute(query)
    count = cs1.fetchall()[0][0]
    return count
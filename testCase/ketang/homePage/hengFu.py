#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#首页轮播图和横幅广告
import unittest
from datetime import datetime, date, timedelta
import requests
import db_fixture.mysql_db as mySqlConnect

def getTime():
    # 获取当前日期
    nowTime = datetime.now().strftime('%Y%m%d')
    oldTime = (date.today() + timedelta(days=-1)).strftime("%Y%m%d")
    return nowTime,oldTime


#连接数据库
def connects():
    time=getTime()
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询首页横幅广告
    query = "SELECT * FROM web_ad WHERE ad_type='ketang_hengfu' AND ad_endtime >='" + time[0] + "'"
    cs1.execute(query)
    data = cs1.fetchall()
    return data


class HengFu(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://www.test.mbalib.com/appwiki/ad"

    def test_ios(self):
        """ios课堂首页横幅广告"""
        response = requests.get(self.base_url, params={'type': 'ketang_hengfu', 'channel': 'ios', 'purge': 'ture'})
        text = response.json()
        print(text)

    def test_ios_fresh(self):
        """ios专业版课堂首页横幅广告"""
        response = requests.get(self.base_url, params={'type': 'ketang_hengfu', 'channel': 'ios_fresh', 'purge': 'ture'})
        text = response.json()
        print(text)

    def test_android(self):
        """Android课堂首页横幅广告"""
        response = requests.get(self.base_url, params={'type': 'ketang_hengfu', 'channel': 'android', 'purge': 'ture'})
        text = response.json()
        print(text)

    def test_pc(self):
        """pc课堂首页横幅广告-有数据"""
        time = getTime()
        data = connects()
        print("data:",len(data))
        if len(data)==0:
            # 连接数据库
            conn = mySqlConnect.my_db()
            # 获取cursor对象
            cs1 = conn.cursor()
            # 查询首页横幅广告
            query = "update web_ad set ad_endTime='" + time[0] + "' where ad_type='ketang_hengfu' and ad_endTime < '" + time[0] + "'"  # 需要执行的sql语句
            try:
                cs1.execute(query)
                conn.commit()
            except:
                conn.rollback()
            # 关闭cursor对象
            cs1.close()
            # 关闭connection对象
            conn.close()
        response = requests.get(self.base_url, params={'type':'ketang_hengfu','channel':'ke','purge':'ture'})
        text =response.json()
        print(text)

    def test_ke1_null(self):
        """首页横幅广告-无数据"""
        #数据库把横幅广告置为取消
        time = getTime()
        data=connects()
        if len(data)!=0:
            print("有数据，修改数据")
            #连接数据库
            conn=mySqlConnect.my_db()
            # 获取cursor对象
            cs1 = conn.cursor()
            #查询首页横幅广告
            query = "update web_ad set ad_endTime='"+time[1]+"' where ad_type='ketang_hengfu' and ad_endTime >='"+time[0]+"'" # 需要执行的sql语句
            try:
                cs1.execute(query)
                conn.commit()
            except:
                conn.rollback()
            # 关闭cursor对象
            cs1.close()
            # 关闭connection对象
            conn.close()
            response = requests.get(self.base_url, params={'type':'ketang_hengfu','channel':'ke','purge':'ture'})
            text = response.json()
            print("text:",text)
        else:
            print("未有横幅广告")



    if __name__ == '__main__':
        unittest.main()
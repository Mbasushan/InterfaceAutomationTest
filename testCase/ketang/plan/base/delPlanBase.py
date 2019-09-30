#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import db_fixture.mysql_db as mySqlConnect

#删除计划
def delete_plan(planId):
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "delete FROM ketang_plan WHERE plan_id='"+planId+"'"
    try:
        cs1.execute(query)
        conn.commit()
    except:
        conn.rollback()

    # 查询主题信息
    sql = "delete FROM ketang_plan_day WHERE pd_plan_id='" + planId + "';delete FROM ketang_plan_material WHERE pm_plan_id='" + planId + "'"
    try:
        cs1.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    # 关闭cursor对象
    cs1.close()
    # 关闭connection对象
    conn.close()
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import db_fixture.mysql_db as mySqlConnect

#删除代理商
def delete_crm(agent_id):
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "delete FROM crm_agent WHERE agent_id='"+agent_id+"'"
    try:
        cs1.execute(query)
        conn.commit()
    except:
        conn.rollback()
    # 关闭cursor对象
    cs1.close()
    # 关闭connection对象
    conn.close()
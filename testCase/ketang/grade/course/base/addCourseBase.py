#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import testCase.common.getToken as Token
import db_fixture.mysql_db as mySqlConnect


#添加班级课程
def add_course(self):
    url='http://ke.test.mbalib.com/class/addCourse'
    access_token = Token.getToken()
    list = '[{"item_type":"course", "item_id":8535103},{"item_type":"column", "item_id":73},{"item_type":"package", "item_id":1001}]'
    params = {'access_token': access_token, 'class_id': 1002, 'course_list': list}
    response = requests.post(url, params)
    result = response.json()
    print(result)
    flag = selectFlag()
    self.assertEqual(flag, True)

#查找数据库是否添加成功
def selectFlag():
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "SELECT COUNT(*) FROM ketang_class_course WHERE cc_class_id=41"
    cs1.execute(query)
    result = cs1.fetchall()[0][0]
    if int(result)!=0:
        return True
    else:
        return False
import db_fixture.mysql_db as mySqlConnect

#删除
def delete(id,courseId):
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "DELETE FROM ketang_course_signup WHERE signup_user_id='" + id + "'and signup_course_id='"+courseId+"'"
    try:
        cs1.execute(query)
        conn.commit()
    except:
        conn.rollback()
    # 关闭cursor对象
    cs1.close()
    # 关闭connection对象
    conn.close()
import db_fixture.mysql_db as mySqlConnect

#根据订单查询订单支付金额
def getFee(id):   #id 订单号  fee  金额
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "select order_real_amount FROM ketang_order WHERE order_id='" + id + "'"
    cs1.execute(query)
    results = cs1.fetchall()
    fee=results[0][0]
    return fee
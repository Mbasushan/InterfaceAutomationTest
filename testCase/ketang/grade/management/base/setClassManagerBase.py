import requests
import testCase.common.getToken as Token
import db_fixture.mysql_db as mySqlConnect

def setClassManager_admin(self,token):
    url='http://ke.test.mbalib.com/class/setClassManager'
    params = {'access_token': token, 'class_id': 1079, 'set_user_id': 20314, 'role': 'admin'}
    response = requests.post(url, params)
    result = response.json()
    print(result)
    role = select_role()
    self.assertEqual('admin', role)

#查询
def select_role():
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "SELECT member_role FROM ketang_class_member WHERE member_user_id='20314' AND member_class_id=140"
    cs1.execute(query)
    isjoin = cs1.fetchall()
    return isjoin[0][0]
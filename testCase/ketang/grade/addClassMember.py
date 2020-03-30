import requests
import unittest
import testCase.common.getToken as Token
import db_fixture.mysql_db as mySqlConnect

#添加成员-导入手机号
class AddClassMember(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/class/addClassMember'
        self.access_token=Token.getToken()

    def test_AddClassMember(self):
        """添加成员-导入手机号"""
        params={'access_token':self.access_token,'class_key':1000,'mobiles':'18113459825,13106445986,159620'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['illegel_count'],1)
        self.assertEqual(result['unregistered_count'],1)
        self.assertEqual(result['success_count'],1)
        #删除已添加成功的成员
        delect()

    def test_AddClassMember_noToken(self):
        """添加成员-导入手机号-未登录"""
        params={'access_token':'','class_key':1000,'mobiles':'18113459825,13106445986,159620'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_AddClassMember_noKey(self):
        """添加成员-导入手机号-未传班级id"""
        params={'access_token':self.access_token,'class_key':'','mobiles':'18113459825,13106445986,159620'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_AddClassMember_noMobiles(self):
        """添加成员-导入手机号-未传手机号"""
        params={'access_token':self.access_token,'class_key':1000,'mobiles':''}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'],'参数错误')

    def test_AddClassMember_Mobiles(self):
        """添加成员-导入手机号-手机号格式不对，输入中文"""
        params={'access_token':self.access_token,'class_key':1000,'mobiles':'收到'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['illegel_count'], 1)

def delect():
    # 连接数据库
    conn = mySqlConnect.my_db()
    # 获取cursor对象
    cs1 = conn.cursor()
    # 查询主题信息
    query = "delete FROM ketang_class_member WHERE member_user_id='20093'"
    try:
        cs1.execute(query)
        conn.commit()
    except:
        conn.rollback()
    # 关闭cursor对象
    cs1.close()
    # 关闭connection对象
    conn.close()
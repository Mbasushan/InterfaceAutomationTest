import requests
import unittest
import testCase.common.getToken as Token


#学习之星
class StudyStarList(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/class/studyStarList'
        self.access_token=Token.getToken()

    def test_getStrive(self):
        """学习之星努力榜-默认获取数量为10条"""
        params={'access_token':self.access_token,'class_key':'1000','type':'strive'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)

    def test_getAchievement(self):
        """学习之星成果榜-默认获取数量为10条"""
        params={'access_token':self.access_token,'class_key':'1000','type':'achievement'}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)

    def test_getStrive_noJoin(self):
        """学习之星努力榜-不是该班级成员"""
        params = {'access_token': Token.get_token_login('sxs15','123456'), 'class_key': '1000', 'type': 'strive'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)

    def test_getStrive_noToken(self):
        """学习之星努力榜-未登录"""
        params = {'access_token':'', 'class_key': '1000', 'type': 'strive'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')

    def test_getAchievement_noToken(self):
        """学习之星成果榜-未登录"""
        params = {'access_token':'', 'class_key': '1000', 'type': 'achievement'}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'],'获取账号信息失败')
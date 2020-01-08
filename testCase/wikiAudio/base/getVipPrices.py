import requests
import testCase.common.getToken as geToken

#获取大咖商品项，origin  客户端
def getVip_prices(self,origin):
    url='http://www.test.mbalib.com/appaudio/MemberPrice'
    response=requests.get(url,params={'origin':origin})
    result=response.json()
    self.assertEqual(result['state'],'success')
    return result['data']
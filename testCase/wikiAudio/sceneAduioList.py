#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
import requests
import testCase.common.getToken as getToken

#大咖场景音频列表
class SceneAduioList(unittest.TestCase):

    def setUp(self):
        self.base_url='http://www.test.mbalib.com/appaudio/sceneaudio'

    def test_getSceneAduioList(self):
        """大咖场景音频列表-用户是非vip"""
        sceneList=get_sceneIdList()
        for i in range(len(sceneList)):
            scene_id=sceneList[i]
            params={"scene_id":scene_id,"member":"no"}
            response = requests.get(self.base_url,params)
            reslut = response.json()
            print("场景音频数:",len(reslut['data']))
            self.assertEqual(reslut['count'],len(reslut['data']))
            print("场景下的音频详情：")
            for s in range(len(reslut['data'])):
                if len(reslut['data'])!=0:
                    if int(reslut['data'][s]['audition'])==0:
                        self.assertEqual(reslut['data'][s]['url'],"")
                        print("该音频为非试听,音频id为",reslut['data'][s]['aId'])
                    else:
                        print("该音频为试听，音频id为",reslut['data'][s]['aId'])

    def test_getSceneAduioList_vip(self):
        """大咖场景音频列表-用户是vip"""
        sceneList=get_sceneIdList()
        access_token=getToken.getToken()
        for i in range(len(sceneList)):
            scene_id=sceneList[i]
            params={"scene_id":scene_id,"member":"yes","access_token":access_token}
            response = requests.get(self.base_url,params)
            reslut = response.json()
            print("场景音频数:",len(reslut['data']))
            self.assertEqual(reslut['count'],len(reslut['data']))
            print("场景下的音频详情：")
            for s in range(len(reslut['data'])):
                if len(reslut['data'])!=0:
                    print(reslut['data'])
                    if int(reslut['data'][s]['audition'])==1:
                        print("该音频id为",reslut['data'][s]['aId'],"url:",reslut['data'][s]['url'])
                    else:
                        print("vip")
                        print("该音频id为", reslut['data'][s]['aId'], "url:", reslut['data'][s]['url'])

    def test_getSceneAduioList_noSceneId(self):
        """大咖场景音频列表-不传场景Id"""
        params={"member":"yes"}
        response = requests.get(self.base_url,params)
        reslut = response.json()
        self.assertEqual(reslut['count'],0)

    def test_getSceneAduioList_noToken(self):
        """大咖场景音频列表-member是yes,未传token"""
        sceneList=get_sceneIdList()
        for i in range(len(sceneList)):
            scene_id=sceneList[i]
            params={"scene_id":scene_id,"member":"yes"}
            response = requests.get(self.base_url,params)
            reslut = response.json()
            print("场景音频数:",len(reslut['data']))
            self.assertEqual(reslut['count'],len(reslut['data']))
            print("场景下的音频详情：")
            for s in range(len(reslut['data'])):
                if len(reslut['data'])!=0:
                    print(reslut['data'])
                    if int(reslut['data'][s]['audition'])==1:
                        self.assertNotEqual(reslut['data'][s]['url'], "")
                        #print("该音频非vip,id为",reslut['data'][s]['aId'],"url:",reslut['data'][s]['url'])
                    else:
                        self.assertEqual(reslut['data'][s]['url'],"")
                        #print("该音频为vip，id为", reslut['data'][s]['aId'], "url:", reslut['data'][s]['url'])

#获取所有场景的音频
def get_sceneIdList():
    url='http://www.test.mbalib.com/appaudio/scene'
    response=requests.get(url)
    reslut=response.json()
    sceneList=[]
    for i in range(len(reslut['data'])):
        sceneList.append(reslut['data'][i]['scene_id'])
    return sceneList
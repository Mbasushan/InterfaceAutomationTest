#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import unittest
import testCase.common.getToken as Token
import testCase.ketang.grade.course.base.deleteCourseBase as deleteCourseBase
import testCase.ketang.grade.course.base.addCourseBase as addCourseBase



#添加班级课程
class AddCourse(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/class/addCourse'

    def test_addCourse(self):
        """添加班级课程"""
        access_token=Token.getToken()
        list='[{"item_type":"course", "item_id":8535103},{"item_type":"column", "item_id":73},{"item_type":"package", "item_id":1001}]'
        params={'access_token':access_token,'class_id':1002,'course_list':list}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        flag=addCourseBase.selectFlag()
        self.assertEqual(flag,True)
        #删除
        deleteCourseBase.delete_course(self)


    def test_addCourse_noToken(self):
        """添加课程---未登录"""
        list = '[{"item_type":"course", "item_id":8535103},{"item_type":"column", "item_id":73},{"item_type":"package", "item_id":1001}]'
        params = {'access_token': "", 'class_id': 1002, 'course_list': list}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')

    def test_addCourse_noClassId(self):
        """添加课程---未传classId"""
        access_token=Token.getToken()
        list = '[{"item_type":"course", "item_id":8535103},{"item_type":"column", "item_id":73},{"item_type":"package", "item_id":1001}]'
        params = {'access_token': access_token, 'course_list': list}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')


    def test_addCourse_noCourse_list(self):
        """添加课程---未传课程Id"""
        access_token=Token.getToken()
        params = {'access_token': access_token, 'class_id': 1002}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')


    def test_addCourse_noJoinClass(self):
        """添加班级课程---未加入该班级"""
        access_token=Token.get_token_login('sxs14','123456')
        list='[{"item_type":"course", "item_id":8535103},{"item_type":"column", "item_id":73},{"item_type":"package", "item_id":1001}]'
        params={'access_token':access_token,'class_id':1002,'course_list':list}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '您没有权限进行操作')


    def test_addCourse_normal(self):
        """添加班级课程---普通成员"""
        access_token=Token.get_token_login('苏珊11','123456')
        list='[{"item_type":"course", "item_id":8535103},{"item_type":"column", "item_id":73},{"item_type":"package", "item_id":1001}]'
        params={'access_token':access_token,'class_id':1002,'course_list':list}
        response=requests.post(self.base_url,params)
        result=response.json()
        print(result)
        self.assertEqual(result['error'], '您没有权限进行操作')




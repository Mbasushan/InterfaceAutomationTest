#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import json

import requests
import unittest
import testCase.common.getToken as Token
import testCase.ketang.grade.course.base.deleteCourseBase as deleteCourseBase
import testCase.ketang.grade.course.base.addCourseBase as addCourseBase


#删除班级课程
class DelCourse(unittest.TestCase):

    def setUp(self):
        self.base_url='http://ke.test.mbalib.com/class/delCourse'

    def test_delCourse(self):
        """删除班级课程"""
        deleteCourseBase.delete_course(self)

    def test_delCourse_noToken(self):
        """删除班级课程---未登录"""
        #添加课程
        addCourseBase.add_course(self)
        #查询获取班级课程id
        list = json.dumps(deleteCourseBase.selece_courseId())
        #删除
        params = {'access_token': "", 'class_id': 1002, 'cc_list': list}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '获取账号信息失败')
        deleteCourseBase.delete_course(self)

    def test_delCourse_noClassId(self):
        """删除班级课程---未传classId"""
        # 添加课程
        addCourseBase.add_course(self)
        # 查询获取班级课程id
        list = json.dumps(deleteCourseBase.selece_courseId())
        # 删除
        access_token=Token.getToken()
        params = {'access_token': access_token,  'cc_list': list}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')
        deleteCourseBase.delete_course(self)

    def test_delCourse_noCClist(self):
        """删除班级课程---未传班级课程ID"""
        access_token = Token.getToken()
        params = {'access_token': access_token, 'class_id': 1002}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '参数错误')


    def test_delCourse_normal(self):
        """删除班级课程---普通成员"""
        #添加课程
        addCourseBase.add_course(self)
        #查询获取班级课程id
        list = json.dumps(deleteCourseBase.selece_courseId())
        #删除
        access_token=Token.get_token_login('苏珊11','123456')
        params = {'access_token': access_token, 'class_id': 1002, 'cc_list': list}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '您没有权限进行操作')
        deleteCourseBase.delete_course(self)

    def test_delCourse_noJoinClass(self):
        """删除班级课程---不是该班级成员"""
        # 添加课程
        addCourseBase.add_course(self)
        # 查询获取班级课程id
        list = json.dumps(deleteCourseBase.selece_courseId())
        # 删除
        access_token = Token.get_token_login('sxs14', '123456')
        params = {'access_token': access_token, 'class_id': 1002, 'cc_list': list}
        response = requests.post(self.base_url, params)
        result = response.json()
        print(result)
        self.assertEqual(result['error'], '您没有权限进行操作')
        deleteCourseBase.delete_course(self)
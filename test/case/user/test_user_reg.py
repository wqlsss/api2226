#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/18 14:37
# Author : xiaowei
# @File : test_user_reg.py
# @Software : PyCharm
import unittest
import requests
from lib.db1 import * # 导入db.py文件
# 数据准备
NOT_EXIST_USER = 'peter'
EXIST_USER = 'student'
class TestUserReg(unittest.TestCase):
     url = 'http://127.0.0.1:8000/api/student/user/register'
     def test_user_reg_normal(self):
         # 环境检查
         if check_user(NOT_EXIST_USER):
            del_user(NOT_EXIST_USER)
         # 发送请求
         data = {'userName': NOT_EXIST_USER, 'password': '123456',"userLevel": 1}
         res = requests.post(url=self.url, json=data)
         # 期望响应结果,注意字典格式和json格式的区别(如果有true/false/null要转化为字典格式)
         except_res = {
         "code": 1,
         "message": "成功",
         "response": None
         }
         # 响应断言(整体断言)
         self.assertDictEqual(res.json(), except_res)
         # 数据库断言
         self.assertTrue(check_user(NOT_EXIST_USER))
         # 环境清理(由于注册接口向数据库写入了用户信息)
         del_user(NOT_EXIST_USER)
     def test_user_reg_exist(self):
         # 环境检查
         if not check_user(EXIST_USER):
            add_user(EXIST_USER)
         # 发送请求
         data = {'userName': EXIST_USER, 'password': '123456',"userLevel": 1}
         res = requests.post(url=self.url, json=data)
         # 期望响应结果,注意字典格式和json格式的区别(如果有true/false/null要转化为字典格式)
         except_res = {
         "code": 2,
         "message": '用户已存在',

         'response': None
         }
         # 响应断言(整体断言)
         self.assertDictEqual(res.json(), except_res)
         # 数据库断言(没有注册成功,数据库没有添加新用户)
         # 环境清理(无需清理)
if __name__ == '__main__':
 unittest.main(verbosity=2) # 运行所有用例
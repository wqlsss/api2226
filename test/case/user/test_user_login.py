#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2024/5/6 16:58
# Author     : smart
# @File      : test_user_login.py
# @Software  : PyCharm
from test.case.basecase import BaseCase
class test_user_login(BaseCase):
    def test_login_success(self):
        '''level1:正常登录'''
        case_data = self.get_case_data("login_ok")
        self.send_request(case_data)
    def test_login_fail1(self):
        case_data = self.get_case_data("login_err1")
        self.send_request(case_data)
    def test_login_fail2(self):
        case_data = self.get_case_data("login_err2")
        self.send_request(case_data)

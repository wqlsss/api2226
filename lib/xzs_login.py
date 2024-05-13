#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/18 14:15
# Author : xiaowei
# @File : xzs_login.py
# @Software : PyCharm
import requests

class xzs_login():
    def login(self,user,ps):
        url = "http://192.168.55.1:8000/api/user/login"
        header = {
            "content-type": "application/json"
        }
        data={
            "userName": user, "password": ps, "remember": False
        }
        r = requests.post(url=url, headers=header, json=data)
        return r.text

if __name__ == '__main__':
    x =xzs_login()
    print(x.login("", "123456"))
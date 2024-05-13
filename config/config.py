#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2024/4/26 15:03
# Author     : smart
# @File      : config.py
# @Software  : PyCharm
import logging
import os

# 项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(prj_path,"data")
test_path = os.path.join(prj_path,"test")
test_case_path = os.path.join(prj_path,'test','case')
log_file = os.path.join(prj_path, 'log',"log.txt")
report_file = os.path.join(prj_path, 'report',"report.html")
data_file = os.path.join(prj_path,"data","test_user_data.xlsx")
test_list_file = os.path.join(prj_path,"test","test_list.txt")
last_fails_file = os.path.join(prj_path,'last_fails.pickle')
# log文件配置
logging.basicConfig(
     level=logging.DEBUG, # log level
     format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s', # log格式
     datefmt='%Y-%m-%d %H:%M:%S', # 日期格式
     filename=log_file, # 日志输出文件
     # encoding='utf-8',
     filemode='a'
)
# 数据库配置
db_host = '127.0.0.1'
db_port = 3306
db_user = 'root'
db_ps = 'root'
db = 'xzs'

# 邮件配置
smtp_server = 'smtp.qq.com'
smtp_user = '1705158296@qq.com'
smtp_ps = 'epgyuewydtumbehd'
sender = smtp_user
receiver = '1705158296@qq.com'
subject = '接口测试报告'


if __name__ == '__main__':
    logging.info("接口测试")
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/27 8:30
# Author : xiaowei
# @File : send_email_base.py
# @Software : PyCharm
#用于建立smtp连接
import smtplib
# 邮件需要专门的MIME格式
from email.mime.text import MIMEText
# plain指普通文本格式邮件内容
msg = MIMEText('今天是个好天气','plain',"utf-8")
# 发件人
msg['From']='252553516@qq.com'
# 收件人
msg['To']='252553516@qq.com'
# 邮件的标题
msg['Subject']='邮件标题-不想上班'

smtp =smtplib.SMTP_SSL('smtp.qq.com')
smtp.login('252553516@qq.com','txekllcllwihbgbh')
smtp.sendmail("252553516@qq.com","252553516@qq.com",msg.as_string())
smtp.quit()

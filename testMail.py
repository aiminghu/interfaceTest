#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/20 0020 下午 16:39 
# @Author : aiminhu
# @File : testMail.py 
# @Software: PyCharm
from email.mime.text import MIMEText
import smtplib
'''
smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
这里是上面语法的参数细节 -
host - 这是运行SMTP服务器的主机。可以指定主机的IP地址或类似yiibai.com的域名。这是一个可选参数。
port - 如果提供主机参数，则需要指定SMTP服务器正在侦听的端口。通常这个端口默认值是：25。
local_hostname - 如果SMTP服务器在本地计算机上运行，那么可以只指定localhost选项。

SMTP对象有一个sendmail的实例方法，该方法通常用于执行邮件发送的工作。它需要三个参数 -
sender - 具有发件人地址的字符串。
receivers - 字符串列表，每个收件人一个。
message - 作为格式如在各种RFC中指定的字符串。

'''

smtpObj = smtplib.SMTP([])
smtplib
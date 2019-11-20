#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/9 0009 下午 23:35 
# @Author : aiminhu
# @File : configEmail.py 
# @Software: PyCharm
'''
功能：
    1.读配置
    2.配置附件
    3.连接
    4.发送邮件

'''
import  smtplib,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from common.readConfig import ReadConfig


class ConfigEmail():
    #读取文件的配置属性
    r = ReadConfig()
    mail_host = r.get_email('mail_host')

    #配置第三方SMTP服务
    # mail_host = "smtp.126.com" #设置服务器
    mail_user = r.get_email('mail_user') #用户名
    mail_pass = r.get_email("mail_pass") #口令

    #配置邮件属性
    sender = r.get_email('sender')
    receivers = r.get_email('receiver') #接收邮箱
    content = r.get_email('content')
    msg = MIMEMultipart()

    def config_file(self):
        #配置附件属性
        file = self.find_file()


    def find_file(self):
        '''查找最新文件'''
        #获取当前路径
        current_path = os.path.dirname(os.path.abspath(__file__))
        # print(current_path)
        #获取报告的存放路径
        filePath = os.path.dirname(current_path) + '\\' + 'report'
        # print('filepath:',filePath)

        #获取filepath路径下全部文件名称的列表
        fileList = os.listdir(filePath)
        # print(filePath)

        fileDict = {}
        fileTime = []

        for iName in fileList:
            #拼接文件路径和文件名
            filename = filePath + '/' + iName
            #获取该文件的修改时间
            iTime = os.path.getmtime(filename)
            #将该文件的修改时间追加到时间列表中
            # print(iTime)
            fileTime.append(iTime)
            #将文件名iname作为字典的value，文件修改的时间iTime作为字典的key存入
            fileDict[iTime] = iName
        # print(fileDict,fileTime)

        sendfilekey = max(fileTime)
        sendfile = fileDict[sendfilekey]
        # print(sendfile)
        sendfile = filePath + '/' + sendfile
        # print(sendfile)
        return sendfile

    #发送邮件
    def send_mail(self):
        self.config_file()
        try:
            s = smtplib.SMTP()
            # print(self.mail_host,self.mail_user,self.mail_pass)
            s.connect(self.mail_host,25)
            # s.login(self.mail_user,self.mail_pass)
            print("邮件发送成功")
        except smtplib.SMTPException as msg:
            # print(msg)
            print("Error: 无法发送邮件:",msg)

c = ConfigEmail()
print(c.mail_host)
c.send_mail()
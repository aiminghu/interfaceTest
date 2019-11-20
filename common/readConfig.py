#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/9 0009 下午 23:37 
# @Author : aiminhu
# @File : readConfig.py 
# @Software: PyCharm

import os
import codecs
import configparser

#获取该文件的真实路径，然后分割路径和文件名存入一个元组
proDir = os.path.split(os.path.realpath(__file__))[0]
#获取上层目录
parDir = os.path.dirname(proDir)
configPath = os.path.join(parDir,"config.ini")
# print('---',configPath)
# print('prodir:',proDir,configPath)

class ReadConfig(object):
    def __init__(self):

        #1--实例化configparser对象
        self.cf = configparser.ConfigParser()

        self.cf.read(configPath,encoding="utf-8")

    def get_email(self,name):
        #3--获取某某section下的value，name相当于key
        value = self.cf.get('EMAIL',name)
        return value

    def get_http(self, name):
        value = self.cf.get('HTTP', name)
        return value

    def get_db(self, name):
        value = self.cf.get('DATABASE', name)
        return


# p = ReadConfig()
# print(p.get_email('mail_host'))
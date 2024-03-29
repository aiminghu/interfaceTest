#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/9 0009 下午 23:36 
# @Author : aiminhu
# @File : configHttp.py 
# @Software: PyCharm

import  requests
from common import readConfig as readConfig
localReadConfig = readConfig.ReadConfig()

class ConfigHttp(object):

    #get方法
    def get(self,url,param):
        try:
            # param = eval(param)
            # print(type(param))
            respone = requests.get(url,params=eval(param))
            result = respone.text
            return result
        except Exception:
            print('request error,please check out!')
            return None

    #post方法
    def post(self,url,param):
        try:
            respone = requests.post(url,data=eval(param))
            # print(type(eval(param)))
            result = respone.text
            # print(result)
            return result
        except Exception:
            print('request error,please check out!')
            return None

    def getRequest(self,url,param,method):
        if str(method) == 'get':
            return self.get(url,param)
        elif str(method) == "post":
            return self.post(url,param)



# #---------调试信息
# c = ConfigHttp()
# url = 'https://www.wanandroid.com/user/login'
#
# param = '{"username":"lijingying","password":"123456"}'
#
# c.getRequest(url,param,'post')
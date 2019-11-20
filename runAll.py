#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/10 0010 上午 11:16 
# @Author : aiminhu
# @File : runAll.py 
# @Software: PyCharm
'''
模块功能
    1.集成框架内所有的功能模块
    2.测试用例套件的封装-discover
    3.测试用例报告的生成-HTMLTestRunner
    4.垃圾文件的清理
'''
import unittest
import time
import os
import HTMLTestRunner

def run_case(dir = "testCase"):
    #按照指定目录加载测试用例
    case_dir = os.getcwd() + '\\' + dir
    print(case_dir)

    discover = unittest.defaultTestLoader.discover(case_dir,pattern='test_case*.py',top_level_dir=None)
    return discover

def create_resultHtml():
    pass



if __name__ == '__main__':
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    report_path = os.getcwd() + '\\report\\' + current_time + '.html'  #生成测试报告的路径
    print('---reprot_path',report_path)
    fp = open(report_path,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化测试报告',description=u'测试某个接口')
    runner.run(run_case())
    fp.close()
    print(current_time)
    print(run_case())

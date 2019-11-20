#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/9 0009 下午 23:37 
# @Author : aiminhu
# @File : readExcel.py 
# @Software: PyCharm
'''
功能：
    1.读取excel
    2.获取sheet页数据，封装为列表
    3.组装最终列表数据

'''
import xlrd
import os

class readExcel():
    #打开excel
    dir = 'testData'
    # excel_dir = os.path.dirname(os.getcwd()) + '\\' + dir #在当前目录下运行时，获取的是现在的目录
    excel_dir = os.getcwd() + '\\' + dir

    # 打开excel
    workbook = xlrd.open_workbook(excel_dir + '\\' + 'data.xlsx')
    # 根据sheet索引或者名称获取sheet内容
    # sheet1 = workbook.sheet_by_index(0)
    urlSheet = workbook.sheet_by_name('urlSheet')
    paramSheet = workbook.sheet_by_name('paramSheet')
    assertSheet = workbook.sheet_by_name('assertSheet')
    rownum = urlSheet.nrows



    def getInterfaceList(self):
        utlList = []
        # 获取interface列表
        # print(type(self.urlSheet))
        for i in range(1, self.rownum):
            self.rowvalue = self.urlSheet.row_values(i)
            # print(self.rowvalue)
            utlList.append(self.rowvalue)
        return utlList

    def getParamList(self):
        paramList = []
        # 获取param列表
        for i in range(1, self.rownum):
            self.rowvalue = self.paramSheet.row_values(i)
            # print(self.rowvalue)
            paramList.append(self.rowvalue)
        return paramList

    def getAssertList(self):
        assertList = []
        # 获取assert列表;
        for i in range(1, self.rownum):
            self.rowvalue = self.assertSheet.row_values(i)
            # print(self.rowvalue)
            assertList.append(self.rowvalue)
        return assertList

    # def assembleData(self):
    #     urlList = self.getInterfaceList()
    #     paramList = self.getParamList()
    #     assertList = self.getAssertList()
    #     dataList = []
    #     for a,b,c,d in urlList:
    #         singleList = []
    #
    #         id = int(a)
    #         url = b
    #         method = d
    #         param = paramList[id-1][1]
    #         expect = assertList[id-1][1]
    #         singleList.append(id)
    #         singleList.append(url)
    #         singleList.append(method)
    #         singleList.append(param)
    #         singleList.append(expect)
    #         print(singleList)
    #         dataList.append(singleList)
    #         print(dataList)

    # 组装所有的接口参数为一个list，一个元素包含id，url，method，param，expect
    def assembleData(self):
        urlList = self.getInterfaceList()
        paramList = self.getParamList()
        assertList = self.getAssertList()
        # 给每组数据建一个空列表
        dataList = []
        for i in range(len(urlList)):
            dataList.append([])

        for i in range(len(urlList)):
            # 将id，url，method，param，expect分别导出，并放入一个list
            id = urlList[i][0]
            dataList[i].append(id)
            url = urlList[i][1]
            dataList[i].append(url)
            method = urlList[i][3]
            dataList[i].append(method)
            param = paramList[i][1]
            dataList[i].append(param)
            expect = assertList[i][1]
            dataList[i].append(expect)
            # print(dataList[i])
            # print(dataList)
        return dataList


if __name__ == '__main__':
    print(os.getcwd())

p = readExcel()
# print(p.excel_dir)
# p.getInterfaceList()
# print(p.assembleData())
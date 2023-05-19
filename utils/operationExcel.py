"""
#--------------------------------------------
#:/usr/bin/env python
# -*-coding:utf-8 -*-

#ProjectName: apiFrameDev
#Author:jam
#Time: 2023/4/1 17:48
#description:'对Excel操作的封装'
#--------------------------------------------
"""

import xlrd
from utils.operationYaml import OperationYaml
from common.public import *

class ExcelVarles:
	caseID = "测试用例ID"
	caseModel = "模块"
	caseName = "接口名称"
	caseUrl = "请求地址"
	casePre = "前置条件"
	method = "请求方法"
	paramsType = "请求类型"
	params = "请求参数"
	expect = "期望结果"
	isRun = "是否运行"
	headers = "请求头"
	status_code = "状态码"
# 	caseID = 0
# 	des = 1
# 	url = 2
# 	method = 3
# 	data = 4
# 	expect = 5
#
# 	@property
# 	def getCaseID(self):
# 		return self.caseID
#
# 	@property
# 	def getDescription(self):
# 		return self.des
#
# 	@property
# 	def getUrl(self):
# 		return self.url
#
# 	@property
# 	def getMethod(self):
# 		return self.method
#
# 	@property
# 	def getData(self):
# 		return self.data
#
# 	@property
# 	def getExpect(self):
# 		return self.expect

class OperationExcel(OperationYaml):
	def getSheet(self):
		book = xlrd.open_workbook(filePath('data', 'books.xls'))
		return book.sheet_by_index(0)

# 	@property
# 	def getRows(self):
# 		'''获取总行数'''
# 		return self.getRows().nrows
#
# 	@property
# 	def getCols(self):
# 		'''获取总列数'''
# 		return self.getRows().ncols
#
# 	def getValue(self, row, col):
# 		return self.getSheet().cell_value(row, col)
#
# 	def getCaseID(self, row):
# 		return self.getValue(row = row, col = ExcelVarles().getCaseID)
#
# 	def getUrl(self, row):
# 		url = self.getValue(row = row, col = ExcelVarles().getUrl)
# 		if '{bookID}' in url:
# 			return str(url).replace('{bookID}', readContent())
# 		else:
# 			return url
#
# 	def getMethod(self, row):
# 		return self.getValue(row = row, col = ExcelVarles().getMethod)
#
# 	def getData(self, row):
# 		return self.getValue(row = row, col = ExcelVarles().getData)
#
# 	def getJson(self, row):
# 		'''data中books.xls文件中请求参数列映射config中book.yaml文件中请求参数列'''
# 		return self.dictYaml()[self.getData(row = row)]
#
# 	def getExpect(self, row):
# 		return self.getValue(row = row, col = ExcelVarles().getExpect)

	@property
	def getExcelDatas(self):
		datas = list()
		title = self.getSheet().row_values(0)
		#忽略首行
		for row in range(1, self.getSheet().nrows):
			row_values = self.getSheet().row_values(row)
			datas.append(dict(zip(title, row_values)))#zip把两个值搞成元组，强制转换成字典
		return datas

	def runs(self):
		'''获取到可执行的测试用例'''
		run_list = []
		for item in self.getExcelDatas:
			isRun = item[ExcelVarles.isRun]
			if isRun == 'y':
				run_list.append(item)
			else:
				pass
		return run_list

	def case_lists(self):
		'''获取Excel中所有的测试点'''
		cases = list()
		for item in self.getExcelDatas:
			cases.append(item)
		return cases

	def case_pre(self, case_Pre):
		'''
		依据前置测试条件找到关联的前置测试用例
		:param case_Pre:前置测试条件
		:return:
		'''
		for item in self.case_lists():
			if case_Pre in item.values():
				return item
		return None

	def preHeaders(self, preResult):
		#1、请求头在token里面；2、请求参数里面；3、地址里面
		'''
		替换被关联测试点的请求头变量值
		:param preResult:
		:return:
		'''
		for item in self.runs():
			headers = item[ExcelVarles.headers]
			if '{token}' in headers:
				headers = str((headers).replace('{token}', preResult))
				return json.loads(headers)

if __name__ == '__main__':
    obj = OperationExcel()
    for item in obj.case_lists():
	    print(item)
    # print(obj.getJson(row = 2))
    # print(type(obj.getJson(row = 2)))
    # for item in obj.getExcelDatas():
	#     print(item[ExcelVarles.caseUrl])
    # for item in obj.runs():
	#     print(item)


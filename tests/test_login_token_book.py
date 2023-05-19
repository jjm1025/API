"""
#--------------------------------------------
#:/usr/bin/env python
# -*-coding:utf-8 -*-

#ProjectName: apiFrameDev
#Author:jam
#Time: 2023/4/3 1:10
#description:''
#--------------------------------------------
"""
from base.method import Requests
from utils.operationExcel import OperationExcel, ExcelVarles
import pytest
import json
import allure

excel = OperationExcel()
obj = Requests()

@pytest.mark.parametrize('datas', excel.runs())
def test_login_book(datas):
	#对请求参数做反序列化处理
	params = datas[ExcelVarles.params]
	if len(str(params).strip()) == 0:pass
	elif len(str(params).strip()) >= 0:
		params = json.loads(params)

	#对请求头做反序列化处理
	header = datas[ExcelVarles.headers]
	if len(str(header).strip()) == 0:pass
	elif len(str(header).strip()) >= 0:
		header = json.loads(header)

	# 执行前置测试点
	r = obj.post(
		url = excel.case_pre(datas[ExcelVarles.casePre])[ExcelVarles.caseUrl],
		json = json.loads(excel.case_pre(datas[ExcelVarles.casePre])[ExcelVarles.params]))
	preResult = r.json()['access_token']

	#替换被关联测试点中请求头信息的变量
	header = excel.preHeaders(preResult)

	#状态码
	status_code = int(datas[ExcelVarles.status_code])

	def case_assert_result(r):
		assert r.status_code == status_code
		assert datas[ExcelVarles.expect] in json.dumps(r.json(), ensure_ascii = False)

	def getUrl():
		return str(datas[ExcelVarles.caseUrl]).replace('{bookID}', readContent())

	#对请求方法做反序列化处理
	if datas[ExcelVarles.method] == 'get':
		if '/books' in datas[ExcelVarles.caseUrl]:
			r = obj.get(url = getUrl(),
		            headers = header)
			case_assert_result(r = r)
		else:
			r = obj.get(url = getUrl(), headers = header)
			case_assert_result(r = r)

	elif datas[ExcelVarles.method] == 'post':
		r = obj.get(url = datas[ExcelVarles.caseUrl],
					json = params,
		            headers = header)
		writeContent(content = str(r.json()[0]['datas'][id]))
		case_assert_result(r = r)


	elif datas[ExcelVarles.method] == 'put':
		r = obj.put(url = getUrl(),
					json = params,
		            headers = header)
		case_assert_result(r = r)

	elif datas[ExcelVarles.method] == 'delete':
		r = obj.delete(url = getUrl(), headers = header)
		case_assert_result(r = r)

	'''
	1、先获取到所有前置测试点的测试用例
	2、执行前置测试点
	3、获取它的结果信息
	4、拿它的结果信息替换对应测试点的变量
	'''

if __name__ == '__main__':
	pytest.main(["-s", "-v", "test_login_token_book.py", "--alluredir", "./report/result"])
    # import subprocess
    # subprocess.call('allure generate report/result/ -o report/html --clean', shell = True)
    #subprocess.call('allure open -h 127.0.0.1 -p 8088 ./report/html', shell = True)

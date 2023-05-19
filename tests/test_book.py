"""
#--------------------------------------------
#:/usr/bin/env python
# -*-coding:utf-8 -*-

#ProjectName: apiFrameDev
#Author:jam
#Time: 2023/4/2 17:27
#description:''
#--------------------------------------------
"""
import pytest
import json
from base.method import Requests
from utils.operationExcel import OperationExcel
from common.public import *


class TestBook:
	excel = OperationExcel()
	obj = Requests()

	def result(self, r, row):
		'''封装断言'''
		assert r.status_code == 200
		assert self.excel.getExpect(row = row) in json.dumps(r.json(), ensure_ascii = False)


	def test_book_001(self):
		'''获取所有的书籍信息'''
		r = self.obj.get(url = self.excel.getUrl(row = 1))
		# print(r.json())
		# print(type(r.json()))
		self.result(r = r, row = 1)

	def test_book_002(self):
		'''新增书籍'''
		r = self.obj.post(url = self.excel.getUrl(row = 2),
		                  json = self.excel.getJson(row = 2))
		writeContent(content = r.json()[0]['datas']['id'])
		# print(r.json())
		# print(type(r.json()))
		self.result(r = r, row = 2)

	def test_book_003(self):
		'''查看书籍'''
		r = self.obj.get(url = self.excel.getUrl(row = 3))
		print(r.json())
		print(type(r.json()))


	def test_book_004(self):
		'''编辑书籍信息'''
		r = self.obj.put(url = self.excel.getUrl(row = 4),
		                  json = self.excel.getJson(row = 4))
		print(r.json())
		print(type(r.json()))
	# 	self.result(r = r, row = 2)

	def test_book_005(self):
		'''删除书籍信息'''
		r = self.obj.delete(
			url = self.excel.getUrl(row = 5))
		print(r.json())
		print(type(r.json()))
	# 	self.result(r = r, row = 5)
if __name__ == '__main__':
    pytest.mian(["-s", "-v", "test_book.py"])

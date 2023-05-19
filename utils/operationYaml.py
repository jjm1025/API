"""
#--------------------------------------------
#:/usr/bin/env python
# -*-coding:utf-8 -*-

#ProjectName: apiFrameDev
#FileName: operationYaml.py
#Author:jam
#Time: 2023/4/1 1:54
#description:'对Yaml文件进行操作'
#--------------------------------------------
"""
import yaml
from common.public import filePath

class OperationYaml:
	def readYaml(self):
		with open(filePath(), 'r', encoding = 'utf-8') as f:
			return list(yaml.safe_load_all(f))

	def dictYaml(self, fileDir = 'config', fileName = 'book.yaml'):
		with open(filePath(fileDir = fileDir, fileName = fileName), 'r', encoding = 'utf-8') as f:
			return yaml.load(f, Loader = yaml.FullLoader)


if __name__ == '__main__':
	obj = OperationYaml()
	print(obj.dictYaml()['book_002'])
	# 	print(obj.readYaml())
	# 	for item in obj.readYaml():
	# 		print(item)


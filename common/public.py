"""
#--------------------------------------------
#:/usr/bin/env python
# -*-coding:utf-8 -*-

#ProjectName: apiFrameDev
#FileName: public.py
#Author:jam
#Time: 2023/4/1 1:40
#description:'对目录的处理'
#--------------------------------------------
"""

import os

def filePath(fileDir = 'data', fileName = 'login.yaml'):
	'''
	:param fileDir: 目录
	:param fileName: 文件名称
	:return:
	'''
	return os.path.join(
		os.path.dirname(os.path.dirname(__file__)), fileDir, fileName)

def writeContent(content):
	with open(filePath(fileDir = 'data',fileName = 'bookID'), 'w') as f:
		f.write(str(content))

def readContent():
	with open(filePath(fileDir = 'data',fileName = 'bookID'), 'r') as f:
		return f.read()


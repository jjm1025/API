"""
#--------------------------------------------
#:/usr/bin/env python
# -*-coding:utf-8 -*-

#ProjectName: apiFrameDev
#Author:jam
#Time: 2023/4/1 13:34
#description:''
#--------------------------------------------
"""
import pytest
import json
from base.method import Requests
from utils.operationYaml import OperationYaml

obj = Requests()
objYaml = OperationYaml()

@pytest.mark.parametrize('datas', objYaml.readYaml())
def test_login_v1(datas):
	# print(datas['data'])
	# print(type((datas['data'])))
	r = obj.post(
		url = datas['url'],
		json = datas['data'])
	#print(json.dumps(r.json(), ensure_ascii = False))
	assert datas['expect'] in json.dumps(r.json(), ensure_ascii = False)

if __name__ == '__main__':
    pytest.main([ "-s", "-v", "test_login_v1.py"])
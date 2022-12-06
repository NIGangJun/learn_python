# -*- coding: utf-8 -*-
"""
@Author     : NIGangJun
@Date       : 2022/12/5 16:59
@File       : main.py
@Desc       : 学习 http 请求
"""
import json

import requests

url = 'http://114.215.19.181:8012/get_business_app/'
headers = {'content-type': "application/json"}
params = {
    "seq_no": '202100000001001615',
    "operCusRegCode": '1114941005',
    "def_agent_code_scc": '91110302600088026B'
}
response = requests.post(url, headers=headers, data=json.dumps(params))
print(response.text)
print(response.json())

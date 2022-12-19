# -*- coding: utf-8 -*-
"""
@Author     : NIGangJun
@Date       : 2022/12/5 16:59
@File       : main.py
@Desc       : 学习 http 请求
"""
from datetime import datetime

import requests

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
url = 'http://39.98.110.140:8086/api_erp/import_source_dec_status/'
data_list = [{
    "dec_seq_no": 'I20220000956218253',
    "def_agent_code_scc": '91110113773355401B'
}]
json = {
    'data': data_list,
    'token': '7a61bae06a52bec8e312a86cf57be0ef'
}
headers = {'content-type': "application/json"}
params = {
    "seq_no": '202100000001001615',
    "operCusRegCode": '1114941005',
    "def_agent_code_scc": '91110302600088026B'
}
response = requests.post(url=url, json=json)
print("response", response.json())
try:
    data = response.json()
except:
    raise ValueError(u'同步失败，请重试')

# 检查cookie是否过期
errcode = data.get("errcode")
if errcode == '1':
    raise ValueError(data.get('errmsg'))

return_dic = data.get('data')

# 检查返回数据是否有错
if return_dic.get('message'):
    raise ValueError(return_dic.get('message'))
for item in return_dic.get('rows'):
    seq_no = item.get('spDecSeqNo')
    channel = item.get('channel')
    noticeDate = item.get('noticeDate')
    noticeDate = datetime.strptime(noticeDate, DATE_FORMAT)
    message = item.get('note')

    if channel in ['0', '1']:
        receipt_type = 'A'
    else:
        receipt_type = 'B'

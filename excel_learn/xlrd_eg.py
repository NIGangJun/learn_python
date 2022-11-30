# -*- coding: utf-8 -*-
"""
@Author     : NIGangJun
@Date       : 2022/11/30 18:25
@File       : xlrd_eg.py
@Desc       : xlrd 示例
"""

import xlrd


def read_excel(n):
    """
    :param n: execl 路径
    :return: 表单
    """
    excel_file = xlrd.open_workbook(n)  # 打开xlsx文件
    return excel_file.sheets()  # 返回的是列表，列表里面是 xlrd.sheet.Sheet 对象


print(read_excel('test.xls'))

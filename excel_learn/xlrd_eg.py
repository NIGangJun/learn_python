# -*- coding: utf-8 -*-
"""
@Author     : NIGangJun
@Date       : 2022/11/30 18:25
@File       : xlrd_eg.py
@Desc       : xlrd 示例
"""

import datetime
import itertools
import operator

import xlrd

DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M:%S"
DATETIME_FORMAT = "%s %s" % (DATE_FORMAT, TIME_FORMAT)


def read_excel(n):
    """
    :param n: execl 路径
    :return: 表单 list
    """
    excel_file = xlrd.open_workbook(n)  # 打开xlsx文件
    # excel_file.sheet_names() 返回 excel 中工作单的名称
    # return excel_file.sheet_by_index()  # 按表单的索引返回需要读取的 excel 表单 这种一般是固定表单
    # return excel_file.sheet_by_name('学生信息')  # 按名称返回需要读取的 excel 表单
    # return excel_file.sheets()  # 返回的是列表，列表里面是 xlrd.sheet.Sheet 对象
    return excel_file  # 返回excel对象


def _read_xls_book(book):
    sheet = book.sheet_by_index(0)
    for row in map(sheet.row, range(sheet.nrows)):
        values = []
        for cell in row:
            if cell.ctype is xlrd.XL_CELL_NUMBER:
                is_float = cell.value % 1 != 0.0
                values.append(str(cell.value) if is_float else str(int(cell.value)))
            elif cell.ctype is xlrd.XL_CELL_DATE:
                is_datetime = cell.value % 1 != 0.0
                dt = datetime.datetime(*xlrd.xldate.xldate_as_tuple(cell.value, book.datemode))
                values.append(dt.strftime(DATETIME_FORMAT) if is_datetime else dt.strftime(DATE_FORMAT))
            elif cell.ctype is xlrd.XL_CELL_BOOLEAN:
                values.append(u'True' if cell.value else u'False')
            elif cell.ctype is xlrd.XL_CELL_ERROR:
                raise ValueError("读取excel单元格错误: %s".format(
                    xlrd.error_text_from_code.get(cell.value, "错误单元格内容 %s".format(cell.value))))
            else:
                values.append(cell.value)
        if any(x for x in values if x.strip()):
            yield values


def read_datas(rows):
    """
    读取表内数据，返回从第一行开始的的所有数据列表
    :return:
    """
    return itertools.islice(rows, 1, None)


def match_header():
    """
    处理 excel title 信息
    todo 暂时没想好针对 header 应该做什么优化
    :return:
    """
    return ['name', 'sex', 'score', 'age', 'phone', 'address']


if __name__ == '__main__':
    """
    该脚本还缺少一个表头映射表体的方法，将需要的 excel 信息直接通过 title 映射，然后达到通过配置需要的字段获取对应的内容
    """
    table = read_excel('./test.xls')
    table_book = _read_xls_book(table)
    fields = match_header()  # 获取表头
    rows_to_import = read_datas(table_book)  # 获取表体
    indices = [index for index, field in enumerate(fields) if field]
    if len(indices) == 1:
        # 如果只处理一个字段的话
        mapper = lambda row: [row[indices[0]]]
    else:
        mapper = operator.itemgetter(*indices)
    data = [list(row) for row in map(mapper, rows_to_import) if any(row)]
    title = [f for f in fields if f]
    # data title 最终的这个 data 和 title 就是处理好的 excel 数据了

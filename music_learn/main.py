# -*- coding: utf-8 -*-
"""
@Author     : NIGangJun
@Date       : 2022/11/29 16:21
@File       : main.py
@Desc       : 音频转换脚本
"""
import os

from pydub import AudioSegment

SOURCE_PATH = 'source'  # 源文件夹
TARGET_PATH = 'target'  # 目标文件夹


def read_file(p):
    """
    :param p: 文件夹绝对路径
    :return: list 文件的绝对路径
    """
    return map(lambda f: os.path.join(p, f), os.listdir(p))


def get_path():
    """
    :return: 文件夹绝对路径
    """
    return os.path.join(os.getcwd(), SOURCE_PATH)


def trans_file(fp, f):
    """
    :param fp: 文件的绝对路径
    :param f: format 需要处理的文件格式
    :return: None 导出文件
    """
    song_file = AudioSegment.from_file(fp)
    temp_name_file = os.path.basename(fp)
    file_name, file_extension = os.path.splitext(temp_name_file)
    t_path = os.path.join(os.getcwd(), TARGET_PATH)
    song_file.export("{}{}".format(os.path.join(t_path, file_name), ".{}".format(f)), format=str(f))


path = get_path()
for file in read_file(path):
    trans_file(file, 'wav')

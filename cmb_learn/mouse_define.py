# -*- coding: utf-8 -*-
"""
@Author     : NIGangJun
@Date       : 2022/11/28 14:34
@File       : mouse_define.py
@Desc       : 提供学习的鼠标模拟
"""
import win32api
import win32con
import win32gui


def move(x, y):
    """
    函数功能：移动鼠标到指定位置
    参  数：x:x坐标
         y:y坐标
    """
    win32api.SetCursorPos((x, y))


def get_cur_pos():
    """
    函数功能：获取当前鼠标坐标
    """
    p = {"x": 0, "y": 0}
    pos = win32gui.GetCursorPos()
    p['x'] = pos[0]
    p['y'] = pos[1]
    return p


def left_click():
    """
    函数功能：鼠标左键点击
    """
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def right_click():
    """
    函数功能：鼠标右键点击
    """
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN | win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)


def left_down():
    """
    函数功能：鼠标左键按下
    """
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)


def left_up():
    """
    函数功能：鼠标左键抬起
    """
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def right_down():
    """
    函数功能：鼠标右键按下
    """
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)


def right_up():
    """
    函数功能：鼠标右键抬起
    """
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

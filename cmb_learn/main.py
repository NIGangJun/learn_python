# -*- coding: utf-8 -*-
"""
@Author     : NIGangJun
@Date       : 2022/11/28 12:02
@File       : main.py
@Desc       : 打开浏览器，并模拟鼠标键盘进行操作

1. pip install PyUserInput 自动安装 pykeyboard | pymouse
2. 参考 https://juejin.cn/post/6844904200493613064
3. selenium 需要安装浏览器支持

"""

from pykeyboard import PyKeyboard
from pymouse import PyMouse
from selenium import webdriver


def running_ie():
    """
    使用 selenium 拉起浏览器
    :return: None
    """
    driver = webdriver.Ie()  # 打开ie浏览器(或兼容模式Edge) IE 需要安装 IEDriverServer.exe
    driver.maximize_window()  # 浏览器全屏
    driver.implicitly_wait(8)  # 隐性等待时间 判断是否完成页面加载 时间【秒】

    driver.get("https://app.cmbchina.com/cevs/Login.aspx?from=print")  # 拉起浏览器打开的 url 地址
    qr_ele = driver.find_element('id', 'goPassWordLogin')  # 定位需要操作的元素
    # from selenium.webdriver.common.by import By 也可以通过导入 By 定位
    # qr_ele = driver.find_element(By.CLASS_NAME, 'ClassName')
    qr_ele.click()  # 点击事件
    user_input()


def user_input():
    """
    模拟用户操作鼠标键盘
    :return: None
    """
    m = PyMouse()  # 实例化鼠标事件
    k = PyKeyboard()  # 实例化键盘事件
    m.click(960, 460)  # 在坐标处点击 todo 可以使用图像识别的方式进行定位
    k.type_string('4321')  # 执行键盘点击

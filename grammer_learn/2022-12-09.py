# -*- coding: utf-8 -*-
"""
@Author     : NIGangJun
@Date       : 2022/12/9 10:44
@File       : 2022-12-09.py
@Desc       : 尝试不修改源码的情况下 改掉源码中的类方法
"""


class Father(object):
    """父类"""

    def __init__(self):
        self.name = 'wilson'

    def method_first(self, val):
        """
        父类中的一个方法
        :return:
        """
        # 父类中方法执行
        print("我是一个父类中的方法，我叫{}，我有{}".format(self.name, val))


def method_first(self, val):
    """
    定义一个和父类方法一模一样的名称和传参，传参不一样也没关系，考虑原来类方法可能很多地方都在引用，按理是要保证原有的参数不变才好
    :return:
    """
    # 重新定义的方法
    print("我重新定义了")


F_cls = Father()
F_cls.method_first('123')
setattr(Father, 'method_first', method_first)  # 确认是可以完成这个需求
F_cls.method_first('321')

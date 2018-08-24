# -*- coding: utf-8 -*-
# @Time    : 18-8-24
# @Author  : ErichLee ErichLee@qq.com
# @File    : APair.py
# @Comment : 


from util.logger_util import *


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


def start():
    pair = Pair(3, 4)
    infos(pair)


start()

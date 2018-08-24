# -*- coding: utf-8 -*-
# @Time    : 2018/5/30
# @Author  : ErichLee ErichLee@qq.com
# @File    : MyFunctions.py
# @Comments: 函数功能
#

import sys
import html
from util.logger_util import *

"""
    参数传递
    *  -> tuple
    ** -> dict
    
    一个* 参数只能出现在函数定义中最后一个位置参数后面，
    而**参数只能出现在最后一个参数。
    有一点要注意的是，在* 参数后面仍然可以定义其他参数。

"""

"""
    类型1
    任意数量的位置参数，可以使用一个* 参数 
"""


def fun1(first, *rest):
    msg_rest = 'rest [type] : {} , [length] : {} \n'.format(type(rest), len(rest))
    msg = 'message > [first] : {} , [rest] : {} \n'.format(first, ' '.join(rest))
    infos(msg_rest, msg)


"""
    类型2
    任意数量的关键字参数，使用一个以** 开头的参数 
"""


def fun2(first, second, **rest):
    keyvals = [' %s="%s"' % item for item in rest.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(name=first, attrs=attr_str, value=html.escape(second))
    infos(element)


"""
    类型3-1
    函数的某些参数强制使用关键字参数传递
    在second和last中间加入*号 在调用改方法时 
    必须带参调用   fun3(first='1', second=2, last='1') 
    last=None 设置参数last 默认值为None,当传递其他值后 会覆盖默认值
"""


def fun3(first, second, *, last=None):
    pass


"""
    类型3-2
    你写好了一个函数,然后想为这个函数的参数增加一些额外的信息,这样的话其他
    使用者就能清楚的知道这个函数应该怎么使用
"""


def fun3_2(x: int, y: int) -> int:
    return x + y


"""
    类型4
    返回多个值的函数
    例如函数结尾返回 return 1,2,3
    实际上是创建一个元祖后直接返回 相当于 return (1,2,3)
"""


def compute(a, b):
    return a + b


def say_yes(result):
    infos('result > {}'.format(result))


def fun4(func, args, *, callback):
    result = func(*args)
    callback(result)


fun4(func=compute, args=(3, 5), callback=say_yes)

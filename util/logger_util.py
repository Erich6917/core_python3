# -*- coding: utf-8 -*-
# @Time    : 2018/12/21
# @Author  : ErichLee ErichLee@qq.com
# @File    : logger_util.py
# @Comment : 打印工具
#            
import logging


def print_new_line(msg=''):
    if msg:
        print(msg)
        logging.info(msg)
    else:
        print()


def print_no_line(msg=''):
    if msg:
        print(msg, end='')  # py3版本
        # print msg,  # py2版本
        logging.info(msg)


def __get_meg(args):
    msg = [str(each) for each in args if each]
    return ' '.join(msg)


def infos_line(*args):
    if args:
        msg = __get_meg(args)
        print_no_line(msg)


def infos(*args):
    if args:
        msg = __get_meg(args)
        print_new_line(msg)


def ljinfos(lmgs, *args):
    """
    :param lmgs: 左对齐打印头 需要格式化长度
    :param args: 变量参数依次打印
    """
    if lmgs:
        print_no_line('[{}]:'.format(lmgs.ljust(30)))
    else:
        print_no_line('[{}]'.format("".ljust(30)))

    if args:
        for each in args:
            print_no_line(each)

    print_new_line()


def cinfos(lmgs, *args):
    """
    :param lmgs: 居中打印头 需要格式化长度
    :param args: 变量参数依次打印
    """
    if lmgs:
        print_no_line('[{}]:'.format(lmgs.center(30)))
    else:
        print_no_line('[{}]'.format("".center(30)))

    if args:
        for each in args:
            print_no_line(each)

    print_new_line()


def errors(*args):
    if args:
        msg = __get_meg(args)
        print_new_line('[ERROR]: {}'.format(msg))


def println():
    print_new_line('================================')

# infos()
# errors()
# infos('1', None)
# infos_line('1', 2, 3, '4')
# infos('next line')
# ljinfos('title', '1', 2, 3, None, '4', None)
# cinfos('title', '1', 2, 3, '4')
# errors('error', 'msssag', 'exception')

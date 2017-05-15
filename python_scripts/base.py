#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Author      :
Description : 基础操作
Time        : 2017.05.15
Illustration:
- os.path操作
- 查询指定IP所属地理位置
- 输出带有日期和颜色的信息
- 基本数据结构相互转换
'''
import os
import time
from ipip import IP


def os_path():
    # os.path操作
    FILE_PATH = os.path.abspath(__file__)
    CUR_DIR = os.path.dirname(os.path.abspath(__file__))
    print FILE_PATH                         # 当前脚本的完整路径(包含存放路径和文件名)
    print CUR_DIR                           # 输出该脚本所在的完整路径
    print os.path.sep                       # /


def ip_search():
    # 查询指定IP所属地理位置
    IP.load('路径/tinyipdata_utf8.dat')
    print IP.find('ip地址').strip().encode("utf8")


def ColorPrint(message, color=32):
    # 输出带有日期和颜色的信息，32表示绿色，31表示红色
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    message = time_str + '\t' + message
    print_message = "\033[1;{color};40m {message} \033[0m!".format(
        color=color, message=message)
    print print_message


def data_struct():
    # 基本数据结构相互转换
    # python的几种基本的数据结构：元组、列表、字典、集合
    # 字典
    dict = {'a': 1, 'b': 2, 'c': 3}
    print dict.keys()           # 输出字典的key
    print dict.keys()[0], dict[dict.keys()[0]]  # 输出字典的key和value
    print str(dict)             # 字典转为字符串，返回{'a': 1, 'c': 3, 'b': 2}
    print tuple(dict)           # 字典的key转为元组，返回('a', 'c', 'b')
    print tuple(dict.values())  # 字典的value转为元组，返回(1, 3, 2)
    print list(dict)            # 字典的key转为列表，返回['a', 'c', 'b']
    print list(dict.values())   # 字典的value转为列表，返回[1, 3, 2]
    # 元组 - 元组无法转为字典
    tup = (1, 2, 3, 4, 5)
    print str(tup)              # 元组转换为字符串，返回(1, 2, 3, 4, 5)
    print tup.__str__()         # 元组转换为字符串，返回(1, 2, 3, 4, 5)
    print list(tup)             # 元组转化为列表，返回[1, 2, 3, 4, 5]
    # 列表 - 列表无法转为字典
    lis = [1, 2, 3, 4, 5]
    print str(lis)              # 列表转换为字符串，返回[1, 2, 3, 4, 5]
    print tuple(lis)            # 列表转换为元组，返回(1, 2, 3, 4, 5)
    # 字符串转换
    str1 = '(1, 2, 3)'
    str2 = "{'a': 1, 'b': 2, 'c': 3}"
    print tuple(eval(str1))     # 字符串转化为元组，返回(1, 2, 3)
    print list(eval(str1))      # 字符串转化为列表，返回[1, 2, 3]
    print eval(str2)            # 字符串转化为字典，返回{'a': 1, 'c': 3, 'b': 2}
    # 集合 - 主要用于去重
    lis = [1, 1, 2, 2, 5]
    print set(lis)              # 将列表去重，返回{1, 2, 5}


def struct_deal():
    # 基本数据结构处理
    # 列表操作
    # 列表可包含任何数据类型的元素，单个列表中的元素无须全为同一类型。
    lis = [1, 2, 3, 4, 5]       # 创建列表
    print lis.append(7)         # append()向列表的尾部添加一个元素作为参数
    print lis.extend([9, 11])   # extend()向列表的尾部添加一个列表作为参数

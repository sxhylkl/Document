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
import sys
import time
from ipip import IP


def dis_task():
    # 执行脚本path.filename.py
    job_func = getattr(
        __import__('path.filename',
                   globals(),
                   locals(), [filename]),
        filename)
    job_func(self.date.strftime('%Y%m%d'))


def os_path():
    # os.path操作
    FILE_PATH = os.path.abspath(__file__)
    CUR_DIR = os.path.dirname(os.path.abspath(__file__))
    print FILE_PATH                         # 当前脚本的完整路径(包含存放路径和文件名)
    print CUR_DIR                           # 输出该脚本所在的完整路径
    print os.path.sep                       # /


def get_argv():
    # 获取传参
    # python ../base.py a -> path a
    print sys.argv[0], sys.argv[1]      # argv[0]为文件本身的路径，argv[1]表示传入的第一个参数


def get_sum(x, y):
    # 计算x+y的值
    return x + y


def get_reduce(lis):
    # reduce(函数,列表)，reduce()对list的每个元素反复调用函数，并返回最终结果值
    # reduce(get_sum, [1, 3, 5, 7, 9]) -> 25 ，原因1+3=4，4+5=9，9+7=16，16+7=25
    return reduce(get_sum, lis)


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
    # 列表操作 - 列表可包含任何数据类型的元素，单个列表中的元素无须全为同一类型。
    lis = [1, 2, 3, 4, 5]               # 创建列表
    print lis[0]                        # 列表起始位置的索引为0
    cmp(list1, list2)                   # 比较两个列表的元素，相同返回0，不相同返回-1
    max(lis)                            # 返回列表元素最大值
    min(lis)                            # 返回列表元素最小值
    len(lis)                            # 返回列表元素个数
    value in lis                        # 判断列表中是否存在某元素，是返回True，否返回False
    [value] * 5                         # 5个相同的元素内容
    [1, 2, 3] + [1, 2, 5]               # 列表组合，返回[1, 2, 3, 1, 2, 5]
    lis.append(value)                   # append()向列表的尾部添加一个元素作为参数
    lis.extend([value, value])          # extend()向列表的尾部添加一个列表作为参数
    lis.remove(value)                   # 移除列表中某个值的第一个匹配项
    lis.sort()                          # 对列表进行排序
    lis.sort(reverse=True)              # 对列表进行降序排序
    lis.pop()                           # 移除列表中的一个元素(默认最后一个元素)，并且返回该元素的值
    lis.pop(value)                      # 移除列表的第一个元素，并返回该元素的值
    lis.reverse()                       # 反向列表中元素
    li2.index(value)                    # 从列表中找出某个值第一个匹配项的索引位置
    li2.count(value)                    # 统计某个元素在列表中总共出现的次数
    lis.insert(index, value)            # 将元素插入列表的指定位置


def common():
    # 枚举类型
    list(enumerate('abc'))              # 返回[(0, 'a'), (1, 'b'), (2, 'c')]
    dict(enumerate('abc', 4))           # 4表示索引的起始值，返回{4: 'a', 5: 'b', 6: 'c'}
    # 三元运算
    x, y = 20, 10
    small = x if x < y else y           # 获取最小值
    isinstance(1, int)                  # 判断数据类型是否符合，是返回True，否返回False
    # 字典集合解析
    my_dict = {i: i * i for i in xrange(100)}
    my_set = {i * 15 for i in xrange(100)}


if __name__ == '__main__':
    get_argv()

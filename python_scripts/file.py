#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Author      : 
Description : 文件处理
Time        : 2017.04.25
Illustration:
'''


def open_file(path, filename_in, filename_out):
    ''' 
    读写文件 - open方式
    可以用try / finally语句来确保最后能关闭文件
    '''
    file_in = os.path.join(path, filename_in)
    file_out = os.path.join(path, filename_out)
    f_in = open(file_in, 'r')           # 读文件
    f_out = open(file_out, 'w')         # 写文件
    try:
        all_the_text = file_object.read()
        list_of_all_the_lines = file_object.readlines()     # 遍历文件对象获取每行
        for line in f_in:    # 遍历文件对象获取每行：
            f_out.write('\t'.join(map(str, [line])) + '\n')     # 写入文件到f_out
    finally:
        f_in.close()
        f_out.close()


def with_open_file(path, filename):
    ''' 读写文件 - with open方式 '''
    file_in = os.path.join(path, filename_in)
    with open(file_in, 'r') as f:
        lines = f.readlines()
        for i in range(2):  # 打印文件前2行内容
            print lines[i]

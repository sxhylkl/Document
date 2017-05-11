#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Author      : 
Description : 输出带有日期和颜色的信息
Time        : 2017.04.25
Illustration: 
'''
import time


def ColorPrint(message, color=32):
    # 输出带有日期和颜色的信息，32表示绿色，31表示红色
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    message = time_str + '\t' + message
    print_message = "\033[1;{color};40m {message} \033[0m!".format(
        color=color, message=message)
    print print_message

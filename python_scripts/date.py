#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Author      : 
Description : 日期处理
Time        : 2017.05.04
Illustration: 
'''
import time
import datetime
import calendar


def DateFormat(date, date_format_after='%Y-%m-%d', date_format_before='%Y%m%d'):
    # 格式化日期：默认将日期20160101转化为：2016-01-01 格式
    return datetime.datetime.strftime(
        datetime.datetime.strptime(date, date_format_before), date_format_after)


def format_dates(dates):
    # 格式化dates - 用于sql的in查询
    # format_dates(['20160101']) -> ('20160101')
    # format_dates(['20160101', '20160102']) -> ('20160101', '20160102')
    return '({0})'.format(','.join(repr(str(s)) for s in dates))


def ds_delta(start, end, date_format='%Y%m%d'):
    # 日期相减 - delta: 间隔天数;
    # ds_delta('20160301', '20160302') -> 1
    now = datetime.datetime.strptime(start, date_format)
    end = datetime.datetime.strptime(end, date_format)
    if now <= end:
        delta = (end - now).days
        return delta


def ds_add(date, delta, date_format='%Y%m%d'):
    # 日期计算 - delta: 间隔天数，可为负数
    return datetime.datetime.strftime(
        datetime.datetime.strptime(date, date_format) + datetime.timedelta(delta), date_format)


def date_range(start, end, date_format='%Y%m%d'):
    # 以列表形式返回两个日期之间的每个日期
    now = datetime.datetime.strptime(start, date_format)
    end = datetime.datetime.strptime(end, date_format)
    while now <= end:
        yield now.strftime(date_format)
        now += datetime.timedelta(days=1)


def check_week_month(date, mw, num=3):
    # 用于判断是否是星期几(默认周三) 和 是否是月末
    # mw用户判断是根据月还是周判断'm','w'
    if mw.upper() == 'M':
        if date[6:8] == str(calendar.monthrange(int(date[:4]), int(date[4:6]))[1]):
            return True
    if mw.upper() == 'W':
        if num - 1 == datetime.datetime.strptime(date, '%Y%m%d').weekday():
            return True


def get_day(year, month):
    # 根据指定的年和月，返回对应月份的天数
    return calendar.monthrange(year, month)[1]


def get_date(date, date_format_before='%Y%m%d'):
    # 返回指定日期的年月日
    year = datetime.datetime.strptime(date, date_format_before).year
    month = datetime.datetime.strptime(date, date_format_before).month
    day = datetime.datetime.strptime(date, date_format_before).day
    return year, month, day


def get_tamp(stmp, date_format_after='%Y-%m-%d'):
    # 将时间戳转化为指定格式的日期 - 可自选一种方法return
    # get_tamp(1486228605.59) -> '2017-02-05 01:16:45'
    # 方法一
    return time.strftime(date_format_after, time.localtime(stmp))
    # 方法二
    return datetime.datetime.fromtimestamp(stmp).strftime(date_format_after)

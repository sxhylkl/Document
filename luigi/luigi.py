#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Luigi Parameter
'''
import luigi
import datetime


class DateTask(luigi.Task):
    date = luigi.DateParameter()


a = datetime.date(2014, 1, 21)
b = datetime.date(2014, 1, 21)
print a is b

c = DateTask(date=a)
d = DateTask(date=b)


print c is d
True

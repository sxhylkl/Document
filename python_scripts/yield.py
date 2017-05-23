#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Author      :
Description : 基础操作
Time        : 2017.05.17
Illustration: Python yield
'''
# Iterator(迭代器) - 可以被next()函数调用并不断返回下一个值的对象称为迭代器
# Iterator可以是一个无限大的数据流，但是list永远不可能存储无限大的数据流。
# 迭代 - 利用for循环来遍历一个列表（list）或元组（tuple），将值依次取出，这种方法我们称为迭代。
# 斐波那契數列 - 一个非常简单的递归数列，除第一个和第二个数外，任意一个数都可由前两个数相加得到
# 输出斐波那契數列前N个数


def fab(num):
    # 方法一 - 直接print输出
    # 缺点：函数返回None，可复用性差
    n, a, b = 0, 0, 1
    while n < num:
        print b
        a, b = b, a + b
        n = n + 1


def fab(num):
    # 方法二 - 为提高可复用性, 返回一个 List,
    # 缺点：内存的占用会随着num的增大而增大
    n, a, b = 0, 0, 1
    L = []
    while n < num:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L


class Fab(object):
    # 方法三 - 把fab函数改写为一个支持iterable的class, Fab类通过next()不断返回数列的下一个数，内存占用始终为常数
    # 缺点：代码不够简洁
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()


def fab(num):
    # 方法四 - 在保持简洁性的同时获得了iterable的效果
    # 调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象
    # 函数执行结束时，generator 自动抛出 StopIteration 异常，表示迭代完成。在 for 循环里，无需处理 StopIteration 异常，循环会正常结束.
    # f = fab(5)    f.next()
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1



# range：会导致生成一个1000个元素的 List
for i in range(1000):
    pass
# xrange：不会生成一个1000个元素的List，而是在每次迭代中返回下一个数值，内存空间占用很小。因为 xrange 不返回
# List，而是返回一个 iterable 对象。
for i in xrange(1000):
    pass

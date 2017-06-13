#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Author      : Dong Junshuang
Description : 多进程并发操作中进程池Pool的应用
Create_date : 2017.06.09
Illustration: 通过Pool指定并发进程的最大值，当有新的请求提交到pool中时，如果池还没有满，就会
创建一个新的进程用来执行该请求；如果池中的进程数已经达到规定最大值，那么该请求就会等待，直到池中
有进程结束，才会创建新的进程给它
'''
from multiprocessing import Pool
from time import sleep


def get_i(i):
    print i
    sleep(1)


if __name__ == '__main__':
    '''
    pool.apply_async()用来向进程池提交目标请求
    pool.join()是用来等待进程池中的worker进程执行完毕，防止主进程在worker进程结束前结束
    pool.join()必须使用在pool.close()或者pool.terminate()之后
    其中close()跟terminate()的区别在于close()会等待池中的worker进程执行结束再关闭pool,而terminate()则是直接关闭
    result.successful()表示整个调用执行的状态，如果还有worker没有执行完，则会抛出AssertionError异常
    '''
    # 设置进程数最多为3个
    pool = Pool(processes=3)
    for i in range(11, 20):
        result = pool.apply_async(get_i, (i,))
    pool.close()
    pool.join()
    if result.successful():
        print 'successful'

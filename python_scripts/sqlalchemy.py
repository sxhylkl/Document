#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Author      : 
Description : 连接impala/hive/mysql，并处理数据
Time        : 2017.04.25
Illustration: sqlalchemy：高效的、高性能的数据库访问
支持数据库: PostgreSQL、MYSQL、Oracle、SQLlite、SQL Server、Other
'''

from sqlalchemy.engine import create_engine
import pandas as pd


def hql_to_df(hql, server='impala', db=None):
    '''
    将hql检索出结果放入dataframe中返回，默认使用impala，速度更快。
    >>> hql_to_df('show tables like "表名"').name[0]
    '表名'
    '''
    db = db or settings_dev.platform
    if server == 'impala':
        url = impala_template.format(db=db)
    elif server == 'hive':
        url = hive_template.format(db=db)
    else:
        raise Exception('argument server have to be hive or impala!')

    engine = sqlalchemy.create_engine(url)
    conn = engine.raw_connection()
    try:
        if server == 'impala':
            cur = conn.cursor()
            cur.execute('INVALIDATE METADATA')
        df = pd.read_sql(hql, conn)
    finally:
        conn.close()
    return df


def hqls_to_dfs(hqls, server='impala', db=None):
    '''并行处理多个hql请求
    >>> sqls = ['show tables like "{0}"'.format(i) for i in ['表名', '表名']]
    >>> [df.name[0] for df in hqls_to_dfs(sqls)]
    ['表名', '表名']
    '''
    assert isinstance(hqls, list)
    pool = Pool(5)
    results = pool.map(lambda x: hql_to_df(x, server, db), hqls)
    pool.close()
    pool.join()
    return results


def test_sqlalchemy(url, sql):
    engine = create_engine(url)
    connection = engine.raw_connection()
    # 原始方法
    # cur = connection.cursor()
    # cur.execute(sql)
    # print cur.fetchone()
    # print cur.fetchall()
    # 读取为pandas dataframe
    df = pd.read_sql(sql, connection)
    print df
    connection.close()


if __name__ == '__main__':
    # mysql
    mysql_url = 'mysql+pymysql://用户名:密码@IP地址/数据库?charset=utf8'
    mysql_sql = "SELECT * FROM 表名 LIMIT 100"
    test_sqlalchemy(mysql_url, mysql_sql)

    # hive
    hql = "SELECT * FROM 表名 LIMIT 100"
    # impala connector 由 [impyla](https://github.com/cloudera/impyla) 提供
    hive_url = 'hive://IP地址:端口号/数据库'
    test_sqlalchemy(hive_url, hql)

    # impala
    impala_url = 'impala://IP地址:端口号/数据库'
    result = test_sqlalchemy(impala_url, hql)

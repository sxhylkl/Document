#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Author      : 
Description : hive文件处理
Time        : 2017.05.15
Illustration: 上传文件时需保证hive和网络稳定，否则可能需要进行多次数据上传
'''
import os
import sqlalchemy
from hdfs import InsecureClient

if __name__ == '__main__':
    db = '数据库'
    date = '日期'
    table = '表名'
    filename = 'hdfs中存储的文件名'
    hdfs_url = 'http://dhfs的IP:dhfs的端口号'
    hive_template = 'hive://hive的IP:hive的端口号/{db}'.format(db=db)
    hive_path = '/user/hive/warehouse/{db}.db/{table}/ds={date}/{filename}'.format(
        db=db, table=table, filename=filename,
        date=date)
    local_path = '/home/data/superhero/redis_stats/info_{date}'.format(
        date=date)
    hdfs_path = '/tmp/{db}/{filename}'.format(**{
        'filename': filename,
        'db': db
    })
    try:
        hdfs_client = InsecureClient(hdfs_url)
        engine = sqlalchemy.create_engine(hive_template)
        conn_hive = engine.raw_connection()
        cur = conn_hive.cursor()
        # 检测文件是否存在
        if hdfs_client.status(hive_path, strict=False):
            # 输出文件大小
            print hdfs_client.status(hive_path, strict=False).get('length',
                                                                  '0')
            print 'Data In Hive!'
        else:
            print 'Warning: Data Not In Hive!'.format(table)
        # 删除hive文件
        try:
            hdfs_client.delete(hive_path)
            print '{hive_path} Delete Complete'.format(hive_path=hive_path)
        except Exception, e:
            print e
            print '{hive_path} Delete Faild'.format(hive_path=hive_path)
        # 上传本地文件到Hive
        if os.path.exists(local_path):
            remote_path = hdfs_client.upload(
                hdfs_path, local_path, overwrite=True)
            if remote_path:
                hql = '''
                load data inpath '{remote_path}'
                into table {db}.{table}
                partition (ds='{date}')
                '''.format(**{
                    'date': date,
                    'remote_path': remote_path,
                    'table': table,
                    'db': db,
                })
                cur.execute(hql)
                print 'Success: {local_path} -> {db}.{table} partition: {date}\n'.format(
                    **{
                        'table': table,
                        'db': db,
                        'local_path': local_path,
                        'date': date
                    })
            else:
                print 'Warning: Load Data To Hive Faild!'
        else:
            print 'Warning: {local_path} Not In Local!'.format(
                local_path=local_path)

    finally:
        cur.close()
        conn_hive.close()

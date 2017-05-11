# hdfscli
> * [官方文档](http://hdfscli.readthedocs.io/en/latest/index.html)

# hive技术
> * [impalaSQL](https://my.oschina.net/weiqingbin/blog/189413)
> * [ORACLE/HIVE/impala的SQL比较](http://blog.csdn.net/mayp1/article/details/51415854)

- 上传数据到hdfs
```sh
# ---------------------------------------------
# SQL语句
INSERT overwrite TABLE 表名 partition (ds='分区名')
SELECT 字段名
FROM 表名
WHERE 限制条件
# ---------------------------------------------
# 命令
$ hdfscli upload 文件名 /tmp                 # 上传文件
$ snakebite -n IP地址 ls '/tmp/'       # 查看文件
hive> load data inpath '/tmp/文件名' into table 数据库.表 partition(分区1='值1',分区2='值2');
```

- 表结构修改
```sh
create database 数据库名 IF NOT EXISTS 数据库名;    # 创建数据库
# 建表
CREATE TABLE IF NOT EXISTS 数据库.表(
    字段名 数据类型 comment '备注'
    , 字段名 数据类型 comment '备注'
) PARTITIONED BY(分区名 数据类型)
ROW format delimited FIELDS TERMINATED BY '\t' stored AS textfile
# ---------------------------------------------
# 修改列名、类型、备注
alter table 表名 change column 老字段名 新字段名 新字段类型 comment '备注';
ALTER TABLE 表名  ADD COLUMNS (列名 数据类型 comment '备注');  # 增加列
ALTER TABLE 老表名 rename to 新表名;      # 表重命名
drop table raw_gem;                     # 删除表
create table 表名 like 复制前表名;        # 复制表结构和分区
# ---------------------------------------------
# 常用操作
ALTER TABLE name RENAME TO new_name
ALTER TABLE name ADD COLUMNS (col_spec[, col_spec ...])
ALTER TABLE name DROP [COLUMN] column_name
ALTER TABLE name CHANGE column_name new_name new_type
ALTER TABLE name REPLACE COLUMNS (col_spec[, col_spec ...])
# ---------------------------------------------
# 查询数据库、数据库中的表名
show databases;
show databases like '数据库*';
show tables;
show tables in 数据库名;
show columns in 表名;    # 查询列
show partitions 数据库.表;  # 查看表中存在的所有分区
desc 表名;               # 查询表结构
use 数据库;               # 使用数据库
truncate table 表名;      # 删除表中的数据
describe database test;     # 查询数据库所在文件位置目录
```

- 数据查询
```sh
invalidate metadata;    # 刷新impala
hive -e "select * from 数据库名.表名 限制条件"   # hive一次执行命令
# 静默模式，可以在输出结果中去掉OK、Time taken等行，以及一些其他无关紧要的输出信息,并将查询到的信息存入文件
hive -S -e "select * from 数据库名.表名 限制条件" > 文件路径/文件名
# ---------------------------------------------
# 表生成函数：接受0个或多个输入，产生多列或多行输出
select 字段,字段 from 表名 lateral view  explode(array(1,2,3)) subview as sub where 限制条件 ;
# array函数的使用
select explode(array(1,2,3)) from 表名 where 限制条件;
# 生成日期格式
to_date(日期)
# 计算字段长度
LENGTH(字段名)
```


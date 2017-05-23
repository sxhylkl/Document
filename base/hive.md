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
```py
invalidate metadata;    # 刷新impala
hive -e "select * from 数据库名.表名 限制条件"   # hive一次执行命令
# 静默模式，可以在输出结果中去掉OK、Time taken等行，以及一些其他无关紧要的输出信息,并将查询到的信息存入文件
hive -S -e "select * from 数据库名.表名 限制条件" > 文件路径/文件名
# ---------------------------------------------
# 表生成函数：接受0个或多个输入，产生多列或多行输出
SELECT 字段,字段 from 表名 lateral view  explode(array(1,2,3)) subview as sub where 限制条件 ;
SELECT explode(array(1,2,3)) from 表名 where 限制条件;        # array函数的使用
to_date(日期)          # 生成日期格式
LENGTH(字段名)         # 计算字段长度
row_number() over(partition BY 字段名1 ORDER BY 字段名2 DESC) AS rn     # 排序
regexp_replace(substr(字段名,1,10),'-','')                             # 字符串操作
substr(字段名, start_index, num)          # 字符串截取，开始截取的位置(1开始)，截取的位数
select decode(条件值,值1,翻译值1,...值n,翻译值n,默认值)       # if条件值==值1，返回翻译值1，相当于case when
case when 条件 then 条件为真时的值 else 条件为假时的值 end     
```



# Impala
cloudera 公司出品的另一个 SQL 引擎，功能是 Hive 的一个子集，与 Hive 的区别如下：

- 使用C++语言实现，基于内存计算而非hive那种转化为mr任务的模式，因此速度比hive快很多，方便用来做一些交互式的SQL查询
- 自身不负责元数据管理，依赖 Hive 存在
- 功能是Hive的子集，如hive可以通过 json serde 直接将json格式的文件转化为表，但impala不行。在我们的数据中，行为日志是以json格式存在的，因此，对于行为日志的分析只能通过 hive，其它大部分可以用 impala 替代
- 由于是基于内存的计算，当需要的内存超过已有的内存时会报错。而hive无此问题，因为中间数据会使用磁盘暂存。

在hue中选择impala editor即可使用，操作与hive一致。 由于impala自己不维护表结构信息，而是使用hive的信息，且该过程并非实时的。因此， 当hive中表结构发生改变时，需要先执行以下命令，使原来的元数据无效，然后重新获取。
```
invalidate metadata;
```
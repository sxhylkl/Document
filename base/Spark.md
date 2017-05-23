# Spark
快如闪电的集群计算，是快速和通用的大规模集群技术。

> * [apache官网](http://www.apache.org)
> * [spark官网](http://spark.apache.org)


## 速度(speed)
- 在内存中执行mr作业比Hadoop快100倍
- 在磁盘上比Hadoop快10倍
- spark有DAG(有向无环图)执行引擎，支持高数据流和内存计算。

## 易于使用
- 支持多种语言：Java、Scala、python、R
- 提供了80多种高级操作用于并行APP，可以使用脚本语言进行交互式编程。

## 常规性
- 合成SQL语句
- 流计算
- 复杂分析
- MLIB(机器学习类库)
- GraphX(图形计算)
- spark数据流

## 运行环境
- 可运行环境：Hadoop、Mesos、standalone、cloud
- 可访问的数据源：HDFS、Cassandra、Hbase、S3(亚马逊的分布式文件系统)

## 其他
- spark有自己的集群管理机制
- spark使用Hadoop有2种方式：1.存储，2.处理
- 由于spark有自己的集群管理，所以使用Hadoop只是为了存储。
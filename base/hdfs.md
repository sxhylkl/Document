# DHFS基础

> DHFS（Hadoop Distributed File System）Hadoop分布式文件系统

## HDFS特点

- 运行在廉价的机器上
- 保存多个副本，且提供容错机制，副本丢失或宕机自动恢复，默认存3份。
- 适合大数据的处理，HDFS默认会将文件分割成Block，将Block按键值对存储在HDFS上，并将键值对的映射存入内存，如果小文件太多，内存的负担就会很重。

## Block

- 磁盘的Block
    - 是磁盘读/写数据的最小单位
    - 磁盘块一般为512字节(byte)
    - 文件系统的块通常是磁盘块的整数倍。文件系统的块一般为几千字节(byte)
- HDFS的Block
    - HDFS中的Block是一个很大的单元
    - 默认是64MB
    - 当HDFS上的文件小于块大小时，则占用实际的文件大小，而非一个块的大小

## 说明
- 热备份：b是a的热备份，如果a坏掉。那么b马上运行代替a的工作。
- 冷备份：b是a的冷备份，如果a坏掉。那么b不能马上代替a工作。但是b上存储a的一些信息，减少a坏掉之后的损失。
- fsimage：元数据镜像文件（文件系统的目录树。）
- edits：元数据的操作日志（针对文件系统做的修改操作记录）
- NameNode
    - Master节点
    - 管理数据块映射
    - 处理客户端的读写请求
    - 配置副本策略
    - 管理HDFS的名称空间
    - 内存中存储的是=fsimage+edits。
- SecondaryNameNode
    - 分担namenode的工作量
    - 是NameNode的冷备份
    - 定时默认1小时，从namenode上获取fsimage和edits来进行合并再发给namenode。
- DataNode
    - Slave节点
    - 负责存储client发来的数据块block
    - 执行数据块的读写操作。


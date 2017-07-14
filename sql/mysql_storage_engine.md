# MySQL存储引擎
> [MySQL存储引擎](http://www.cnblogs.com/gbyukg/archive/2011/11/09/2242271.html)



**1. MySQL引擎类型**
- MyISAM
- InnoDB
- Memory
- CSV
- Archive

**2. 查询默认数据存储引擎**
```sql
show variables like 'default_storage_engine';   # 查看当前数据库到默认引擎。
show engines;                                   # 当前数据库所支持的引擎
show variables like 'have%';                    # 当前数据库所支持的引擎，其中Value显示为disabled的表示数据库支持此引擎
```

**3. 查看文件的存储路径**
> 以下均根据Centos7系统统计
```sh
# vim /etc/my.cnf
datadir=/var/lib/mysql      # 数据文件的存储位置
```

## 一、MyISAM引擎
引擎文件
- .myd : 表数据文件
- .myi : 索引文件
- .log : 日志文件


## 二、InnoDB
> InnoDB采用表空间（tablespace）来管理数据，存储表数据和索引

引擎文件
- ibdata1、ibdata2等 : 系统表空间，存储InnoDB系统信息、用户数据库表和索引，所有表共用
- .ibd : (表名.ibd)单个表空间文件，每个表使用一个表空间文件，存放用户数据表数据和索引，默认存储位置在MySQL数据存储目录中数据库目录下
- ib_logfile1、ib_logfile2 : 日志文件

**存储文件查询**
```sh
# cd /var/lib/mysql
# ls
auto.cnf  ibdata1  ib_logfile0  ib_logfile1  mysql  mysql.sock  performance_schema  test
# cd test
# ls
aa.frm  aa.ibd  bb.frm  bb.ibd  db.opt
```

Innodb存储引擎管理主要基于两个文件：表空间数据文件和日志文件。


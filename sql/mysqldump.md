# MySQL的备份恢复
[mysqldump参考文档](http://www.cnblogs.com/wxb-km/p/3610594.html)

## 一、MySQL的常用备份方式
MYSQL官方将MySQL的备份方式主要划分为以下三类：
- 热备份：备份过程中MYSQL实例始终是运行的，所有用户的读写请求都不会受到影响
- 冷备份：备份前需要先停止MySQL的实例运行，整个备份过程中用户均无法访问数据库
- 温备份：备份过程中MYSQL实例是运行的，但是为了保证数据的一致性，允许用户通过加锁的方式来方式可能的更新或者修改操作。备份过程中数据是只读的，所有的写请求都会被阻塞

## 二、mysqldump备份和恢复
> MySQL自带的备份工具，是当前主流的备份软件之一，通过SQL语句将数据库中的数据导出成.sql文件，并且该文件是可读的，因此称之为逻辑备份

```sh
$ mysqldump -u用户名 -p密码 -h主机 数据库 表 --where "sql条件" 参数 > 路径/文件名.sql       # 备份
$ mysqldump -u用户名 -p密码 -h主机 数据库 表 < 路径/文件名.sql       # 恢复
$ mysqldump -h 主机IP -u用户名 -p密码 -t 数据库名 > 文件名.sql      # 例如: 只导出数据，不导出建表语句：
```

## 三、参数说明
- -P (--port) : 指定连接的端口号
- -d (--no-data)  : 不导出任何数据，指导出表结构
- -t (--no-create-info): 只导出数据，不导出建表语句
- -q (--quick): 用于转储大表，它强制mysqldump每次从服务器检索一行(不是所有行)并在输出前将它缓存到内存中
- --default-character-set=charset : 指定字符集(utf8)
- -R (--routines) : 转储存储程序(函数和程序)
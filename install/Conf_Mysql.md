# MySQL字符集配置

> * MySql默认编码是Latin1，不支持中文，以下为mysql支持中文编码的配置说明
> * 只对修改字符集编码后的内容生效，修改字符集编码前的数据依旧保持原来的字符集编码，可通过数据迁移等操作，使其与当前表字符集编码一致

## 查看MySQL数据库的字符集

查看MySQL数据库服务器和数据库的字符集

```sql
mysql> show variables like 'character_set_%';
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | utf8                       |
客户端字符集
| character_set_connection | utf8                       |
| character_set_database   | utf8                       |
数据库字符集
| character_set_filesystem | binary                     |
| character_set_results    | utf8                       |
| character_set_server     | utf8                       |
服务器字符集
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+
8 rows in set (0.00 sec)
```

查看MySQL数据库的字符集

```sql
mysql> SHOW CREATE DATABASE 数据库名;
+---------------+------------------------------------------------------------------------------------------------+
| Database      | Create Database                                                                                |
+---------------+------------------------------------------------------------------------------------------------+
| 数据库名 | CREATE DATABASE `数据库名` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */ |
+---------------+------------------------------------------------------------------------------------------------+
1 row in set (0.01 sec)
```

查看MySQL数据列字符集

```sql
mysql> SHOW FULL COLUMNS FROM 表名;
+---------------+------------+-----------------+------+-----+---------+-------+---------------------------------+---------+
| Field         | Type       | Collation       | Null | Key | Default | Extra | Privileges                      | Comment |
+---------------+------------+-----------------+------+-----+---------+-------+---------------------------------+---------+
| 字段名            | text       | utf8_unicode_ci | YES  |     | NULL    |       | select,insert,update,references |         |
| 字段名     | bigint(20) | NULL            | YES  |     | NULL    |       | select,insert,update,references |         |
+---------------+------------+-----------------+------+-----+---------+-------+---------------------------------+---------+
2 rows in set (0.00 sec)
```

## 配置MySQL字符集

### 永久修改

修改配置文件：/etc/my.cnf

- [mysqld]下添加init-connect='SET NAMES utf8'，用于指定客户端和服务器之间传递字符的编码为UTF8
- [mysqld]下添加default-collation = utf8_general_ci，数据库字符集,用于设置数据库的默认编码为utf8
- [mysqld]下添加character-set-server = utf8
- [mysql]下添加default-character-set=utf8
- [client]下添加default-character-set=utf8

```sh
[root@localhost mysql]# vim /etc/my.cnf
[mysqld]
datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock
user=mysql
# Disabling symbolic-links is recommended to prevent assorted security risks
symbolic-links=0
#collation-server = utf8_unicode_ci
init-connect='SET NAMES utf8'
character-set-server = utf8
default-collation = utf8_general_ci

[mysql_safe]
log-error=/var/log/mysqld.log

[mysql]
default-character-set=utf8

[client]
default-character-set=utf8
```

### 手动修改和临时修改
```sh
# --------------手动修改--------------------
# 修改数据库的字符编码
mysql> ALTER DATABASE `数据库名` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci
# 修改字段的字符编码
mysql> ALTER TABLE 字段名 CHANGE 字段名 字段名 字段类型 CHARACTER SET utf8 COLLATE utf8_general_ci;
# 修改表的字符编码
mysql> ALTER TABLE `表摩纳哥` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci
# -------------临时修改字符编码---------------
$ set character_set_results = utf8;
$ set character_set_server = utf8;
$ set character_set_client = utf8;
$ ...
```

## 备注
修改完字符编码之后需重启mysql生效（注：临时修改的重启后会恢复到改之前的样子）
```sh
$ service mysqld start
$ service mysqld restart
```

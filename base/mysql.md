# MySql技术
> * [MYSQL数据导入导出](http://blog.chinaunix.net/uid-16844903-id-3411118.html)

## SQL分类

> SQL语言共分为四大类：数据查询语言DQL，数据操纵语言DML，数据定义语言DDL，数据控制语言DCL
- 数据查询语言DQL:数据查询语言DQL基本结构是由SELECT子句，FROM子句，WHERE
- 数据操纵语言DML:主要有三种形式：插入：INSERT，更新：UPDATE， 删除：DELETE
- 数据定义语言DDL:创建数据库中的各种对象--表、视图、索引、同义词、聚簇等如：CREATE TABLE/VIEW/INDEX/SYN/CLUSTER
- 数据控制语言DCL：用来授予或回收访问数据库的某种特权，并控制数据库操纵事务发生的时间及效果，对数据库实行监视等。如：GRANT：授权, ROLLBACK [WORK] TO [SAVEPOINT]：回退到某一点。

## DDL
```sql
show index from 表名;     # 查询索引
alter table 表名 add 列名 数据类型;     # 添加列
alter table 表名 change 老列名 新列名 新数据类型;     # 修改列
alter table 表名 modify column 列名 新数据类型;      # 修改列数据类型
alter table 表名 add index 索引名 (字段1,字段2);     # 添加索引（多列）
ALTER TABLE table_name DROP INDEX index_name;     # 删除索引
create table 复制后表名 as select * from 复制前表名 限制条件;  # 复制表结构和数据
```

## DQL
```sql
reverse(substring(reverse(user_id), 8)) AS server
regexp_replace(substr(act_time,1,10),'-','')
substr(uid,1,1)
```

## 类型转换 - 字符串转换为数值类型

```
CAST(xxx  AS   类型), CONVERT(xxx,类型)
类型必须用下列的类型:
    二进制,同带binary前缀的效果 : BINARY    
    字符型,可带参数 : CHAR()     
    日期 : DATE     
    时间: TIME     
    日期时间型 : DATETIME     
    浮点数 : DECIMAL      
    整数 : SIGNED     
    无符号整数 : UNSIGNED
```

## 数据库/表导入导出
```sql
# mysql快速复制数据库
mysqldump -h IP地址 -u用户名 -p'密码' 数据库名 --add-drop-table | mysql -h IP地址 -u用户名 -p'密码' 数据库名
```

## 数据类型

- 日期和时间

| MySQL数据类型	| 含义 |
| ----	| ---- |
| date	|	3字节，日期，格式：2014-09-18	|
| time	|	3字节，时间，格式：08:42:30	|
| datetime	|	8字节，日期时间，格式：2014-09-18 08:42:30	|
| timestamp		|4字节，自动存储记录修改的时间	|
| year		|1字节，年份 	|

- 数值数据类型 - 整型

| MySQL数据类型 | 	含义（有符号） | 
| ----	| ---- |
| tinyint | 	1字节，范围（-128~127）| 
| smallint | 	2字节，范围（-32768~32767）| 
| mediumint | 	3字节，范围（-8388608~8388607）| 
| int	| 4字节，范围（-2147483648~2147483647）| 
| bigint	| 8字节，范围（+-9.22*10的18次方）| 

- 数值数据类型 - 浮点型

| MySQL数据类型	 | 含义 | 
| ----	| ---- |
| float(m, d)	 | 4字节，单精度浮点型，m总个数，d小数位 | 
| double(m, d)	 | 8字节，双精度浮点型，m总个数，d小数位 | 
| decimal(m, d)	 | decimal是存储为字符串的浮点数 | 

- 字符串数据类型

MySQL数据类型	| 	含义	| 
| ----	| ---- |
| char(n)	| 	固定长度，最多255个字符	| 
| varchar(n)	| 	可变长度，最多65535个字符	| 
| tinytext	| 	可变长度，最多255个字符	| 
| text		| 可变长度，最多65535个字符	| 
| mediumtext		| 可变长度，最多2的24次方-1个字符	| 
| longtext		| 可变长度，最多2的32次方-1个字符	| 

```
说明
1.char（n）和varchar（n）中括号中n代表字符的个数，并不代表字节个数，所以当使用了中文的时候(UTF8)意味着可以插入m个中文，但是实际会占用m*3个字节。
2.同时char和varchar最大的区别就在于char不管实际value都会占用n个字符的空间，而varchar只会占用实际字符应该占用的空间+1，并且实际空间+1<=n。
3.超过char和varchar的n设置后，字符串会被截断。
4.char的上限为255字节，varchar的上限65535字节，text的上限为65535。
5.char在存储的时候会截断尾部的空格，varchar和text不会。
6.varchar会使用1-3个字节来存储长度，text不会。
```






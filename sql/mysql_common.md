# MySQL基础

> - MySQL是一个RDBMS(Relational Database Management System)(关系型数据库管理系统)，由瑞典MySQL AB 公司开发，目前属于 Oracle 旗下产品
> - MySQL分为社区版和商业版
> - MySQL体积小、速度快、总体拥有成本低、开源免费

## 一、参考链接
- [mysql官网](https://dev.mysql.com)
- [MySQL Yum Repository](https://dev.mysql.com/doc/refman/5.7/en/linux-installation-yum-repo.html#yum-repo-select-series)
- [MySQL的高阶实用和概念](http://chars.tech/2017/05/29/mysql-advanced-study/?hmsr=toutiao.io&utm_medium=toutiao.io&utm_source=toutiao.io)


## 二、命令参数说明
| 参数 |	描述 | 
| ---- | ---- |
| -D,–database=name	| 打开指定数据库| 
| –delimiter=name	| 指定分隔符| 
| -h,–host=name| 	服务器名称| 
| -p,–password[=name]	| 密码| 
| -P,–port=# | 	端口号| 
| –prompt=name | 	设置提示符| 
| -u,–user=name | 	用户名| 
| -V,–version	| 输出版本信息并退出| 

## 三、加密函数
| 函数名称	| 描述 | 
| ---- | ---- |
| MD5()	| 信息摘要算法 | 
| PASSWORD() |	密码算法 | 

## 四、常用查询
```sql
# 显示当前服务器版本
SELECT VERSION(); 
# 显示当前日期时间
SELECT NOW();
# 显示当前用户 
SELECT USER();
```

### 4.1 获取更新数据的时间
```sql
select * from information_schema.TABLES where information_schema.TABLES.TABLE_SCHEMA = '数据库名' and information_schema.TABLES.TABLE_NAME = '表名';
```

### 4.2 字段类型所占字节

- 整型
    - tinyint ：占1个字节，用于存储(-128 至 127 的整数)(负2的7次幂 至 2的7次幂-1)
    - smallint ：占2个字节，用于存储(-32768 至 32767 的整数)(负2的15次幂 至 2的15次幂-1)
    - int ：占4个字节，用于存储(负2的31次幂 至 2的31次幂-1 的整数)
    - bigint ：占8个字节，用于存储(负2的63次幂 至 2的63次幂-1 的整数)
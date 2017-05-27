# 一些基本的SQL语句(基于ORACLE) 

## 一.查询表结构信息
- user_tab_columns：视图列出了特定于表的信息
- all_tab_columns：系统视图，说明数据库中所有表的字段结构内容
- all_col_columns：系统视图，说明数据库中所有列的字段结构内容
- user_tables：查询当前用户下所有的表
- all_tables：查询所有用户下的表
- dba_tables：查询包括系统表的所有表
- user_tab_commnents：查询表的备注信息
- user_col_comments：查询列的备注信息
- user_tablespace：查询所有表空间
- user_indexes：系统视图，存放的是索引的名称以及该索引是否是唯一索引等信息
- user_ind_column：系统视图，存放的是索引名称，对应的表和列等。
```sql
select * from user_tab_columns where table_name='TEST_1';
select * from user_tab_comments where TABLE_NAME=' ';
select * from user_tab_commnents where TABLE_NAME=' ';
```

## 二.函数的用法
- DECODE函数的用法

   DECODE函数相当于一条IF语句，它将输入数值与函数中的参数列表相比较，根据输入值返回一个对应值。DECODE还能识别和操作空值。
   ```sql
   DECODE(input_value,value,result[,value,result...][,default_result]);
   ```
- 截取日期
    ```sql
    extract(year from sysdate)          # 获取当前日期的年
    extract(month from sysdate)         # 获取当前日期的月
    extract(day from sysdate)           # 获取当前日期的日 
    last_day(sysdate)                   # 获取当前月份的最后一天
    add_months(sysdate,3)               # 将当前月份加上3个月
    ```
- 日期的转换
    ```sql
    to_char(sysdate,'Month DD YYYY')
    to_char(sysdate,'MM DD YYYY')
    to_char(sysdate,'DS')
    to_char(sysdate,'DL')
    to_char(23542,'$99,999.99')
    ```
- instr函数

    返回要查找的字符串在源字符串中的位置，索引位置从1开始，如果没有找到，instr函数返回0.
    instr('源字符串','要查找的字符串','开始查找的位置','要查找的字符串第几次出现')
    ```sql
    例：instr('ABC','B')
    区别：in('A','B')
    ```
## 三.区别
- truncate,delete,drop之间的区别
    - truncate table：删除内容，释放空间，但不删除定义，删除的数据不能恢复。
    - delete table：删除内容，不删除定义，不释放表空间，删除的数据可恢复。
    - drop table：删除内容和定义，释放表空间。
    
    ```
    备注：
    truncate table 比delete table 速度快，且使用的系统和事务日志资源少，delete语句每次删除一行，并在事务日志中为所删除的每行记录一项。
    truncate table 通过释放存储表数据所用的数据页来删除数据，并且只有在事务日志中记录页的释放
    ```

## 四.操作
- 解锁用户并设定密码
    ```sql
    alter user 用户名 account unlock identified by 密码;
    ```
- sqlplus连接数据库
    ```sql
    sqlplus 用户名/密码@数据库名
    ```
- 为表添加备注
    ```sql
    comment on table 表名 is '备注';
    comment on table 表名.列名 is '备注';
    ```
- 建表
    ```sql
    create table test_ccc(ids number);      # 创建表
    alter table tast_ccc add(id2 number);   # 添加列
    alter table test_ccc drop column ids;   # 删除列
    ```
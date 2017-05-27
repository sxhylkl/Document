# in、not in、exists、not exists的用法和区别

## 一、原始数据表
```sql
mysql> select * from aa;
+------+------+
| id   | name |
+------+------+
|    1 | a    |
|    2 | b    |
|    3 | c    |
+------+------+
3 rows in set (0.00 sec)

mysql> select * from bb;
+------+-------+
| id   | value |
+------+-------+
|    1 |    11 |
|    2 |    22 |
|    5 |    55 |
3 rows in set (0.00 sec)
```

## 二、用法和区别

- exists用于检查子查询是否至少会返回一行数据，该子查询并不返回任何数据，而是返回值True或False
- in 和 exists 是可以互相替换的，只是效率有所不同
- not in 和 not exist 在子表中没有null值时是可以互相替换的，但是not in的效率没有not exists的效率高。当子表中存在null值时，是不能not in的，原因如下：
    - null代表未知，表示可能什么都是，也可能什么都不是，null值与其他任何值作比较或者计算时，结果都为null(oracle中默认null最大,mysql中默认null最小)
    - in 相当于 or 连接
        ```sql
        mysql> select id,name from aa where id in (select id from bb);
        <!-- 等价于 -->
        mysql> select id, name from aa where id = 1 or id = 2 or id = null;
        ```
    - not in 相当于 and 连接，只有当所有条件都满足时才有结果
        ```sql
        mysql> select id,name from aa where id not in (select id from bb);
        Empty set (0.00 sec)
        <!-- 等价于 -->
        mysql> select id,name from aa where id != 1 and id !=2 and id !=5 and id !=null;
        Empty set (0.00 sec)
        ```
**正常值时**
```sql
mysql>  select id,name from aa where id in (select id from bb);
+------+------+
| id   | name |
+------+------+
|    1 | a    |
|    2 | b    |
+------+------+
2 rows in set (0.00 sec)

mysql> select id,name from aa where EXISTS(select * from bb where aa.id = bb.id);
+------+------+
| id   | name |
+------+------+
|    1 | a    |
|    2 | b    |
+------+------+
2 rows in set (0.00 sec)

mysql> select id,name from aa where id not in (select id from bb);
+------+------+
| id   | name |
+------+------+
|    3 | c    |
+------+------+
1 row in set (0.00 sec)

mysql> select id,name from aa where not exists(select * from bb where aa.id=bb.id);
+------+------+
| id   | name |
+------+------+
|    3 | c    |
+------+------+
1 row in set (0.00 sec)
```
**子表为null值时**
```sql
mysql> select * from bb;
+------+-------+
| id   | value |
+------+-------+
|    1 |    11 |
|    2 |    22 |
|    5 |    55 |
| NULL |    12 |
+------+-------+
4 rows in set (0.00 sec)

mysql> select id,name from aa where id not in (select id from bb);
Empty set (0.00 sec)

mysql> select id,name from aa where not exists(select * from bb where aa.id=bb.id);
+------+------+
| id   | name |
+------+------+
|    3 | c    |
+------+------+
1 row in set (0.00 sec)
```

## 三、效率

a表(小表)：4000条数据      
b表(大表)：10000条数据     

**in和exists**
- 当子表比主表数据量大时，适合使用exists
- 当主表和子表数据量差不多时，exists和in的效率也是差不多的
- exists的执行次数为主表的执行次数
- in通过内存遍历比较，exists通过查询数据库比较
```sql
mysql> select count(1) from b where exists(select * from a where a.ds=b.ds);
mysql> select count(1) from b where ds in (select ds from a);
mysql> select count(1) from a where exists(select * from b where b.ds=a.ds);
mysql> select count(1) from a where ds in (select ds from b);
```

**not in和not exists**
- not exists效率高于not in
```sql
-- 效率高
mysql> select count(1) from dis_spend_detail where not exists(select * from dis_daily_data where dis_daily_data.ds=dis_spend_detail.ds);
1 row in set (1 min 2.94 sec)
-- 效率低
mysql> select count(1) from dis_spend_detail where ds not in (select ds from dis_daily_data);
1 row in set (1 min 3.63 sec)
-- 效率高
mysql> select count(1) from dis_daily_data where not exists(select * from dis_spend_detail where dis_spend_detail.ds=dis_daily_data.ds);
1 row in set (39.18 sec)
-- 效率低
mysql> select count(1) from dis_daily_data where ds not in (select ds from dis_spend_detail);
1 row in set (40.07 sec)
```
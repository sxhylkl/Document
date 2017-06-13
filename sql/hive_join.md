# hive中各种join的区别

## 原始数据表
```sql
> select * from aa;
+--------+----------+--+
| aa.id  | aa.name  |
+--------+----------+--+
| 1      | a        |
| 2      | b        |
+--------+----------+--+
> select * from bb;
+--------+----------+--+
| bb.id  | bb.name  |
+--------+----------+--+
| 1      | b        |
| 3      | c        |
+--------+----------+--+
```
## 一、left join
```sql
> select * from aa left join bb on aa.id =bb.id;
+--------+----------+--------+----------+--+
| aa.id  | aa.name  | bb.id  | bb.name  |
+--------+----------+--------+----------+--+
| 1      | a        | 1      | b        |
| 2      | b        | NULL   | NULL     |
+--------+----------+--------+----------+--+
```
## 二、left semi join
```sql
> select * from aa left semi join bb on aa.id =bb.id;
+--------+----------+--+
| aa.id  | aa.name  |
+--------+----------+--+
| 1      | a        |
+--------+----------+--+
```
## 三、left outer join
```sql
> select * from aa left outer join bb on aa.id =bb.id;
+--------+----------+--------+----------+--+
| aa.id  | aa.name  | bb.id  | bb.name  |
+--------+----------+--------+----------+--+
| 1      | a        | 1      | b        |
| 2      | b        | NULL   | NULL     |
+--------+----------+--------+----------+--+
```
## 四、right outer join
```sql
> select * from aa right outer join bb on aa.id =bb.id;
+--------+----------+--------+----------+--+
| aa.id  | aa.name  | bb.id  | bb.name  |
+--------+----------+--------+----------+--+
| 1      | a        | 1      | b        |
| NULL   | NULL     | 3      | c        |
+--------+----------+--------+----------+--+
```
## 五、join
```sql
> select * from aa join bb on aa.id =bb.id;
+--------+----------+--------+----------+--+
| aa.id  | aa.name  | bb.id  | bb.name  |
+--------+----------+--------+----------+--+
| 1      | a        | 1      | b        |
+--------+----------+--------+----------+--+
```
# Hive和impala

- [hive手册](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF)
- [参考函数](http://blog.csdn.net/mayp1/article/details/51415854)

## 常用的日期处理函数
```sql
$ select fresh_time,create_time,DATEDIFF(fresh_time,create_time)  from a;
2015-07-01 19:16:57	    2015-03-20 16:57:02	    103
$ select fresh_time,day(fresh_time),dayofmonth(fresh_time) from a; 
2016-12-06 14:03:06	    6	    6
$ select fresh_time,dayname(fresh_time) from a; 
2016-12-06 14:03:06	    Tuesday
$ select fresh_time,DAYOFWEEK(fresh_time) from a; 
2016-12-06 14:03:06	    3
$ select fresh_time,HOURS_ADD(reg_time,1) from a; 
2016-12-06 14:03:06	    2016-12-06 15:03:06
$ select fresh_time,to_date(reg_time) from a; 
2016-12-06 14:03:06	    2016-12-06
```

| 函数 | 说明 |
| ---- | ---- |
| DATEDIFF | 两个日期间隔的天数 |
| day      | 返回该日期在月内的日 |
| dayofmonth | 返回该日期在月内的日 |
| dayname | 返回周的英文名,例（Tuesday） |
| DAYOFWEEK | 返回周的数字序号，1(Sunday)到7(Saturday) |
| DAYOFYEAR | 本年的第多少天 |
| HOUR | 返回字符串的小时 |
| HOURS_ADD | 指定日期加n小时 |
| HOURS_SUB | 指定日期减n小时 |
| month     | 返回日期的月份 |
| MONTHS_ADD | 指定日期加n月 |
| MONTHS_SUB | 指定日期减n月 |
| MONTHS_BETWEEN | 两个日期间相差的月数，返回浮点数 |
| to_date | 返回时间戳或字符串的日期部分 |


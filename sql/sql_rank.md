# SQL排序

## row_number
row_number() over() 用于按顺序排序（不并列）
```sql
select ds,level,row_number() over(partition by ds order by level desc) rn from table_name;
```

## rank
rank() over() 用于并列排序（不按顺序、按照整体排名）
```sql
select ds,level,rank() over(partition by ds order by level desc) rn from table_name;
```

## dense_rank
dense_rank() 用于并列排序（按顺序）
```sql
select ds,level,dense_rank() over(partition by ds order by level desc) rn from table_name;
```
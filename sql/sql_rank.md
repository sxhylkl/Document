# SQL排序

## row_number
row_number() over() 用于按顺序排序（不并列）
```sql
SELECT ds,
       level,
       row_number() over(partition BY ds ORDER BY level DESC) rn
FROM TABLE_NAME;
```

## rank
rank() over() 用于并列排序（不按顺序、按照整体排名）
```sql
SELECT ds,
       LEVEL,
       rank() over(partition BY ds ORDER BY level DESC) rn
FROM TABLE_NAME;

```

## dense_rank
dense_rank() 用于并列排序（按顺序）
```sql
SELECT ds,
       LEVEL,
       dense_rank() over(partition BY ds ORDER BY level DESC) rn
FROM TABLE_NAME;
```
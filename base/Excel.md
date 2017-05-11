# Excel

## 小技巧

```
F4：锁定选中列    # 例如：$D$1
```

## 常用函数

```
SEARCH函数语法：search(找谁，从什么里面找，从第几个找),第三个参数一般情况下可以忽略，默认为从第一个参数开始找。
=SEARCH($D$1,A2)
IFERROR(value,value_if_error)，如果是正常值，返回value，如果是错误值，返回value_if_error。
=IFERROR(SEARCH($D$1,A2),0)
COUNTA(表格区间)，计算区间内有值的个数
=COUNTA(A2:D2)
INDEX(array，row_num，column_num)，即为（引用的区域，引用区域里的第几行，引用区域里的第几列）
=INDEX(A2:B3,2,2)
```


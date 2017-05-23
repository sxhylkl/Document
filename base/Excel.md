# Excel

## 小技巧
```
F4：锁定选中列(单元格)    # 例如：$D$1
```

## 快捷键

|  快捷键  |  说明   |
| ----     |  ----  | ----  |
|  F2  |  编辑单元格   |
|  ENTER  |  切换到下方相邻单元格（同一列）   |
|  SHIFT+ENTER  |  切换到上方相邻单元格（同一列）   |
|  CTRL+方向键  |  快速移动光标至最上，下，左，右   |
|  SHIFT  |  连续选择单元格   |
|  CTRL+SHIFT+方向键  |  快速连续选择单元格   |
|  TAB  |  切换到右侧相邻单元格（同一行）   |
|  SHIFT+TAB  |  切换到左侧相邻单元格（同一行）   |
|  CTRL+SHIFT+"+"  |  增加列   |
|  CTRL+"-"  |  删除列   |
|  CTRL+SHIFT+"L"  |  筛选   |
|  CTRL+H  |  替换（“*”号在替换中的应用）   |
|  CTRL+F  |  查询   |
|  CTRL+PAGEDOWN  |  切换到下一个标签页   |
|  CTRL+PAGEUP  |  切换到上一个标签页   |
|  光标在单元格边缘处，变为“+”后，双击  |  快速填充（当左侧单元格为空时，停止填充）   |
|  CTRL+D  |  快速填充相同数据   |
|  CTRL+C  |  复制   |
|  CTRL+V  |  粘贴   |
|  CTRL+X  |  剪切   |
|  CTRL+Z  |  取消本次操作   |
|  CTRL+S  |  存储   |
|  CTRL+";"  |  插入当前日期   |
|  CTRL+SHIFT+":"  |  插入当前时间   |



## 常用函数

| 函数     |  说明  |
| ----     |  ----  |
|  MODE  |  众数  |
|  MEDIAN  |  中位数  |
|  ROUND  |  四舍五入取整  |
|  ROUNDUP  |  向上取整  |
|  ROUNDDOWN  |  向下取整  |
|  VALUE  |  将代表数值的文本型字符串转换为数值型  |
|  COUNT  |    |
|  COUNTIF  |   |
|  MAX  |    |
|  MIN  |    |
|  DAY  |    |
|  DAYS  |    |
|  RANK.EQ  |    |
|  RANK  |    |


```
=VLOOKUP(列,列,第几个值,0)
=HLOOKUP(列,列,第几个值,0)
SEARCH函数语法：search(找谁，从什么里面找，从第几个找),第三个参数一般情况下可以忽略，默认为从第一个参数开始找。
=SEARCH($D$1,A2)
IFERROR(value,value_if_error)，如果是正常值，返回value，如果是错误值，返回value_if_error。
=IFERROR(SEARCH($D$1,A2),0)
COUNTA(表格区间)，计算区间内有值的个数
=COUNTA(A2:D2)
INDEX(array，row_num，column_num)，即为（引用的区域，引用区域里的第几行，引用区域里的第几列）
=INDEX(A2:B3,2,2)
```
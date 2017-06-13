# Python基础

## 一、assert
> assert断言是声明其布尔值必须为真的判定，如果发生异常就说明表达示为假，就会触发异常

- 语法：assert 表达式 [, 异常说明]
- 例子：
```py
In [224]: assert 1==1
In [229]: assert 1==3,'值不相等'
In [226]: assert isinstance(['a','b'],list)
In [228]: assert isinstance('aa',list),'不是列表'
```
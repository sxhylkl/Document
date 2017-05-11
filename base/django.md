# Django

- [参考文档](http://www.ziqiangxuetang.com/django/django-tutorial.html)

## widthratio

> widthratio 通常用来显示图表，比例时用的，一个数字占了多少百分比等

```
乘法 A*B: {% widthratio A 1 B %}
除法 A/B: {% widthratio A B 1 %}

利用 add 这个filter ,可以做更疯狂的事:

计算 A^2: {% widthratio A 1 A %}
计算 (A+B)^2: {% widthratio A|add:B 1 A|add:B %}
计算 (A+B) * (C+D): {% widthratio A|add:B 1 C|add:D %}
```
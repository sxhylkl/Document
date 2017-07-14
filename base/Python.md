# Python技术

[参考文档](https://my.oschina.net/zyzzy/blog/115096)

## Counter计数器(统计字符出现的个数)

```py
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from collections import Counter

print Counter('aabbccdser')
print Counter('aabbccdser')['a']
```

## zip

```python
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
print zip(x, y, z)
结果：[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
print zip(x, u)
结果：[(1, 4), (2, 5), (3, 6)]
print zip(x)
结果：[(1,), (2,), (3,)]
print zip()
结果：[]
print zip(*zip(x, y, z))
结果：[(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print zip(* [x] * 3)
结果：[(1, 1, 1), (2, 2, 2), (3, 3, 3)]
```

## lambda

```python
格式：lambda 一个或多个参数: 一个表达式
square_root = lambda x: math.sqrt(x)    # def square_root(x): return math.sqrt(x)
sum = lambda x, y:   x + y     # def sum(x,y): return x + y
dd = lambda x: x if x > 100 else 0      # 如果x>100,返回x，否则返回0
print sum(2,3)
结果：5
print square_root(4)
结果：2
print dd(101)
结果：101
print dd(99)
结果： 0
# =============================================
lambda表达式常用来编写行为的列表或字典
L = [(lambda x: x**2),  
    (lambda x: x**3),  
    (lambda x: x**4)]  
print L[0](2),L[1](2),L[2](2)  

D = {'f1':(lambda: 2+3),  
    'f2':(lambda: 2*3),  
    'f3':(lambda: 2**3)}  
print D['f1'](),D['f2'](),D['f3']() 
# =============================================
map函数可以在序列中映射函数进行操作
def inc(x): return x+1 
L = [1,2,3,4]  
print map(inc,L)  
print map((lambda x: x+1),L) 
结果：[2, 3, 4, 5]
# =============================================
列表解析可以实现map函数同样的功能，而且往往比map要快
print [x**2 for x in range(10)]  
print map((lambda x: x**2), range(10))  
```

## os.walk()

> * 获取指定文件夹下的文件名

```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os  
for dirpath, dirname, filename in os.walk(path):  
    print dirpath #当前目录路径  
    print dirname #当前路径下所有子目录  
    print filename #当前路径下所有非目录子文件
```

## os.listdir()

> * 获取指定文件夹下的文件名，os.listdir()函数得到的是仅当前路径下的文件名

```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os  
print os.listdir(path):
```

## 字符串操作

```python
# 字符串替换：str.replace(替换前的值，替换后的值)
print 'abcda'.replace('a','e')
结果：ebcde
# 字符串是否以某个或几个字符开始：str.startswith('start_str'),结果以True或者False返回
print 'raw_sss'.startswith('raw_')
结果：True
print 'raw_sss'.startswith('dis_')
结果：False
# 字符串是否以某个或几个字符结束：str.endswith('start_str'),结果以True或者False返回
print 'aa.py'.endswith('.py')
结果：True
print 'aa.py'.endswith('.md')
结果：False
# 字符串连接
print '\t'.join(map(str,['a','b','c'])) + '\n'
结果：a	b	c
# 字符串分割
print 'as@123'.split('@')
结果：['as', '123']
# 移除字符串头尾指定的字符（默认为空格）
print ' ddd '.strip()
结果： 'ddd'
print 'a234a'.strip('a')
结果： '234'
```

## 日期操作

```python
# 当天日期
print datetime.date.today()
结果：datetime.date(2017, 4, 25)
# 日期加减
print datetime.date.today() + datetime.timedelta(days=1)
结果：datetime.date(2017, 4, 26)
print datetime.date.today() - datetime.timedelta(days=1)
结果：datetime.date(2017, 4, 24)
# 获取当时的时间
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
结果：2017-04-25 16:50:27
```

## 文件操作(os.path)

```python
print os.path.join('/usr/aa','bb','cc','dd.py')     # 返回文件名
结果： '/usr/aa/bb/cc/dd.py'
local_path='/home/data/aa/bb_20170101'
print os.path.basename(local_path)      # 返回文件名
结果：bb_20170101
print os.path.sep
结果：'/'
```

| 加工方法  |  说明   |
| ----     |  ----  |
| os.path.abspath(path)   |  返回绝对路径  |
| os.path.basename(path)   |  返回文件名  |
| os.path.commonprefix(list)   |  返回list(多个路径)中，所有path共有的最长的路径。  |
| os.path.dirname(path)   |  返回文件路径  |
| os.path.exists(path)    |  路径存在则返回True,路径损坏返回False  |
| os.path.lexists    |  路径存在则返回True,路径损坏也返回True  |
| os.path.expanduser(path)    |  把path中包含的"~"和"~user"转换成用户目录  |
| os.path.expandvars(path)    |  根据环境变量的值替换path中包含的”$name”和”${name}”  |
| os.path.getatime(path)    |  返回最后一次进入此path的时间。  |
| os.path.getmtime(path)    |  返回在此path下最后一次修改的时间。  |
| os.path.getctime(path)    |  返回path的大小  |
| os.path.getsize(path)    |  返回文件大小，如果文件不存在就返回错误  |
| os.path.isabs(path)    |  判断是否为绝对路径  |
| os.path.isfile(path)    |  判断路径是否为文件  |
| os.path.isdir(path)    |  判断路径是否为目录  |
| os.path.islink(path)    |  判断路径是否为链接  |
| os.path.ismount(path)    |  判断路径是否为挂载点（）  |
| os.path.join(path1[, path2[, ...]])    |  把目录和文件名合成一个路径  |
| os.path.normcase(path)    |  转换path的大小写和斜杠  |
| os.path.normpath(path)    |  规范path字符串形式  |
| os.path.realpath(path)    |  返回path的真实路径  |
| os.path.relpath(path[, start])    |  从start开始计算相对路径  |
| os.path.samefile(path1, path2)    |  判断目录或文件是否相同  |
| os.path.sameopenfile(fp1, fp2)    |  判断fp1和fp2是否指向同一文件  |
| os.path.samestat(stat1, stat2)    |  判断stat tuple stat1和stat2是否指向同一个文件  |
| os.path.split(path)    |  把路径分割成dirname和basename，返回一个元组  |
| os.path.splitdrive(path)     |  一般用在windows下，返回驱动器名和路径组成的元组  |
| os.path.splitext(path)    |  分割路径，返回路径名和文件扩展名的元组  |
| os.path.splitunc(path)    |  把路径分割为加载点与文件  |
| os.path.walk(path, visit, arg)    |  遍历path，进入每个目录都调用visit函数，visit函数必须有  |
| os.path.supports_unicode_filenames    |  设置是否支持unicode路径名  |

## execfile

> * execfile(filename [,globals [,locals ]])函数可以用来执行一个文件

```py
$ vim aa.py
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
print 3+4
In [56]: execfile(r'/Users/kaiqigu/aa.py')
7
```

## dict.items()

```py
In [60]: a = {'a':1,'b':2}
In [61]: a.items()
Out[61]: [('a', 1), ('b', 2)]
```

## str()和repr()
```
函数str() 用于将值转化为适于人阅读的形式，而repr() 转化为供解释器读取的形式
epr()函数得到的字符串通常可以用来重新获得该对象，通常情况下 obj==eval(repr(obj)) 这个等式是成立的。
repr()绝大多数情况下（不是所有）可以通过求值运算（内建函数eval()）重新得到该对象。
str()则不同，它生成一个对象的可读性好的字符串表示，结果通常无法用eval()求值，但适合print输出搜索。
```

## 字典
```
card_shangzheng_pos = set(range(1, 10, 1))
```

## map

map(function, iterable, ...)    #对可迭代函数'iterable'中的每一个元素应用‘function’方法，将结果作为list返回

```py
In [48]: def add100(x):
   ....:         return x + 100
   ....:
In [49]: list1 = [11,22,33]
In [50]: map(add100,list1)
Out[50]: [111, 122, 133]
In [51]: [add100(i) for i in list1]
Out[51]: [111, 122, 133]
# ------------------------------------------
>>> def abc(a, b, c):
...     return a*10000 + b*100 + c
>>> list1 = [11,22,33]
>>> list2 = [44,55,66]
>>> list3 = [77,88,99]
>>> map(abc,list1,list2,list3)
[114477, 225588, 336699]
# ------------------------------------------
'\t'.join(map(str, [user_id, server, account, coin))
'\t'.join(map(str, ['1','2','3']))
```


```py
In [84]: print c
[1, 2, 4, 6, 3, 7]
# 列表推导式
In [85]: [i for i in c if i%2==0]
Out[85]: [2, 4, 6]
In [154]: a = [2,4,6]
In [155]: b = [1,3,9]
In [158]: [i * j for i in a for j in b]
Out[158]: [2, 6, 18, 4, 12, 36, 6, 18, 54]
# [i * j for i in a for j in b] 等价于下列for循环
for i in a:
    for j in b:
        print i*j
# 遍历字典
In [168]: for name ,value in a.items():
   .....:     print name,value
```

## 数据结构
列表： 可重复，可修改，字符串和元组不可修改，[]
元组： 可重复，不可修改，(,)
集合： 无序不重复，用于消除重复元素和检测成员，set()
字典： 键值对的结合，且键不可重复，dict()，{}

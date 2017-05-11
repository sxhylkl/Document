website.md# pandas技术整合

> * [官方文档](http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy)
> * [pandas的pdf文档](http://pandas.pydata.org/pandas-docs/version/0.19.2/pandas.pdf)
> * [参考文档](https://docs.scipy.org/doc/numpy/reference/generated/numpy.isinf.html)
> * [pandas的git文档](https://github.com/pandas-dev/pandas)

## 常用导入包
```
import numpy as np
import pandas as pd
from pandas import Timestamp
```

## 技术整合

- 创建DataFrame

```py
In [62]: pd.DataFrame([('a', 1), ('b', 2)], columns=['name', 'value'])
Out[62]:
  name  value
0      a          1
1      b          2
In [26]: df = pd.DataFrame(np.random.randn(6, 4), columns=['one', 'two', 'three','four'],index=list('abcdef'))

In [27]: df
Out[27]:
        one       two     three      four
a -0.844883 -0.227276  0.061315 -0.731842
b -0.381648 -0.146314 -0.741698  0.105474
c -0.368688 -0.125157  0.257138 -0.942163
d -0.397223 -1.019062  1.426528 -0.147622
e -0.002957  1.182453  0.290078  0.905151
f -1.861510 -0.382731  0.173068  1.403485
```

- 值替换

```py
df.fillna({'列名': '值'})   # 指定列填充缺失值
df.fillna(填充后的值)        # df中所有为空的字段都填充值
df.replace({'列名':{替换前的值:替换后的值}})    # 值替换,is_new_pay
df.replace({np.inf:0})  # 将inf替换为0
np.isinf(np.inf)    # 判断是否是inf
```

```python
# 排除与另一个df相同的数据
result_df = assist_df[~assist_df['user_id'].isin(gs_df.user_id.values)]
# 通过agg计算
assist_df.groupby(['ds', 'plat']).agg({
        'user_id': 'count', 
        'uid': 'nunique',   # uid去重并计算总数
        'coin': 'sum',
        'spend_coin': 'sum'
    }).reset_index()
# 字段重命名
df.rename(columns={'user_id': 'act_user_num','coin': 'coin_save')
# 处理指定列的每一行数据
bowl_df['sort'] = bowl_df['args'].map(lambda s: eval(str(s))['sort'][0])
grouped_result_df2['red_1'] = grouped_result_df2['evo_counter'].map(lambda x: x.get(evo, 0))
# 修改列的数据类型
bowl_df['num'] = bowl_df['num'].astype('int')
# 行转列
df.pivot_table('times', ['ds', 'plat'], 'sort')
# 取指定的数据
pub_result_df = result_df[result_df.plat == 'g']
# 列的除法运算
result_df['avg_coin_save'] = result_df['coin_save'].div(result_df['dau'],
                                                            fill_value=0)
# 通过集合计算总数
keep_df['dau'] = len(set(act_df.loc[act_df.act_ds == reg_date].uid.tolist()))
# map函数：map()的两个参数一个是函数名，另一个是列表或元组。
In [120]: a = [1,2,3,4,5]
In [121]: map(lambda x:x+3,a)
Out[121]: [4, 5, 6, 7, 8]
# filter（）函数包括两个参数，分别是function和list。该函数根据function参数返回的结果是否为真来过滤list参数中的项，最后返回一个新列表
Out[122]: a = [1, 2, 3, 4, 5]
In [124]: filter(lambda x:x>3,a)
Out[124]: [4, 5]
# df数据替换
In [142]: pay_df.replace('q25','aa')
# cut统计
df.groupby(['vip_level',pd.cut(df.sum_money,ranges)]).count().uid.reset_index()
# 排序
df = df.sort_values(by=column, ascending=ascend)[:num]
# categories
pd.cut(assist_df.order_money,ranges).cat.categories
# 操作一列
df.列名.str.replace('-', '')
df.列名.str[:4]
actionlog_df['spend'] = actionlog_df['coin_diff'].map(
     lambda s: s if s < 0 else 0)
# 保留小数位数
df.round(2)   # 保留两位小数
df.round({'A': 0, 'C': 2})    # 指定列保留小数位数
# 获取季度时间
from pandas import Timestamp
print Timestamp('2012Q2')
print Timestamp('2012Q1')
```

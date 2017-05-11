# Python环境搭建

> [参考文档](https://github.com/cloudera/impyla)

## yum安装
- gcc-c++
- cyrus-sasl-devel 
- cyrus-sasl-plain

## pip安装

- thrift_sasl
- sasl
- impyla
- ipython
- pymysql
- pyhive
- SQLAlchemy
- pandas
- numpy
- thrift==0.9.3

## MAC环境变量配置
```sh
# 查找当前pyhton的site-packages目录
$ python -c 'import site; print site.getsitepackages()[0]'
//anaconda/lib/python2.7/site-packages
# 进入项目根目录下(/Users/kaiqigu/Documents/scripts/bi_scripts)执行以下命令
$ echo `pwd` > //anaconda/lib/python2.7/site-packages/bi.pth
# 使用以下命令查看当前目录是否在输出中
$ python -c 'import sys; print sys.path'
# ---------------------------------------------
# 删除环境变量中的内容
$ sys.path.remove('/Users/kaiqigu/Downloads/bi_scripts')
```

## 各种坑
- 坑一
```sh
问题场景：pip install sasl时遇到问题
error: command 'gcc' failed with exit status 1
解决办法：yum install -y cyrus-sasl-devel cyrus-sasl-plain
```
- 坑二
```sh
问题场景：执行impala的查询语句时
AttributeError: 'TBufferedTransport' object has no attribute 'trans'
解决办法：thrift版本问题，pip install thrift=0.9.3
```


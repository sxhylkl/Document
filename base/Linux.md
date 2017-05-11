# Linux

## for的使用

```sh
$ for i in {1..5};do echo ${i};done
1
2
3
4
5
```

## 基本命令

```sh
echo 'cc' >> a.txt      # 以追加形式向文件中添加内容
echo 'cc' > a.txt       # 重新写入文件
echo `date +%Y-%m-%d`   # 格式化日期
echo `date +%Y%m%d`     # 格式化日期
```

## 简单的传参脚本
```sh
#!/bin/sh
DATE=$1
echo $DATE
```
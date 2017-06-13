# Linux

> * [Linux命令大全](http://man.linuxde.net)
> * [鸟哥的linux私房菜](http://linux.vbird.org/new_linux.php)
> * [VIM常用操作命令梳理](https://zhuanlan.zhihu.com/p/27232184?hmsr=toutiao.io&utm_medium=toutiao.io&utm_source=toutiao.io)

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
# Linux基础

- [centos7分区](http://blog.csdn.net/huangxiang360729/article/details/52639673)
- [关机重启参考文档](http://www.centoscn.com/CentOS/help/2013/0725/559.html)
- [Linux进程状态](http://www.cnblogs.com/itech/p/3208261.html)

## 常用的文件处理
```sh
touch dd          # 创建空文件
cp -f dd ee       # 复制文件(是否覆盖不提醒)
cp -u dd ee       # 文件变更时复制
stat dd           # 查看文件统计信息
cat dd            # 查看整个文件(-n加上行号，-s压缩到单个空白行，-T去掉制表符)
more dd           # more命令:每页的数据内容(space 翻页,z 翻页,q 退出,= 行号,/ 查询内容 查找匹配)
less dd           # 和more基本差不多，是more的升级版本
tail -n 10 dd     # 查看部分文件（tail）(-n 最后n行)
tail -10 dd       # 查看部分文件（tail）(-n 最后n行)
tail -f dd        # 动态显示文件的末尾数据 
tail -10 dd       # 查看部分文件(head)(开始n行)
cp -arf /home/  /backup/    # 复制文件（如果复制到的目录存在相同）
# -a  保持目录或文件的所有属性
# -r  递归持续复制，用于目录的复制
# -f  强制复制，不需要询问
```

# 进程
## 1.查看进程
```sh
ps          # 查看进程
ps -ef      # 查看所有进程
pstree -p   # 进程树
```
## 2.结束进程
```sh
kill 进程号      # 根据进程号结束进程
killall http*   # 根据进程名批量结束进程
```
# 磁盘空间
```sh
df
df -h   # 用M、G
du      # 当前目录下的所有文件的空间使用情况，-s每个参数的总计，-h用M、G统计
```
# 排序
```sh
sort aa     # 按字符排序
sort -n aa  # 按数字排序
sort -M aa  # 按月份排序
```
# 搜索数据（grep）
```sh
-n  # 所在行号
-c  # 匹配的行数
[]  # 正则表达式
```
# 输入/输出重定向
```sh
# 输出重定向（>）
date > ss
who >aa
# 注：重定向操作创建文件并将命令的输出重定向到文件中，如果文件已存在，则会用新文件覆盖原文件
# 追加重定向文件（当不想文件覆盖时使用）(<<)
who >> ss
# ---------------------------------------------
# 输入重定向(<)
[root@localhost test]# wc ss
  7  36 341 ss
[root@localhost test]# wc < ss
  7  36 341
# 注：wc:文本的行数、词数、字节数，输出重定向将内容指向命令
# 内联输入重定向(<<)(注：开始和结尾必须一致)
# ---------------------------------------------
[root@localhost test]# wc << EOF
> dfsa
> dfs
> ss
> EOF
 3  3 12
```

# 计算列的和
```sh
[root@localhost home]# cat aa
1   3   5
2   4   6
4   6   9
[root@localhost home]# cat aa | awk '{sum1+= $1}END{print sum1}'
7
[root@localhost home]# cat aa | awk '{sum1+= $2}END{print sum1}'
13
[root@localhost home]# cat aa | awk '{sum1+= $3}END{print sum1}'
20
第一列和第二列的平均值：
cat aa | awk '{sum1+=$1;sum2+=$2;count++}END{print sum1/count,sum2/count}'
```

# 编写脚本
- if-then
```sh
if date
then
    echo date
fi
```

- if-then-else
```sh
if false
then
    date
else
    echo "it false"
fi
```

- if-then-elif
```sh
if false
then
    date
elif date
then
    echo "it dt"
fi
```

- 数值比较
```sh
# -eq   # 相等
# -ge   # 大于等于
# -gt   # 大于
# -le   # 小于等于
# -lt   # 小于
# -ne   # 不等于
val=10
if [ $val -eq 10 ]
then
    echo "it's equal"
fi
```

- 字符串比较(=,!=,<,>,-n str1,-z str1)
```sh
# -n和-z：用于检查字符串变量是否含有数据
# -n str1   #检查str1的长度是否非0
# -z str1   #检查str1的长度是否为0
val1=aa
val2=aa
if [ $val1 = $val2 ]
then
    echo "it's equal"
fi
# ----------------
val1=aa
val2=aa
if [ -n $val1 ]
then
    echo "it's not 0"
fi
```

# 其他命令
```sh
# 改变用户对一些命令的权限
sudo -i
# 查看当前文件夹下文件大小
du -sh *
```

# crontab -l
```
一般用命令：crontab -l
crontab命令简介：
crontab命令常见于Unix和类Unix的操作系统之中，用于设置周期性被执行的指令。该命令从标准输入设备读取指令，并将其存放于“crontab”文件中，以供之后读取和执行。
使用时可用参数：
-e [UserName]: 执行文字编辑器来设定时程表，内定的文字编辑器是 VI，如果你想用别的文字编辑器，则请先设定 VISUAL 环境变数来指定使用那个文字编辑器(比如说 setenv VISUAL joe)
-r [UserName]: 删除目前的时程表
-l [UserName]: 列出目前的时程表
-v [UserName]:列出用户cron作业的状态
```
# 查看系统运行的进程
若需要查看系统当前运行的所有进程，就需要用如下命令：
``` 
ps auxw 
```
其中参数a表示显示系统中所有用户的的进程；u表示输出进程用户所属信息； x表示也
显示没有控制台的进程；若显示行太长而被截断则可以使用f参数；

# 系统监听的服务
```
netstat -ln
```
l表示显示当前系统监听的端口信息；n表示端口按照端口号来显示，而不转换为
service文件中定义的端口名；若希望了解各个端口都是由哪些进程监听则可以使用p参数。
若发现不需要的服务， 可以使用linuxconf或ntsysv命令来关闭这些服务在系统启动时自
启动，然后重新启动系统则这些服务将在运行。
有些服务是由inetd超级服务器来监控的，则需要标记/etc/inetd.conf来关闭这些服务。

# 关机重启

```
shutdown命令的部分参数如下：
[-t] 指定在多长时间之后关闭系统
[-r] 重启系统
[-k] 并不真正关机，只是给每个登录用户发送警告信号
[-h] 关闭系统（halt）
```

- halt
```
halt是最简单的关机命令，其实际上是调用shutdown -h命令。halt执行时，杀死应用进程，文件系统写操作完成后就会停止内核。
halt命令的部分参数如下：
[-f] 没有调用shutdown而强制关机或重启
[-i] 关机或重新启动之前，关掉所有的网络接口
[-p] 关机时调用poweroff，此选项为缺省选项
```
- reboot
```
reboot的工作过程与halt类似，其作用是重新启动，而halt是关机。其参数也与halt类似。
```
- init
```
init是所有进程的祖先，其进程号始终为1。init用于切换系统的运行级别，切换的工作是立即完成的。init 0命令用于立即将系统运行级别切换为0，即关机；init 6命令用于将系统运行级别切换为6，即重新启动。
```

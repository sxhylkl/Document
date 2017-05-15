# 虚拟机搭建 - Centos7环境配置

> * [VirtualBox虚拟机](https://www.virtualbox.org/wiki/Downloads)
> * [Centos7系统镜像](http://mirrors.btte.net/centos/7/isos/x86_64/)
> * [Centos7静态IP配置](http://blog.csdn.net/aman1111/article/details/48224585)
> * [Centos7防火墙firewalld](http://www.excelib.com/article/287/show/)

## 一、 虚拟机搭建

1. 下载虚拟机和系统镜像(wget)
2. 安装Centos7
- 2.1 设置 -> 存储 -> 控制器：IDE -> 添加Centos7镜像
- 2.2 设置 -> 网络 -> 桥接网卡
- 2.3 启动 -> 配置分区 -> root用户，普通用户
- 2.4 检查网络，例：ping www.baidu.com
```
如果ping不通，检查/etc/sysconfig/network-scripts/ifcfg-enp2s0文件ONBOOT是否为yes
ONBOOT="yes"    # 指明在系统启动时是否激活网卡，只有在激活状态的网卡才能进行网络通讯
```

## 二、 Centos7配置
### 基本环境安装

> * pip安装：easy_install pip
> * 下列包的安装：yum -y install 包名

- wget 
- vim 
- rsync 
- ncurses-devel 
- openssl-devel
- sudo 
- bzip2-devel 
- zlib-devel 
- curl 
- gcc-c++
- make 
- cmake 
- swig 
- patch 
- bison-devel
- sqlite-devel 
- libselinux-python 
- readline 
- readline-devel 
- nload
- ntp 
- ntpdate 
- libjpeg-devel 
- python-setuptools 
- net-tools
- telnet 
- firewalld
- psmisc

### 系统配置

> 静态 IP、主机名、hosts 文件

> - 静态 IP 地址（又称固定IP地址）是长期分配给一台计算机或网络设备使用的 IP 地址
> - 动态IP地址(Dynamic IP)指的是在需要的时候才进行IP地址分配的方式（随机分配一个IP地址）

- 配置静态IP
```sh
$ vi /etc/sysconfig/network-scripts/ifcfg-enp2s0
ONBOOT=yes    # 指明在系统启动时是否激活网卡，只有在激活状态的网卡才能进行网络通讯
BOOTPROTO=static      # static表示静态IP，dhcp表示动态IP
IPADDR=IP地址    # IPADDR为网卡地址
GATAWAY=网关地址     # GATEWAY为网关地址，实际的路由器的地址
DNS1=114.114.114.114    # DNS域名解析，DNS1和DNS2这2个至少要填DNS1
DNS2=8.8.8.8
NETMASK=255.255.255.0   # 配置子网掩码
NM_CONTROLLED=no        # 使网卡配置生效时不用重启NetworkManager，直接重启network即可
# ---------------------------------------------
# 配置主机名
$ cat /etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6

IP地址 主机名
# ---------------------------------------------
# 配置hostname
$ hostname master
$ hostname
master
# ---------------------------------------------
# 配置resolv.conf 
$ vim /etc/resolv.conf
nameserver 114.114.114.114
nameserver 8.8.8.8
# 说明
# resolv.conf 是配置DNS域名解析的配置文件
# nameserver　表明DNS服务器的IP地址。可以有很多行的nameserver，每一个带一个IP地址。在查询时就按nameserver在本文件中的顺序进行
# ---------------------------------------------
# 配置默认网关
# 调试：ping IP地址 , ping www.baidu.com
# ===========永久添加方法===========
$ chmod +x /etc/rc.d/rc.local
$  vim /etc/rc.d/rc.local
$  route add default gw 网关地址
# ===========临时添加方法===========
$  route add default gw 网关地址            # 添加默认网关
$  route del default                       # 删除
```

- 基本操作
```sh
service iptables stop               # centos 6 关闭防火墙
systemctl stop firewalld.service    # centos 7 关闭防火墙
service network restart             # 重启网络
```

## 时区配置
检查当前的时区是否是需要的本地时区，通常： Asia/Shanghai - CST - 为北京东八区的时区
```sh
$ date +%Z
$ date -R
# 将当前时区设置为北京时区，其他时区，根据具体情况设置，或者使用 tzselect 工具
$ cp -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
# 同步时间(以下使用国内服务器，海外服务器，选择其他合适的时间服务器)：
$ ntpdate cn.pool.ntp.org
```

## 创建管理用的 admin 系统账号并添加公钥
```sh
$ useradd admin
$ mkdir /home/admin/.ssh
$ chown admin:admin /home/admin/.ssh/
$ chmod 0700 /home/admin/.ssh/
# 然后，在 .ssh 目录中构建 authorized_keys 文件，将公司指定人员的公钥加入进去，设置好 authorized_keys 文件的所有者和属性，操作如下：
$ echo "xxxxxxx(公钥内容)" > /home/admin/.ssh/authorized_keys
$ chown admin:admin /home/admin/.ssh/authorized_keys
$ chmod 0600 /home/admin/.ssh/authorized_keys
# 赋予 admin 用户 sudo 的权限：
$ echo "admin ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
# 以上操作完成，即可退出 root 账号，使用 admin 账号登录（使用以上 authorized_keys 中的公钥所对应的私钥进行验证），继续后续的操作。
# 创建数据目录（某些服务器可能已经建立并挂载了数据盘到该目录）：
$ chown admin:admin /data
```


## 安装包说明

> -devel：开发包,里面包含编译软件需要的库

```
1. bzip2 是一个基于Burrows-Wheeler 变换的无损压缩软件，是一款免费软件，能够把普通的数据文件压缩10%至15%，压缩的速度和解压的效率都非常高！支持大多数压缩格式，包括tar、gzip 等等
2. sudo是linux系统管理指令，是允许系统管理员让普通用户执行一些或者全部的root命令的一个工具
3. zlib是提供数据压缩用的函式库，由Jean-loup Gailly与Mark Adler所开发
4. wget是一个从网络上自动下载文件的自由工具，支持通过HTTP、HTTPS、FTP三个最常见的TCP/IP协议下载，并可以使用HTTP代理。wget名称的由来是“World Wide Web”与“get”的结合
5. curl是利用URL语法在命令行方式下工作的开源文件传输工具,curl http://curl.haxx.se,这是最简单的使用方法。用这个命令获得了http://curl.haxx.se指向的页面，同样，如果这里的URL指向的是一个文件或者一幅图都可以直接下载到本地
6. GNU编译器套件（GNU Compiler Collection）包括C、C++、Objective-C、Fortran、Java、Ada和Go语言的前端，也包括了这些语言的库（如libstdc++、libgcj等等）。
7. CMake是一个跨平台的安装（编译）工具，可以用简单的语句来描述所有平台的安装(编译过程)
8. SWIG 是一个非常优秀的开源工具，支持您将 C/C++ 代码与任何主流脚本语言相集成
9. Patch多指补丁的意思比如内存补丁、文件补丁等， 也是电脑命令程序的一种。
10. ncurses，计算机语言，指的是提供字符终端处理库
11. OpenSSL 是一个安全套接字层密码库，囊括主要的密码算法、常用的密钥和证书封装管理功能及SSL协议，并提供丰富的应用程序供测试或其它目的使用
12. GNU bison 是属于 GNU 项目的一个语法分析器生成器。Bison 把一个关于“向前查看 从左到右 最右”(LALR) 上下文无关文法的描述转化成可以分析该文法的 C 或 C++ 程序。它也可以为二义文法生成 “通用的 从左到右 最右” (GLR)语法分析器
13. SQLite，是一款轻型的数据库，是遵守ACID的关系型数据库管理系统，它包含在一个相对小的C库中
14. libselinux1 提供了一个可以被 SELinux 应用程序查看或设置进程和文件的安全性上下文以及获取安全策略决策的 API。
15. GNU readline是一个开源的跨平台程序库，提供了交互式的文本编辑功能。
16. nload它是一个实时监控网络流量和带宽使用的控制台应用程序.
17. NTP是网络时间协议(Network Time Protocol)，它是用来同步网络中各个计算机的时间的协议。
18. libjpeg是一个完全用C语言编写的库，包含了被广泛使用的JPEG解码、JPEG编码和其他的JPEG功能的实现.
19. python下的setuptools带有一个easy_install的工具，在安装python的每三方模块、工具时很有用，也很方便，安装setuptools前先安装pip，
20. 《Net Tools》是迄今为止集成工具最多的免费优化软件之一，分为网络、文件和系统三大类共计170余款工具
21. Telnet协议是TCP/IP协议族中的一员，是Internet远程登陆服务的标准协议和主要方式。
22. Centos7中默认将原来的防火墙iptables升级为了firewalld，firewalld自身并不具备防火墙的功能，而是和iptables一样需要通过内核的netfilter来实现，也就是说firewalld和iptables一样，他们的作用都是用于维护规则，而真正使用规则干活的是内核的netfilter，只不过firewalld和iptables的结构以及使用方法不一样罢了。
23. Psmisc软件包包含三个帮助管理/proc目录的程序。安装下列程序: fuser, killall,pstree和pstree.x11(到pstree的链接)
```
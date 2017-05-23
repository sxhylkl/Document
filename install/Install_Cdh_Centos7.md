# CDH搭建 - Centos7

> * [cloudera官方文档](https://www.cloudera.com/documentation/enterprise/latest/topics/quickstart.html)
> * [Hive官网](https://cwiki.apache.org/confluence/display/Hive/Home)
> * [Hive官网-入门](https://cwiki.apache.org/confluence/display/Hive/GettingStarted)
> * [Hive官网-教程](https://cwiki.apache.org/confluence/display/Hive/Tutorial#Tutorial-GettingStarted)
> * [Hadoop教程和示例](https://github.com/romainr/hadoop-tutorials-examples)
> * [HUE参考文档](https://github.com/cloudera/hue)
> * [HUE文档](http://gethue.com/automatic-high-availability-with-hue-and-cloudera-manager/)
> * [CDH搭建-参考文档1](http://blog.csdn.net/wzy0623/article/details/51768968)
> * [CDH搭建-参考文档2](http://blog.csdn.net/shenliang1985/article/details/50460828)
> * [CDH安装失败后重装](http://www.cnblogs.com/ivictor/p/4846358.html)
> * [Hadoop-shell命令](https://hadoop.apache.org/docs/r1.0.4/cn/hdfs_shell.html)
> * [hive学习笔记](http://blog.csdn.net/column/details/hive-home.html?&page=2)
> * [Hive-JSON-Serde工具](https://github.com/rcongiu/Hive-JSON-Serde)
> * [Hive-Join操作](http://www.cnblogs.com/ggjucheng/archive/2013/01/15/2860723.html)

------
## 1.安装Centos7并配置环境

> 参考文档 -> 虚拟机搭建 - Centos7环境配置 文档

- 硬件配置（内存：8G，硬盘：1T）
- 检查网络
- 基本环境安装
- 配置静态IP（静态 IP、主机名、hosts 文件）

### 2.下载文件
> * [下载cloudera-manager.repo](https://archive.cloudera.com/cm5/redhat/7/x86_64/cm/)
> * [下载manifest.json，CDH-5.10.0-1.cdh5.10.0.p0.41-el7.parcel，CDH-5.10.0-1.cdh5.10.0.p0.41-el7.parcel.sha1](https://archive.cloudera.com/cdh5/parcels/5.10/)
> * [下载oracle官方jdk的RPM包(jdk-8u112-linux-x64.rpm)](http://www.oracle.com/technetwork/java/javase/downloads/java-archive-javase8-2177648.html)
> * [下载cm5.10.0-centos7.tar.gz](http://archive.cloudera.com/cm5/repo-as-tarball/5.10.0/)
> * [下载mysql-jdbc](https://dev.mysql.com/downloads/file/?id=465643)

```sh
# 下载命令，例如：
$ wget -O /etc/yum.repos.d/cloudera-manager.repo https://archive.cloudera.com/cm5/redhat/7/x86_64/cm/cloudera-manager.repo
```

### 3.安装JDK
```sh
$ yum -y install jdk-8u112-linux-x64.rpm
# 配置环境变量
$ export JAVA_HOME=/usr/java/jdk1.8.0_112
$ export JAVA_LIB=$JAVA_HOME/lib
$ JAVA_BIN=$JAVA_HOME/bin
$ export PATH=$JAVA_BIN:$PATH
$ source ~/.bashrc <使jdk环境变量生效>
$ java -version <查看当前JDK版本>
# =============== 查看命令 ================
$ java -version   # 查看Java的版本
$ env             # 查看当前系统的所有环境变量
$ echo $JAVA_HOME # 查看当前系统指定的环境变量
```

### 4. 安装数据库

> 安装数据库 字符集配置，添加用户，设置权限
> 参考文档 -> MariaDB安装及字符集配置

```sh
# 安装
$ yum -y install mariadb mariadb-server mariadb-devel
# 基本配置
$ systemctl start mariadb         # 启动mariadb
$ systemctl enable mariadb        # 设置开机启动
$ mysql_secure_installation       # 配置mariadb
# 建立元数据库
mysql> create database cloudera_manager;   # 主节点server数据库
mysql> create database hive;               # Hive服务数据库
mysql> create database rman;   
mysql> create database oozie;              # Oozie服务数据库
mysql> grant all on *.* to '用户名'@'%' identified by '密码';   # 授权
```

### 5. 安装cm

```sh
$ tar -zxf cm5.10.0-centos7.tar.gz
$ mv cm /opt/
$ cd /data/centos7/yum/cm/5/RPMS/x86_64
$ yum -y install cloudera-manager-daemons-5.10.0-1.cm5100.p0.85.el7.x86_64.rpm
$ yum -y install cloudera-manager-server-5.10.0-1.cm5100.p0.85.el7.x86_64.rpm
$ yum -y install cloudera-manager-agent-5.10.0-1.cm5100.p0.85.el7.x86_64.rpm
```

### 6. 安装JDBC驱动

```sh
$ tar -xzvf mysql-connector-java-5.1.40.tar
$ mkdir -p /usr/share/java/
$ cp mysql-connector-java-5.1.40-bin.jar /usr/share/java/mysql-connector-java.jar
```

### 7. 其他配置

```sh
# 将percal文件放到对应的位置
$ mv CDH-5.10.0-1.cdh5.10.0.p0.41-el7.parcel /opt/cloudera/parcel-repo/
$ mv CDH-5.10.0-1.cdh5.10.0.p0.41-el7.parcel.sha1 /opt/cloudera/parcel-repo/
$ mv manifest.json /opt/cloudera/parcel-repo/
# 注：.sha1文件需改为.sha
# =======================================================
# 修改cloudera-scm-agent/config.ini，将主机名修改为跟当前主机名一样
$ vim /etc/cloudera-scm-agent/config.ini
server_host=master
use_tls=1
# =======================================================
# 建cm用户
# 查看当前是否存在cloudera-scm用户，如果不存在，则新加一个用户
$ cat /etc/passwd
$ cat /etc/group
$ useradd --system --home=/opt/cm/run/cloudera-scm-server --no-create-home --shell=/bin/false --comment "Cloudera SCM User" cloudera-scm
$ usermod -a -G root cloudera-scm
$ echo USER=\"cloudera-scm\" >> /etc/default/cloudera-scm-agent
$ echo "Default secure_path = /sbin:/bin:/usr/sbin/:/user/bin" >> /etc/sudoers
$ chown -R cloudera-scm:cloudera-scm /opt/cloudera/
$ chown -R cloudera-scm:cloudera-scm /opt/cm/
$ mkdir -p /opt/cloudera/parcels
$ chown cloudera-scm:cloudera-scm /opt/cloudera/parcels
$ /etc/init.d/cloudera-scm-server start
$ /etc/init.d/cloudera-scm-agent start
# =======================================================
# 执行初始化脚本：（安装完成 Cloudera Manager Server 软件包后才有）
/usr/share/cmf/schema/scm_prepare_database.sh mysql cloudera_manager root kaiqigu1
```

### 8. 启动server和agent
```sh
# 启动命令
$ systemctl start cloudera-scm-server
$ systemctl start cloudera-scm-agent
# 重启命令
$ systemctl restart cloudera-scm-server
$ systemctl restart cloudera-scm-agent
# 注：如果启动失败，可查看是否因为缺少mysql-jdbc，如果是，可将mysql-jdbc包放到对应位置改为指定的名称即可
# 执行完成后，稍等一会(原因Java的JDK启动较慢)，查看 7180 端口是否起来，如果端口启动成功，则查看下面网址：http://IP地址:7180/
```

### 9. 安装CDH

进入网址后，按步骤安装即可


### 10. 安装hdfs
```sh
# 用于和hadoop的hdfs进行交互
$ pip install hdfs
```


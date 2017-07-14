# MySQL - Centos7安装

[brew安装MySQL](http://www.cnblogs.com/xueweihan/p/5143066.html)

## 一、通过官网下载安装MySQL
```sh
# wget http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm
# rpm -ivh mysql-community-release-el7-5.noarch.rpm
# yum install mysql-community-server
# service mysqld restart        # 重启mysql服务
# service mysqld status         # 查看MySQL的运行状态
```
安装完成后，配置字符集，重启MySQL，初次启动MySQL时root无密码，可通过```mysql```或者```mysql -uroot```启动
```sql
set password for root@localhost =password('密码');   # 设置密码
```



## 二、安装mariadb

安装MySQL的常用安装方法，但是在Centos7中mysql-server安装失败，原因：CentOS7版本将MySQL用mariadb代替了
```sh
# yum install mysql
# yum install mysql-server
# yum install mysql-devel
```
安装mariadb，并配置字符集
```sh
# yum install mariadb-server mariadb 
# systemctl start mariadb       # 启动MariaDB
# systemctl stop mariadb        # 停止MariaDB
# systemctl restart mariadb     # 重启MariaDB
# systemctl enable mariadb      # 设置开机启动
# systemctl start mariadb       # 所以先启动数据库
```
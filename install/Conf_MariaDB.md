# MariaDB安装及字符集配置

> MariaDB数据库管理系统是MySQL的一个分支

## 安装
```sh
# 安装
$ yum -y install mariadb mariadb-server mariadb-devel
# 基本配置
$ systemctl start mariadb         # 启动mariadb
$ systemctl enable mariadb        # 设置开机启动
$ mysql_secure_installation       # 配置mariadb
mysql> grant all on *.* to '用户名'@'%' identified by '密码';   # 授权
```

## 字符集配置
```sh
$ vim /etc/my.cnf
# 在[mysqld]标签下添加
init_connect='SET collation_connection = utf8_unicode_ci'
init_connect='SET NAMES utf8'
character-set-server=utf8
collation-server=utf8_unicode_ci
skip-character-set-client-handshake
# =======================================================
$ vim /etc/my.cnf.d/client.cnf
# 在[client]中添加
default-character-set=utf8
=======================================================
$ vim /etc/my.cnf.d/mysql-clients.cnf
# 在[mysql]中添加
default-character-set=utf8
# =======================================================
# 全部配置完成，重启mariadb
$ systemctl restart mariadb
# 进入MariaDB查看字符集
mysql> show variables like "%character%";show variables like "%collation%";
注：skip-character-set-client-handshake是忽略客户端的字符集，使用服务器的设置；这样就使得接口也是UTF8
```


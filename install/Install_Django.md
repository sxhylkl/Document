# Django安装

> * [官方文档](https://www.djangoproject.com)
> * [Nginx配置参考文档](http://www.nginx.cn/115.html)

## Django支持的python版本

| Django version |	Python versions|
| ----  | ---- |
| 1.8   |	2.7, 3.2 (until the end of 2016), 3.3, 3.4, 3.5 |
| 1.9   |   1.10	2.7, 3.4, 3.5 |
| 1.11  |	2.7, 3.4, 3.5, 3.6 |
| 2.0   |   3.5+ |

## nginx 安装配置

```sh
$ vim /etc/yum.repos.d/nginx.repo
[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/centos/7/$basearch/
gpgcheck=0
enabled=1
$ yum -y install nginx
# nginx配置
$ vim /etc/nginx/conf.d/nginx.conf
server {
    	listen       端口号;
    	server_name  IP;

    	#charset koi8-r;

    	access_log  项目路径/logs/data.access.log  main;
    	error_log   项目路径/logs/data.error.log;

    	location /static/ {
        	root   项目路径;
        	index  index.html index.htm;
    	}

    	location /项目名/ {
        	rewrite "^/项目名/(.*)$" /$1 last;
    	}

    	location / {
        	uwsgi_pass 127.0.0.1:uwsgi端口号;
                include uwsgi_params;
    	}

    	location /admin/ {
        	uwsgi_pass 127.0.0.1:uwsgi端口号;
        	include uwsgi_params;
    	}
}
```

## 安装 uwsgi MariaDB Django

```sh
# 安装uwsgi
$ pip install uwsgi
$ find / -name 'uwsgi'
==========================================================
# 项目中uwsgi.ini的配置
plugins = python
py-autoreload = 2
==========================================================
# 安装MariaDB并配置字符集(见MariaDB字符集配置文档)
$ yum -y install mariadb mariadb-server mariadb-devel
==========================================================
安装1.8.7版本的Django和python包
$ pip install Django==1.8.7
$ pip install Pillow
$ pip install MySQL-python
$ pip install django-advanced-filters
$ pip install django-easy-select2
$ pip install sqlalchemy
$ pip install pandas
$ pip install pymysql
# django版本查询
$ django-admin --version
==========================================================
# 启动服务
$ systemctl enable nginx
$ systemctl start nginx
$ systemctl restart nginx
$ /usr/bin/uwsgi /项目路径/apps/uwsgi.ini
$ sudo /usr/share/nginx/sbin/nginx      # 重新运行一下 
$ sudo /usr/share/nginx/sbin/nginx -s reload  # 重启nginx
```

## 常用命令

```sh
$ python manage.py
$ python manage.py collectstatic    # 生成django管理页面的样式
$ python manage.py createsuperuser  # 创建超级用户
$ mkdir common/migrations
$ cd common/migrations/
$ touch common/migrations/__init__.py
$ python manage.py makemigrations   # 记录所有的关于modes.py的改动
$ python manage.py migrate          # 将该改动作用到数据库文件，比如产生table之类

$ pip list                          # 查询当前系统安装包版本
$ service mysqld start              # 启动mysql
$ /etc/init.d/nginx restart         # 重启Nginx
$ /usr/local/bin/uwsgi --reload /项目路径/logs/uwsgi-master.pid   # 重启uwsgi
$ /usr/local/bin/uwsgi /项目路径/apps/uwsgi.ini     # 启动uwsgi

$ netstat -lnptu                    # 查看端口
$ pstree -p                         # 查看进程
$ kill -9 进程号                     # 结束指定进程

$ /etc/sysconfig/iptables     # iptables 所在目录 
$ service iptables status     # 查看iptables状态
$ service iptables restart    # iptables服务重启
$ service iptables stop       # iptables服务禁用
$ getenforce   # 这个命令可以查看到selinux的状态，当前可以看到是关闭状态的

# sql数据导入和授权
mysql> mysql -uroot -p'密码' 数据库 < 文件.sql
mysql> grant all on 数据库名.* to 数据库@'IP地址' identified by '密码';
```
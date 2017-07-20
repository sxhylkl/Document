# 部署Django

- [uwsgi官方文档](https://uwsgi-docs.readthedocs.io/en/latest/)

## 一、创建项目
```sh
$ django-admin.py startproject test_pro     # 创建项目
$ chmod +x django-admin.py      # 如果权限拒绝，运行此命令
$ django-admin startapp app1    # 创建应用
$ python manage.py runserver    # 启动服务，默认访问127.0.0.1:8000/url/
# 项目存放位置最好是根目录(root)之外的位置，因为放到根目录有使人通过网络看到源代码的风险
```
uwsgi.ini
```
# plugins = python
py-autoreload = 2
```


## python的两种安装组件的方法(通常两种都需要安装)
- easy_install ：出现较早
- pip ：pip是easy_install的改进版，提供了更好的提示信息

## WEB服务器
web服务器是连接用户浏览器与python服务端程序的中间节点，目前主流的web服务器包括：Nginx、Apache、Lighthttpd、IIS等

WSGI：全称 Web Server Gateway Interface，wsgi是将python服务端程序连接到web服务器的通用协议，uwsgi和apache的mod_wsgi都是独立的wsgi程序。wsgi用于为python语言定义web服务器和服务器端程序的通用接口规范。

WSGI的接口分为两个：
- 与web服务器的接口
- 与服务器端程序的接口


## Nginx
> - Nginx是由俄罗斯工程师开发的一个高性能HTTP和反向代理服务器
> - 优点：运行稳定、配置简单、资源消耗低

Nginx的相关文件路径：
```sh
/etc/nginx/nginx.conf           # 全局配置文件
/var/log/nginx/access.log-日期   # 访问日志文件
/var/log/nginx/error.log-日期    # 错误日志文件
```
Nginx配置文件
```sh
$ vim /etc/nginx/nginx.conf
user  nginx;                # 定义运行Nginx的用户
worker_processes  1;        # Nginx的进行数，应设置与系统CPU数量相等的数值

error_log  /var/log/nginx/error.log warn;   # 错误日志文件路径
pid        /var/run/nginx.pid;              # 

events {
    worker_connections  1024;               # 每个Nginx进行允许的最大客户端连接数
}

http {
    include       /etc/nginx/mime.types;        # 
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;    # 访问日志文件路径名
    sendfile        on;             # 是否允许文件上传
    #tcp_nopush     on;             # 防止网络阻塞
    keepalive_timeout  65;          # 允许客户端长连接最大秒数
    #gzip  on;

    server {
    	listen       9090;              # 配置站点监听的端口
    	server_name  IP地址;             # 站点监听的IP地址，可设置问localhost或者真实的IP地址
    	#charset koi8-r;

    	access_log  /data/项目名/logs/data.access.log  main;
    	error_log   /data/项目名/logs/data.error.log;

        # location用于配置URL的转发接口
    	location /static/ {
        	root   /data/项目名;
        	index  index.html index.htm;
    	}

    	location /项目名/ {
        	rewrite "^/项目名/(.*)$" /$1 last;
    	}

    	location / {
        	uwsgi_pass 127.0.0.1:8078;
                include uwsgi_params;
    	}

    	location /admin/ {
        	uwsgi_pass 127.0.0.1:8078;
        	include uwsgi_params;
    	}
    }

    include /etc/nginx/conf.d/*.conf;

}
```

## uWSGI
安装
```sh
pip install uwsgi       # 安装
uwsgi  uwsgi.ini        # 启动uwsgi时，直接指定uwsgi.ini即可
```
编辑uWSGI.ini文件
```sh
[uwsgi]
socket = 127.0.0.1:8078     # 以WSGI的socket方式运行，并指定链接地址和端口    
master = true
processes = 4               # 指定服务器端程序的进程数

basedir = /data/项目名       # 
chdir = %(basedir)          # 指定uWSGI启动后的当前目录
wsgi-file = common/wsgi.py  # 指定服务器端的程序名

uid = root                  # 指定用户隐形uWSGI的Linux用户ID
gid = root

pidfile = %(basedir)/logs/uwsgi-master.pid
daemonize = %(basedir)/logs/uwsgi-daemonize.log

# plugins = python
py-autoreload = 2
```
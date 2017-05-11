# 搭建本地Yum源

暂不可用，未搭建成功，待搭建成功后修改补充
> [参考文档](http://blog.csdn.net/qq_25371579/article/details/54572953)

## 1.安装http服务
```
$ cd /data/soft 
$ wget http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm 
$ sudo yum install nginx-release-centos-7-0.el7.ngx.noarch.rpm
$ sudo yum install nginx
```

## 2. 安装createrepo软件包
```
$ sudo yum -y install createrepo
```

## 3. 创建存放软件包仓库目录

此步骤需在/data/centos7/yum/目录下已经存放yum源所需的rpm包后执行，或新添rpm包后再次执行以刷新yum源
```
$ mkdir -p /data/centos7/yum/
$ createrepo /data/centos7/yum/
```

## 4. nginx 配置

无特殊要求可不用变动
配置/etc/nginx/conf.d/yum.conf
```
$ cd /etc/nginx/conf.d/
$ sudo cp default.conf yum.conf
$ sudo mv default.conf default.conf.bak
$ vim yum.conf
server {  
    listen 80;  
    charset utf8; 
    server_name yum.yoursite.com;   

    location / {
    allow 192.168.2.179;
    deny all;
    root /data/centos6/yum;  
    index index.html; 
    }
}
# 查看nginx的安装目录
ps  -ef | grep nginx
# 重启nginx
$ /bin/systemctl restart nginx.service
$ sudo chkconfig nginx on
location内的添加allow和deny可以确保服务器不被其他机器使用，allow表示允许某个IP访问
```



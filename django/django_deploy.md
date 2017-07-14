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

## 二、关闭Debug模式
> 将DEBUG设置为False

settings.py文件中的DEBUG默认设置为True，表示DEBUG模式开启，此时会导致如下几个问题：
- 1.所有的数据库查询将被保存在内存中，以django.db.connection.queries的形式.会很吃内存。
- 2.任何404错误都将呈现Django的包含敏感信息的页面，而不是普通的404页面。
- 3.应用中任何未捕获的异常、错误的python语法、错误的模板语法等都会返回包含敏感信息的Django错误页面。

## 三、模型数据操作

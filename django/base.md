# Django
> Django 是用 Python 编写的一组类库,可以运行与任何Python可以运行的环境，Django诞生于新闻网站
> Django 代码向后兼容，例：1.1写的应用，适用于1.2、1.3等之后的版本，但不一定适用于2.0以后的版本

> * [Python安装包](https://www.python.org/downloads/)
> * [Django安装包](https://www.djangoproject.com/download/)
> * [mysql-python安装包](https://sourceforge.net/projects/mysql-python/)

## 一、MVC 设计模式
> MVC 是一种软件开发的方法，它把代码的定义和数据访问的方法（模型）与请求逻辑 （控制器）还有用户接口（视图）分开来
 
- mode.py : 模型，用Python类来描述数据表，可以通过简单的Python代码来创建、检索、更新、删除数据库的记录，不需要写SQL
- views.py : 视图，页面的业务逻辑，通过Python函数来实现
- urls.py : 控制器，指出不同的URL调用不同的视图
- xxx.html ：html模板，描述了页面的设计

## 二、Django安装
```sh
$ python -V   # 查新当前的Python版本，确保当前环境已经安装了Python
$ yum -y install python-setuptools  
$ easy_install pip
$ pip install django
```

## 三、创建第一个项目
创建项目
```sh
$ django-admin.py startproject test_pro     # 创建项目
$ chmod +x django-admin.py      # 如果权限拒绝，运行此命令
$ django-admin startapp app1    # 创建应用
$ python manage.py runserver    # 启动服务，默认访问127.0.0.1:8000/url/
# 项目存放位置最好是根目录(root)之外的位置，因为放到根目录有使人通过网络看到源代码的风险
```
配置视图(app.views.py)
```py
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World")
```
配置URL(pro.urls.py)
```py
from django.conf.urls import url
# from app.views import hello
from app import views

urlpatterns = [
    # url(r'^hello/$', hello),
    url(r'^hello/'$, views.hello_world),         # 称作URLpattern
    # url(r'^hello/\d{1,2}/$', views.hello_world),    
]
```

## 四、URL说明
> 松耦合：更新一个模块不会影响其他模块的改变
```py
from django.conf.urls import url
# from app.views import hello
from app import views

urlpatterns = [
    # url(r'^hello/', hello),
    url(r'^hello/', views.hello_world),         # 称作URLpattern
]
----说明----------------
1. URLpattern是一个Python的元组，元组中第一个元素是模式匹配字符串（正则表达式）；第二个元素是那个模式将使用的视图函数
2. Django在检查URL模式前，移除每一个申请的URL开头的斜杠(/)，这意味着为/hello/写URL模式不用包含斜杠(/)
```

## 五、settings文件说明
```py
# Django通过在ROOT_URLCONF配置来决定根URLconf
ROOT_URLCONF = 'pro.urls'
# LANGUAGE_CODE用于指定翻译语言,翻译语言文件存放位置：site-packages/django/conf/locale
# zh_Hans:中文简体，zh_Hant：中文繁体
LANGUAGE_CODE = 'zh-hans'
# 设置时区，北京常用'Asia/Shanghai'，也有用'PRC'的
TIME_ZONE = 'Asia/Shanghai'
```

## 六、Model中的Meta
> Meta是Django的一个内部类，用于定义Django模型层的元数据

主要用法
```py
sex_choices = (('f', 'famale'), ('m', 'male'),)

class User(models.Model):
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=1, choices=sex_choices)

    class Meta:
        verbose_name = u"用户信息表"
        verbose_name_plural = u"用户信息表"

    def __unicode__(self):
        return self.name

注：
verbose_name: 给模型类定义一个可读性的模型名称
verbose_name_plural: 指定模型类的复数形式，如不指定，Django会自动在模型名称后加一个s 
```




-----

## 说明一、Django支持的数据库
- [PostgreSQL](http://www.postgresql.org/)
- [SQLLite 3](http://www.sqlite.org/)
- [MySQL](http://www.mysql.com/)
- [Oracle](http://www.oracle.com/)

## 说明二、正则表达式
| 符号	    |  匹配    |
| ----	    |  ----    |
| . (dot)    | 	任意单一字符  |
| \d	    |   任意一位数字  |
| [A-Z]	    |   A 到 Z中任意一个字符（大写）    |
| [a-z]	    |   a 到 z中任意一个字符（小写）    | 
| [A-Za-z]	|   a 到 z中任意一个字符（不区分大小写）    |
| +	        |   匹配一个或更多 (例如, \d+ 匹配一个或 多个数字字符)  |
| [^/]+	    |   一个或多个不为‘/’的字符   |
| *	        |   零个或一个之前的表达式（例如：\d? 匹配零个或一个数字）|
| *	        |   匹配0个或更多 (例如, \d* 匹配0个 或更多数字字符)      |
| {1,3}	    |   介于一个和三个（包含）之前的表达式（例如，\d{1,3}匹配一个或两个或三个数字）   |

## 说明三
- Django 服务器在开启时默认运行在 debug 模式，Django 出错信息仅在 debug 模式下才会显现
# Django的简单说明

## CGI
CGI(Common Gateway Interface) 是外部应用程序（CGI程序）与WEB服务器之间的接口标准，是在CGI程序和Web服务器之间传递信息的过程。CGI规范允许Web服务器执行外部程序，并将它们的输出发送给Web浏览器，CGI将Web的一组简单的静态超媒体文档变成一个完整的新的交互式媒体。

### 处理步骤编辑
1. 通过Internet把用户请求送到web服务器
2. web服务器接收用户请求并交给CGI程序处理
3. CGI程序把处理结果传送给web服务器
4. web服务器把结果送回到用户

## MVC 设计模式

- models.py (the database tables)
> 主要用一个 Python 类来描述数据表。 称为 模型(model) 。 运用这个类，你可以通过简单的 Python 的代码来创建、检索、更新、删除 数据库中的记录而无需写一条又一条的SQL语句
```py
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateField()
```

- views.py (the business logic)
> 包含了页面的业务逻辑。 latest_books()函数叫做视图
```py
from django.shortcuts import render_to_response
from models import Book

# latest_books()函数叫做视图
def latest_books(request):
    book_list = Book.objects.order_by('-pub_date')[:10]
    return render_to_response('latest_books.html', {'book_list': book_list})
```

- urls.py (the URL configuration)
> 指出了什么样的 URL 调用什么的视图。 在这个例子中 /latest/ URL 将会调用 latest_books() 这个函数。 换句话说，如果你的域名是example.com，任何人浏览网址http://example.com/latest/将会调用latest_books()这个函数
```py
from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^latest/$', views.latest_books),
)
```

- latest_books.html (the template)
> html 模板，它描述了这个页面的设计是如何的。 使用带基本逻辑声明的模板语言，如{% for book in book_list %}
```html
<html><head><title>Books</title></head>
<body>
<h1>Books</h1>
<ul>
{% for book in book_list %}
<li>{{ book.name }}</li>
{% endfor %}
</ul>
</body></html>
```


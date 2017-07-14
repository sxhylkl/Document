# Django测试

## 一、模型数据操作

models.py
```py
from django.db import models
class Test(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        # 将对象以字符串形式返回
        return self.name
```

views.py
```py
from app.models import Test
def index(request):
    tes = Test.objects.all()
    return render_to_response('index.html', {'tes': tes})
```

数据存储操作
```sh
$ python manage.py shell
In [1]: from app.models import Test
# 存入数据 - 方法一
In [3]: t = Test()
In [5]: t.name = 'wang'
In [7]: t.save()
# 存入数据 - 方法二
In [8]: t = Test(name='Tom')
In [9]: t.save()
# 存入数据 - 方法三
In [12]: Test.objects.create(name='Li')
# 查询数据
In [15]: ts = Test.objects.all()
```

```py
In [1]: from app.models import Entry, blog
In [4]: entry1 = Entry.objects.create(name = 'aa')
In [5]: entry2 = Entry.objects.create(name='Max')
In [6]: entry3 = Entry.objects.create(name='carl')
In [9]: blog1 = blog.objects.create(name='aa',te=entry1)
In [11]: blog1.te_id
Out[11]: 1L
In [12]: blog1.te
Out[12]: <Entry: aa>
In [13]: entry1.id
Out[13]: 1L
In [14]: entry1.name
Out[14]: 'aa'
In [16]: entry1.blog_set.all()
Out[16]: <QuerySet [<blog: aa>]>
```
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


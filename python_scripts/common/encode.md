# Python编码

## 文件开头设置编码
```py
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
```

## 获取当前系统默认编码
```py
import sys
print sys.getdefaultencoding()
```

## 修改系统默认编码
```py
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
# 注：python加载时首先加载了site.py，其中由一段函数是删除了这个方法的（del sys.getdefaultencodingy），因此需要reload(sys),才能重新设置编码
```

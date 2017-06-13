# Python类型

- 所有类型都有一个共同祖先类型 object，它为所有类型提供原始模版，以及系统 所需的基本操作方式
- 所有类型对象都是 type 的实例

例如：
```py
$ isinstance(int, type)
True
$ isinstance(int, object)
True
$ issubclass(int, object)
True
$ issubclass(int, type)
False
$ issubclass(int, int)
True
$ isinstance(1, int)
True
# 注：isinstance用于判断对象是否是指定的类型，issubclass用于判断对象是否是子类
```
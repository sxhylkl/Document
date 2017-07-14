# mac安装MySQL-python遇到的坑

```sh
$ python manage.py runserver
django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: dlopen(//anaconda/lib/python2.7/site-packages/_mysql.so, 2): Library not loaded: libssl.1.0.0.dylib
  Referenced from: //anaconda/lib/python2.7/site-packages/_mysql.so
  Reason: image not found.
Did you install mysqlclient or MySQL-python?
```

解决方式：
```sh
pip install psycopg2
brew install --upgrade openssl
brew unlink openssl && brew link openssl --force
```
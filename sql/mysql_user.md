# MySQL用户创建及授权

## 创建用户与删除用户

创建用户
```sql
create user 用户名@host identified by 密码;
注：host可以是指定的登陆的主机IP或者本地的localhost，或者允许任意主机可以登陆的%
```
删除用户
```sql
drop user 用户名@主机名;
```


## 授权与撤销授权

授权
```sql
grant all pivileges on 数据库名.表名 to 用户名@主机名 identified by 密码;
# 注：all表示所有权限，也可单独指定select、insert等权限
```
撤销授权
```sql
revoke all pivileges on 数据库名.表名 to 用户名@主机名 identified by 密码;
# 注：all表示所有权限，也可单独指定select、insert等权限
```

## 设置或者更改用户密码
```sql
set password for 用户名@主机名 = password('新密码');
```

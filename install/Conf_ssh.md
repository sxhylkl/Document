# SSH KEY 配置

## 生成 SSH KEY
```sh
$ ssh-keygen -t rsa -C "Email"
Generating public/private rsa key pair.
# 输入保存密钥的文件
Enter file in which to save the key (/Users/.ssh/id_rsa): /Users/.ssh/自定义密钥文件名
# 输入密码（无密码为空）
Enter passphrase (empty for no passphrase):
# 再次输入相同的密码
Enter same passphrase again:
```

## 查看密钥
```sh
# 此处返回的内容可用于SSH KEY网站
$ cat ~/.ssh/公钥文件名.pub
ssh-rsa 公开密钥的内容 Email
```

## 配置多个 SSH KEY
```sh
# 在~/.ssh目录下创建 config 文件：
$ vim ~/.ssh/config
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/公钥文件名

...
# 将对应的公钥添加至对应的网站
```
# SSH KEY 配置
> [ssh-keygen参数说明](http://www.cnblogs.com/sunjf/p/ubutu_ssh.html)

## 一、生成 SSH KEY
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

## 二、查看密钥
```sh
# 此处返回的内容可用于SSH KEY网站
$ cat ~/.ssh/公钥文件名.pub
ssh-rsa 公开密钥的内容 Email
```

## 三、配置多个 SSH KEY
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

## 四、ssh-keygen的常用参数
> - ssh-keygen 用于生成、管理和转换认证密钥
> - ~/.ssh/known_hosts：会存储所有访问过的主机的密钥，可通过【ssh-keygen -R 机器IP地址】命令删除属于该主机的密钥

* -t type: 指定要生成的密钥类型，有rsa1(SSH1),dsa(SSH2),ecdsa(SSH2),rsa(SSH2)等类型，较为常用的是rsa类型
* -C comment: 提供一个新的注释
* -b bits: 指定要生成的密钥长度 (单位:bit)，对于RSA类型的密钥，最小长度768bits,默认长度为2048bits。DSA密钥必须是1024bits
* -f filename: 指定生成的密钥文件名字
* -R hostname: 从known_hosts 文件中删除所有属于 hostname 的密钥

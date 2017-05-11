# gitbook安装

在本地生成各类版本的文档电子书
> * [config参考文档](http://blog.csdn.net/guomutian911/article/details/45744885)
> * [gitbook官方文档](https://toolchain.gitbook.com)

- 搭建虚拟机并调通网络
- 安装基础包
```
$ yum -y install vim wget rsync
$ yum -y install gcc-c++
```

- 下载安装包
```sh
$ cd /data
$ wget http://nodejs.org/dist/v0.10.48/node-v0.10.48.tar.gz，
```

- 安装
```sh
$ tar -zxvf node-v0.10.48.tar.gz
$ ./configure --prefix=/usr/local/node/0.10.48
$ make
$ make install
```

- 环境变量配置
```sh
$ vim /etc/profile
# set for nodejs
export NODE_HOME=/usr/local/node/0.10.48
export PATH=$NODE_HOME/bin:$PATH
# :wq保存并退出，编译/etc/profile 使配置生效
$ source /etc/profile
# 验证是否安装配置成功
$ node -v
# npm模块安装路径
/usr/local/node/0.10.48/lib/node_modules/npm
```

- 安装gitbook
```sh
$ npm install -g gitbook-cli
# 查看gitbook是否安装成功
$ gitbook -V
```

- 生成gitbook项目
```sh
$ mkdir myGitBook
$ cd myGitBook/
$ gitbook init
# 当前目录下启动
$ gitbook serve .
# 非当前目录下启动
$ gitbook serve ./图书目录
```

- 备注
```
1. linux下，源码的安装一般由3个步骤组成：配置（configure）、编译（make）、安装（make install）
2. 不指定prefix，则可执行文件默认放在/usr /local/bin，库文件默认放在/usr/local/lib，配置文件默认放在/usr/local/etc。其它的资源文件放在/usr /local/share。
你要卸载这个程序，要么在原来的make目录下用一次make uninstall（前提是make文件指定过uninstall）,要么去上述目录里面把相关的文件一个个手工删掉。
3. ./configure是源代码安装的第一步，主要的作用是对即将安装的软件进行配置，检查当前的环境是否满足要安装软件的依赖关系，但并不是所有的tar包都是源代码的包
```

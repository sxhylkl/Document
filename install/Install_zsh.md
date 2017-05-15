# 安装oh my zsh

[参考文档](http://blog.csdn.net/yuqiongran/article/details/52280522)

## linux下安装git
```
$ yum install git
```

## linux下安装zsh
```sh
# 安装zsh
$ yum install zsh
# 获取并安装 oh my zsh，前提先安装好git
$ wget --no-check-certificate https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh
# 替换bash为zsh
chsh-s/bin/zsh
# 重启电脑
$ sudo reboot
```


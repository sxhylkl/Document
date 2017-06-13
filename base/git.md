# Git 入门指南

> * [Git - Book](https://git-scm.com/book/zh/v1)
> * [git - 简易指南](http://www.bootcss.com/p/git-guide/)
> * [Git分支管理策略](http://www.ruanyifeng.com/blog/2012/07/git.html)
> * [pull - fetch](https://stackoverflow.com/questions/292357/what-is-the-difference-between-git-pull-and-git-fetch)
> * [rebase - fetch - pull](https://stackoverflow.com/questions/14894768/in-git-how-is-fetch-different-than-pull-and-how-is-merge-different-than-rebase)
> * [pull - merge](https://stackoverflow.com/questions/17339091/difference-between-git-pull-master-vs-git-merge-master)
> * [Git教程 - 廖雪峰](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)
> * [15分钟交互式学习git](https://try.github.io/levels/1/challenges/19)
> * [Git暂存区](http://blog.csdn.net/agul_/article/details/7835786)
> * [git权威指南 - 读书笔记](http://hustlzp.com/post/2014/03/git-solo)
> * [gitignore配置](http://www.cnblogs.com/haiq/archive/2012/12/26/2833746.html)

## 一、GitHub中https和SSH的区别
- https
  - 可以随意克隆任何人github上的项目
  - push时需要验证用户名和密码
- SSH
  - 必须是要克隆项目的拥有者或管理员，并且需要先添加SSH key，否则无法克隆
  - push时不需要验证用户名和密码，如果配置SSH key时候设置了密码，则需要输入密码
  - github添加Deploy keys时，需选中Allow write access才能push，否则为只读模式

## 二、常用命令

- 获取帮助
```sh
$ man git           # 详细的git帮助
$ man git-commit    # 详细的git帮助
```

- 克隆远程代码库到本地
```sh
$ git clone git地址               # 克隆代码库到本地（默认主分支）
$ git clone -b 分支名 git地址      # git克隆指定分支的代码库
```

- 用户信息配置
```sh
# 配置用户名和Email，每次Git提交时都会引用，并将用户信息和更新内容一起存入历史记录
$ git config --global user.name '用户名'
$ git config --global user.email 'Email'
# 这个命令会在~/.gitconfig填入以下信息
$ cat ~/.gitconfig
[user]
  name = 用户名
  email = Email
```

- 检查工具
```sh
$ rm -rf .git             # 取消git init
$ git log                 # 查看历史记录
$ git log -p              # 查看历史记录，-p选项可以查看更详细的信息
$ git blame FileName      # 查看某个文件各行的最后提交者
$ git diff                # 查看当前工作区的改变
$ git diff FileName       # 查看具体某个文件的改变
```

- URL地址
```sh
$ git remote                              # 不带参数，列出已经存在的远程分支
$ git remote -v                           # 查看url地址
$ git remote set-url origin git地址        # 更改url地址
$ git remote rm origin                    # 删除URL地址
$ git remote add origin git地址            # 添加URL地址
```

- 文件操作
```sh
$ git status                  # 查询本地版本与版本库的对比情况
$ gst                         # 查询本地版本与版本库的对比情况(items中git status的简化)
$ git pull                    # 拉取远程分支到本地
$ git add FileName            # 添加单个文件
$ git add .                   # 添加所有文件
$ git rm FileName             # 删除单个文件
$ git add -A .      # 删除本地已经删除的所有文件,-A是--all的简写，且必须是大写的A
$ git add --all .   # 删除本地已经删除的所有文件,-A是--all的简写，且必须是大写的A
$ git checkout FileName       # 将文件还原为与版本库文件一致
$ gco FileName                # 将文件还原为与版本库文件一致(items中git checkout的简化)
$ git commit -m 'Explain'     # 版本提交 - 加提交备注
$ git push                    # 版本提交 - 将提交内容加入版本库
```

## 三、撤销或回滚到某个版本
### 1、没有push的情况
> 发生在本地代码库，用于add、commit后取消提交
```sh
# 查找想要回退到版本的哈希值
git log
# 回退
git reset [--soft | --mixed | --hard ] 回退到版本的哈希值
# 注：git reset --mixed 哈希值 等价于 git reset 哈希值
```
- mixed：保留源码，将commit信息和index信息会退到某个版本
- soft：保留源码，只将commit信息回退到某个版本，不回退index的信息
- hard：源码、commit信息、index信息都会会退到某个版本(注：改变的是本地代码仓库源码)

### 2、push后的情况
> 同时回滚线上代码和本地代码
```sh
# 查询需要回滚的版本的哈希值(注意：这里不是回滚到的版本的哈希值)
git log
# 回滚
git revert 哈希值
# 更新线上的版本
git push
```
注意：
- 如果已经push到线上的代码库，reset删除指定的commit以后，git push可能会导致很多冲突，revert不会导致冲突
- git reset 是直接删除指定的commit，head向后移动
- git revert 是用一次新的commit来回滚之前的commit，head向前移动
- 日后现有分支和历史分支需要合并时,reset 恢复部分的代码依然会出现在历史分支里.但是revert 方向提交的commit 并不会出现在历史分支里.
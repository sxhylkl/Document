# Git 入门指南

> * [gitignore配置](http://www.cnblogs.com/haiq/archive/2012/12/26/2833746.html)

## 获取帮助
- man git
示例：输入命令 man git-commit，出来的内容是详细的git帮助，常见类型如下：
```
  NAME            # 名字
  SYNOPSIS        # 参数
  DESCRIPTION     # 描述
  OPTIONS         # 选项
  DATE FORMATS
  EXAMPLES        # 示例，可做参考
  DISCUSSION
  SEE ALSO        # 相关命令
```
## 检查工具
- git log/git log -p: 提交历史，-p选项可以查看全面的信息
- git blame：查看某个文件各行的最后提交者

- git init 取消
```
# 切换到文件目录，删除文件
rm -rf .git 
```
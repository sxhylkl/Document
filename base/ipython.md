# Ipython说明

IPython 是一个 python 的交互式 shell，优点：数据执行记录，便于调试代码
> [参考文档](http://www.cnblogs.com/zzhzhao/p/5295476.html)

## 简单好用的函数
- %env显示环境变量
- %hist 或 %history显示历史记录
- %time statement计算一段代码的执行时间
- %bg function把 function 放到后台执行，例如: %bg myfunc(x, y,z=1)，之后可以用jobs将其结果取回。myvar = jobs.result(5) 或 myvar =jobs[5].result。另外，jobs.status() 可以查看现有任务的状态。
- %pwd显示当前目录
- %pycat filename用语法高亮显示一个 python 文件(不用加.py后缀名)
- 另外，ipython 中用 ! 表示执行 shell 命令，用 $ 将 python 的变量转化成shell 变量。通过这种两个符号，我们就可以做到和 shell命令之间的交互，可以非常方便地做许多复杂的工作。比如你可以很方便地创建一组目录:

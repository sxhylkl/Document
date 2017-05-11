# Linux正则表达式
sed编辑器、gawk程序
## 1. 正则表达式
### 1. 纯文本
正则表达式区分大小写，使用标准文本字符串过滤数据
+ 匹配字符
```
# 用标准文本字符串过滤数据
# sed编辑器、gawk程序用他们各自的print命令打印匹配该正则表达式的所有行
echo "this is Test"| sed -n '/test/p'   # 不成立，Test和test不一致，区分大小写
echo "this is Test"| sed -n '/Test/p'   # 成立
echo "the books" | sed -n '/book/p'     # 成立
echo "the book" | sed -n '/books/p'     # 不成立
echo "this number 1" | sed -n '/ber 1/p'    #成立
```
+ 匹配文本
```
[root@localhost test]# cat aa
this is aa
this  is aa
[root@localhost test]# sed -n '/  /p' aa    #成立，可匹配多个空格
this  is aa
```
### 2. 特殊字符
+ 特殊字符
```
# 正字表达式识别的特殊字符
.*[]^{}\+?|()
# 转义字符:反斜线(\),用于特定字符的使用
```
+ 用法
```
[root@localhost test]# cat bb
this $4.00
[root@localhost test]# sed -n '/\$/p' bb
this $4.00
```
+ 注意(斜线(/)的使用)
```
# 尽管斜线不是特殊字符，但也需转义，否则会报错
[root@localhost test]# echo "3 / 2" | sed -n '/\//p'
3 / 2
```
### 3. 锚字符
+ 锁定在行首（脱字符：^）
```
[root@localhost test]# echo "this is aa" | sed -n '/^this/p'
this is aa
[root@localhost test]# echo "this is aa" | sed -n '/^is/p'
```
+ 锁定在行尾（美元符：$）
```
[root@localhost test]# echo "this is aa" | sed -n '/aa$/p'
this is aa
[root@localhost test]# echo "this is aa" | sed -n '/is$/p'
```
+ 组合锚点(行首行尾一起使用)
```
# 特殊用法：过滤文本中的空白行
# 说明：sed编辑器用d命令删除匹配正则表达式的行
[root@localhost test]# cat bb
aa
bb
dd


ff
[root@localhost test]# sed '/^$/d' bb
aa
bb
dd
ff
```
### 4. 点字符(.)
```
# 点字符的位置的位置必须匹配一个字符，如果在.的位置没有字符，则模式不成立
# (即匹配的字符不能在行首，注：空格会被当做字符)
[root@localhost test]# echo "this cat" |sed -n '/.at/p'
this cat
[root@localhost test]# echo "at a" |sed -n '/.at/p'
[root@localhost test]# echo " at" |sed -n '/.at/p'
 at
```
### 5. 字符组(方括号,包含指定字符)
```
# 方括号中包含想要在该组中包含的任何字符
[root@localhost test]# echo "yes" | sed -n '/[Yy]es/p'
yes
[root@localhost test]# echo "Yes" | sed -n '/[Yy]es/p'
Yes
[root@localhost test]# echo "YEs" | sed -n '/[Yy][Ee]s/p'
YEs
[root@localhost test]# echo "452" | sed -n '/[123456789]/p'
452
```
```
# 限定指定位数的字符串
[root@localhost test]# echo "abdca" | sed -n '/[abcd][abcd][abcd][abcd]/p'
abdca
[root@localhost test]# echo "abdca" | sed -n '/^[abcd][abcd][abcd][abcd]$/p'
[root@localhost test]# echo "abdc" | sed -n '/^[abcd][abcd][abcd][abcd]$/p'
abdc
```
### 6. 排除字符
```
# 在字符组开头加个脱字符(^),用于寻找组中没有的任意字符
sed -n '/[^ch]at/p' data6
# 注：没理解
```
### 7. 使用区间
```
[root@localhost test]# echo "123" | sed -n '/[0-9]/p'
123
[root@localhost test]# echo "acc" | sed -n '/[a-z]/p'
acc
[root@localhost test]# echo "ac" | sed -n '/[a-z][h-m]/p'
# a~c,h~m中的字母必须出现在at之前，并且这区间不允许出现d~g之间的字母
[root@localhost test]# echo "the cat" |sed -n '/[a-ch-m]at/p'
the cat
[root@localhost test]# echo "the eat" |sed -n '/[a-ch-m]at/p'
```
### 8. 特殊字符组
```
[[:alpha:]]     # 匹配任意字母，不区分大小写
[[:alnum:]]     # 匹配任意字母数字字符0-9、a-z、A-Z
[[:blank:]]     # 匹配空格或制表符
[[:digit:]]     # 匹配数字
[[:lower:]]     # 匹配小写字母a-z
[[:print:]]     # 匹配任意可打印字符
[[:punct:]]     # 匹配标点符号
[[:space:]]     # 匹配任意空白字符：空格、制表符、NL、FF、VT、CR
[[:upper:]]     # 匹配任意大写字母字符A-Z
[root@localhost test]# echo "aSd" | sed -n '/[[:alpha:]]/p'
aSd
```
### 9. 星号
```
# 星号前面的字符可以出现0次或多次
[root@localhost test]# echo 'color' |sed -n '/colou*r/p'
color
[root@localhost test]# echo 'colour' |sed -n '/colou*r/p'
colour
```
## 2. 扩展正则表达式
### 1. 问号
```
# 问号前面的字符可以出现0次或1次
[root@localhost test]# echo "beet" | gawk '/be?t/{print $0}'
[root@localhost test]# echo "bet" | gawk '/be?t/{print $0}'
bet
```
### 2. 加号
```
# 加号前面的字符可以出现1次或多次
```
### 3. 花括号
```
# {m}   # 准确出现m次
# {m,n} # 至少出现m次，最多出现n次
[root@localhost test]# echo "bet" | gawk --re-interval '/b[ae]{1,2}t/{print $0}'
bet
[root@localhost test]# echo "beet" | gawk --re-interval '/b[ae]{1,2}t/{print $0}'
beet
[root@localhost test]# echo "beeet" | gawk --re-interval '/b[ae]{1,2}t/{print $0}'
[root@localhost test]# echo "beeet" | gawk --re-interval '/b[ae]{3}t/{print $0}'
beeet
```
### 4. 管道符(|)
```
相当于OR，任何一个匹配成功就通过
正则表达式和管道符之间不能有空格，否则会加到正则表达式中
```
### 5. 聚合表达式(括号)
```
# 正则表达式也可以用圆括号聚合起来
[root@localhost test]# echo "cat" | gawk '/(c|b)at/{print $0}'
cat
[root@localhost test]# echo "ebt" | gawk '/(c|b)(a|b)t/{print $0}'
[root@localhost test]# echo "bat" | gawk '/(c|b)at/{print $0}'
bat
[root@localhost test]# echo "bbt" | gawk '/(c|b)(a|b)t/{print $0}'
bbt
```
## 3. 实用
```
# 查看PATH环境变量，并用空格替换冒号(;)
[root@localhost test]# echo $PATH | sed 's/:/ /g'
/usr/local/sbin /usr/local/bin /sbin /bin /usr/sbin /usr/bin /root/bin
```

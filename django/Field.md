## Django字段类型清单
> 注：该文本为网上查询的资料，并修改了部分格式和内容

| 字段 | 说明 |
| ---- | ---- |
| AutoField | 自动递增的整型字段，通常不需要指定 |
| BooleanField | 布尔字段 |
| CharField     | 字符串字段，单行输入，必填参数(max_length) |
| TextField     | 文本字段，容量大，多行编辑框    |
| CommaSeparatedIntegerField    | 存放逗号分隔的整数值，必填参数(max_length)   |
| DateField     | 日期字段，auto_now（对象保存时间）,auto_now_add（对象创建时间）  |
| DateTimeField     | 类似DateField，支持相同的选项   | 
| EmailField    | 带有Email合法性的CharField  |
| FileField     | 文件上传字段，详情如下 |
| FilePathField     | 选择指定目录按照限定规则选择文件，详情如下 |
| ImageField    | 图片上传字段，可选参数(height_field:高度，width_field:宽度) |
| FloatFIeld    | 浮点型，必填参数(max_digits：除小数点和符号外的总位数，decimal_places：小数点位数)   |
| IntegerFie    | 整数字段      |
| SmallIntegerField     | 小整型字段     |
| PositiveIntegerField  | 整数字段，且非负数     |
| PositiveSmallIntegerField     | 整数小整型字段    |
| IPAddressField    | 字符串类型的IP地址    |
| NullBooleanField  | 布尔类型，但是允许NULL作为其中一个选项（相当于BooleanField加 null=True）     |
| PhoneNumberField  | 合法美国风格的电话号码的CharField(格式：XXX-XXX-XXXX)    |
| SlugField     | 只包含字母、数字、下划线和连字符，通常用于URLs |
| TimeField     | 时间字段  |
| URLField      | 用于保存URL   |
| XMLField      | XML字符字段，校验值是否为合法XML的TextField，必填参数（schema_path：校验文本的 RelaxNG schema 的文件系统路径）|


## Field选项
- null ：缺省设置为false，通常不将其用于字符型字段上，字符型字段如果没有值会返回空字符串。
- blank：该字段是否可以为空。如果为假，则必须有值
- choices：一个用来选择值的2维元组。第一个值是实际存储的值，第二个用来方便进行选择。如SEX_CHOICES= ((‘F’,'Female’),(‘M’,'Male’),)
- core：db_column，db_index 如果为真将为此字段创建索引
- default：设定缺省值
- editable：如果为假，admin模式下将不能改写。缺省为真
- help_text：admin模式下帮助文档
- primary_key：设置主键，如果没有设置django创建表时会自动加上
- radio_admin：用于admin模式下将select转换为radio显示。只用于ForeignKey或者设置了choices
- unique：数据唯一
- unique_for_date：日期唯一，如下例中系统将不允许title和pub_date两个都相同的数据重复出现
- title = meta.CharField(maxlength=30,unique_for_date=’pub_date’)
- unique_for_month / unique_for_year：用法同上
- validator_list：有效性检查。非有效产生 django.core.validators.ValidationError 错误
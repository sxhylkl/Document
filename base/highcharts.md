# Highcharts

> * [官方文档](http://www.hcharts.cn/docs/start-download)
> * [api文档](http://api.hcharts.cn)
> * [参考实例](http://www.hcharts.cn/download)
> * [菜鸟教程](http://www.runoob.com/highcharts/highcharts-tutorial.html)

## Highcharts

Highcharts 纯JavaScript编写的一个图表库， 简单便捷的在 Web 网站或是 Web 应用程序添加有交互性的图表

### 优势
- 支持IE6+、iPhone/iPad、Android 等浏览器,支持手机浏览器（响应式、缩放、手势操作等）
- 完全免费，并且提供完整的源代码；同时基于 Github 开源社区
- 纯Javascript，不需要任何插件，只需要两个 js 文件即可运行
- 支持直线图、曲线图、面积图、曲线面积图、面积范围图、曲线面积范围图、柱状图、柱状范围图、条形图、饼图、散点图、箱线图、气泡图、误差线图、漏斗图、仪表图、瀑布图、雷达图，共18种类型图表，其中很多图表可以集成在同一个图形中形成综合图。
- Highstock 支持股票走势图、K线图及大数据量时间轴图表
- Highmaps 支持各种地图，支持经纬度、GeoJSON 标准地图数据
- 结合jQuery、MooTools、Prototype 等 Javascript 框架提供的 Ajax 接口，可以实时地从服务器取得数据并实时刷新图表
- 提供多轴支持。并且可以针对每个轴设置其位置、文字和样式等属性
- 支持显示数据点的信息提示框，显示的内容和样式可以自己指定和设置
- 可以将 Highcharts 系列软件生成的图表导出为 PNG、JPG、PDF 和 SVG 格式文件或直接在网页上打印出来
- 可以设置图表的缩放、平移、手势缩放，Highstock 还支持滚动条、范围选择器、日期选择器等更多高级功能
- 支持多种数据形式，Javascript 数组、json 文件、json 对象、表格数据、CSV 文件等，这些数据来源可以是本地文件、数据接口，甚至是不同网站


### 使用Highcharts

#### 1.引入在线资源
```
<script src="http://cdn.hcharts.cn/jquery/jquery-1.8.3.min.js"></script>
<script src="http://cdn.hcharts.cn/highcharts/highcharts.js"></script>
<script src="http://cdn.hcharts.cn/highcharts/modules/exporting.js"></script>
```
#### 2.图表主要组成

一般情况下，Highcharts 包含标题（Title）、坐标轴（Axis）、数据列（Series）、数据提示框（Tooltip）、图例（Legend）、版权标签（Credits）等，另外还可以包括导出功能按钮（Exporting）、标示线（PlotLines）、标示区域（PlotBands）、数据标签（dataLabels）等。

![图表主要组成](images/highcharts_struct.png)

#### 3.图表类型

|英文名 |中文名 |
|----|----|
|line   | 直线图|
|spline | 曲线图 |
|area   | 面积图|
|areaspline | 曲线面积图 |
|arearange  | 面积范围图  |
|areasplinerange |曲线面积范围图 |
|column | 柱状图 |
|columnrange| 柱状范围图 |  
|bar |条形图 |
|pie |饼图  |
|scatter| 散点图 |
|boxplot |箱线图 |
|bubble | 气泡图 |
|errorbar  |  误差线图 |   
|funnel | 漏斗图 |
|gauge  | 仪表图 |
|waterfall  | 瀑布图 |
|polar |  雷达图 |
|pyramid |金字塔 |


# 基于Python的新冠病毒数据分析


## 概述

本项目主要使用 `Python3.8` ，首先从 [新型冠状病毒肺炎疫情分布](https://2019ncov.chinacdc.cn/2019-nCoV/) 网站抓取疫情数据，数据分为国际类型(各国的疫情数据)，国内类型(中国各省的疫情数据)，然后将数据进行清洗并转换为 `.csv` 文件，最后在 `Jupyter Notebook` 上利用得到的数据进行数据分析并进行可视化展示。



## 快速开始

### 运行环境

本项目在 `Windows 10` 和 `Google Colab` 上均调试成功

运行 `pip install -r requriments.txt` 以安装项目的所有依赖

### 数据的抓取和转换

`mynewspider.py` 定义了一个爬虫，用于疫情数据的抓取和转换。

```sh
usage: mynewspider.py [-h] [--dst DST] [--start START] [--end END] [--world] [--domestic]

optional arguments:
  -h, --help     show this help message and exit
  --dst DST      .csv 文件存放的文件夹
  --start START  选择开始下载的日期
  --end END      选择结束下载的日期
  --world        下载全球疫情数据
  --domestic     下载中国的疫情数据
```

使用示例：

`python mynewspider.py --dst global --start 20200101 --end 20220915 --world`

`python mynewspider.py --dst china --start 20200101 --end 20220915 --domestic`

### 数据分析

`global/`, `china/` 文件夹中已经默认包含我执行前一个步骤后获取的国际和国内新冠疫情数据。

接下来数据分析的部分在 `covid19-analysis.ipynb` 中完成，具体过程在 `.ipynb` 文件中给出：

- 数据准备
- 获取世界各国某天的疫情数据
- 获取世界各国的疫情时序增长曲线
- 获取某天各国新增确诊数和新增死亡数的词云图
- 创建世界疫情交互式 Choropleth 地图
- 获取中国截止到某天的累计确诊数最少的五个行政区的确诊人数比例饼图

在这一步中，可以在本机或者 `Google Colab` 运行 `jupyter notebook` 笔记本，`Google Colab` 是 `Google` 开发的在线 `Jupyter Notebook` 运行网站。可以在云端运行 `Jupyter Notebook` 脚本。

- 注：由于本项目在进行数据分析时的 `covid19-analysis.ipynb` 是在 `Google Colab` 上运行的，因此若在本地运行 `.ipynb` 笔记本，则需将 `covid19-analysis.ipynb` 放在项目文件夹 `covid19-analysis/` 的上一层目录以使数据读取正常。



## 参考项目与文献

[1] [Sumyak-Jain](https://github.com/Sumyak-Jain)/**[COVID-19](https://github.com/Sumyak-Jain/COVID-19)**

[2] [新型冠状病毒肺炎疫情分布](https://2019ncov.chinacdc.cn/2019-nCoV/)

[3] [Colab使用matplotlib和seaborn绘图中文乱码问题解决](https://zhuanlan.zhihu.com/p/140102126)

[4] [Python数据可视化 词云图 绘制词云的方法总结](https://cloud.tencent.com/developer/article/1699651)

[5] [如何在 Seaborn 中创建饼图](https://verytoolz.com/blog/06f8e49424/)

[6] [Avoiding overlapping when slices are tiny](https://stackoverflow.com/questions/63586376/avoiding-overlapping-when-slices-are-tiny)

[7] [Python绘制饼图调节字体大小、防止标签重叠解决方法](https://www.cnblogs.com/mengxiaoleng/p/12804117.html)

[8] [下载最新的全球疫情历史数据](https://blog.csdn.net/weixin_42464154/article/details/125135440?spm=1001.2014.3001.5502)

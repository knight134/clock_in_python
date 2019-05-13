# clock_in_python
打卡学习python？
* 总共51个视频，共分为9个项目
* 最后一个项目有关爬虫的使用
* 修改本地commit设置
---
## 章节
* python语言介绍
* 汇率兑换
* 分形树的绘制
* 基础代谢率计算（BMR）
* 52周存钱挑战
* 判断一年中的第几天
* 判断一个密码的强弱
* 模拟投骰子
* 空气质量指数的计算（AQI）
---

### os模块的函数
* os.remove()	删除文件
* os.makedirs()	创建多层目录
* os.rmdir()	删除单级目录
* os.rename()	重命名文件
* os.pathisfile()
* os.path.isdir()
* os.path.join()
* os.path.splitext()	将文件分割成文件名与扩展名，如分割tmp.txt为tmp和.txt
---
### requests 模块
* get()	对应http的GET方式
* post()	对应http的POST方式，用于传递用户数据

* status_code	http请求的返回状态码，200 - 连接成功，400 - 连接失败。比如有名的404
* text	url对应的字符串内容
	http://docs.python-requests.org/
---
### beautifulsoup4解析网页
* import bs4
* 创建beautifulsoup对象
* find	找到第一个满足条件的节点
* find_all	找到所有满足条件的节点
* bs=BeautifulSoup(url,html_parser,encoding)
---
### Pandas数据分析模块
* Pandas基于NumPy，提供高性能矩阵运算
* 绘图功能基于matplotlib. https://pandas.pydata.org/pandas-docs/stable/visualization.html
* import pandas as pd
* Series	类似于一维数组
* DataFrame	多维数组/表格数据
* pd.read_csv(f)	读
* pd.to_csv(o)	写
* skipna()	跳过缺失值
* dropna()	丢掉缺失值



# AgileH
爬取链家房价信息（目前支持获取全国楼盘和二手房数据）

### 准备
安装 ES，并运行`Lianjia/ES/init.py` 文件创建 ES 索引。

### 运行
1. 安装依赖  `pip install -r requirements.txt`
2. `python run.py`
默认会先执行二手房的爬取，后执行楼盘的爬取，可在 `run.py` 中进行顺序调整

### 规划
+ [x] 数据清洗
+ [x] 数据保存至 ES
+ [ ] 修改运行方式，添加 `spiderkeeper`
+ [ ] 图表分析
# AgileH
爬取链家房价信息（目前支持获取全国楼盘和二手房数据）

### 1. 准备

- 安装 ES

```shell
docker pull docker.elastic.co/elasticsearch/elasticsearch:6.5.0
```

```shell
docker run -itd -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.5.0
```

- 运行`Lianjia/ES/init.py` 文件创建 ES 索引

- 安装  [elasticsearch-head]( <https://github.com/mobz/elasticsearch-head> )  (可选)。如果需要安装 elasticsearch-head，那么需要修改 elasticsearch.yml，让其支持跨域请求。yml 文件内容如下，启动 ES 时，只需将其挂载进容器即可。
```yaml
cluster.name: "docker-cluster"
network.host: 0.0.0.0
http.cors.enabled: true
http.cors.allow-origin: "*"
```

```shell
docker run -itd -p 9200:9200 -p 9300:9300  -v /tmp/es/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.5.0
```



### 运行

- 安装依赖  `pip install -r requirements.txt`
- `python run.py`默认会先执行二手房的爬取，后执行楼盘的爬取，可在 `run.py` 中进行顺序调整

### 结果
测试爬取楼盘数据 115064条。二手房数据 288060条。共 403124 条数据
![](https://raw.githubusercontent.com/rexyan/warehouse/master/20190803191846.png)

### 规划
+ [x] 数据清洗
+ [x] 数据保存至 ES
+ [ ] 修改运行方式，添加 `spiderkeeper`
+ [ ] 图表分析



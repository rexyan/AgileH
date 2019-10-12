from elasticsearch import Elasticsearch
from LianJia.settings import ES_CONFIG, ES_LOUPAN_MAPPING, ES_ERSHOUFANG_MAPPING


class Elastic:
    def __init__(self, index_name, ip=ES_CONFIG.get("address")):
        """
        :param index_name:
        :param ip:
        """
        self.index_name = index_name
        # 无用户名密码状态
        self.es = Elasticsearch([ip])
        # 用户名密码状态
        # self.es = Elasticsearch([ip], http_auth=(ES_CONFIG.get("username"), ES_CONFIG.get("password")), port=ES_CONFIG.get("port"))

    def create_index(self, index_mapping):
        """
        :param index_mapping: mapping
        :return:
        """
        # 创建映射
        if self.es.indices.exists(index=self.index_name) is not True:
            res = self.es.indices.create(index=self.index_name, body=index_mapping)
            print(res)


if __name__ == "__main__":
    # 新建楼盘索引(名称和爬虫名称一致)
    es = Elastic("lianjialoupan")
    es.create_index(ES_LOUPAN_MAPPING)

    # 新建二手房索引(名称和爬虫名称一致)
    es = Elastic("lianjiaershoufang")
    es.create_index(ES_ERSHOUFANG_MAPPING)

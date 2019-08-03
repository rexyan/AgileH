from elasticsearch import Elasticsearch
from LianJia.LianJia.settings import ES_MAPPINGS


class Elastic:
    def __init__(self, index_name, ip="127.0.0.1"):
        """
        :param index_name:
        :param ip:
        """
        self.index_name = index_name
        # 无用户名密码状态
        self.es = Elasticsearch([ip])
        # 用户名密码状态
        # self.es = Elasticsearch([ip], http_auth=('elastic', 'password'), port=9200)

    def create_index(self):
        """
        :return:
        """
        # 创建映射
        _index_mappings = ES_MAPPINGS
        if self.es.indices.exists(index=self.index_name) is not True:
            res = self.es.indices.create(index=self.index_name, body=_index_mappings)
            print(res)


if __name__ == "__main__":
    es = Elastic("lianjia")
    es.create_index()

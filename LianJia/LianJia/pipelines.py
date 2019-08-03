# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import copy
from elasticsearch import Elasticsearch


class ElasticSearchPipeline(object):
    def __init__(self, host, database, user, password, port):
        # 连接 es
        self.es = Elasticsearch(["127.0.0.1"])
        self.INDEX_NAME = 'lianjia'

    @classmethod
    def from_crawler(cls, crawler):
        # 读取配置文件，读取 es 配置
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            port=crawler.settings.get('MYSQL_PORT'),
        )

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        spider_name = spider.name
        doc_type, _data = self.clean_data(spider_name, item)
        if _data:
            self.es.index(index=self.INDEX_NAME, doc_type=doc_type, body=_data)

    @staticmethod
    def clean_data(spider_name, item):
        """
        清洗数据 TODO 待优化
        :param spider_name:
        :param item:
        :return:
        """
        item_data = item._values
        item_clean_data = copy.deepcopy(item_data)
        doc_type = None

        if spider_name == "LianJiaLouPan":
            # 设置 es 类型
            doc_type = "lou_pan"

            # 清洗数据
            item_clean_data["loupan_name"] = item_data["loupan_name"][0] if len(item_data["loupan_name"]) > 0 else ""
            item_clean_data["loupan_location"] = item_data["loupan_location"][0] if len(item_data["loupan_location"]) > 0 else ""
            item_clean_data["loupan_room_type"] = item_data["loupan_room_type"][0] if len(item_data["loupan_room_type"]) > 0 else ""
            item_clean_data["loupan_room_num"] = item_data["loupan_room_num"] if len(item_data["loupan_room_num"]) > 0 else []
            item_clean_data["loupan_area_range"] = item_data["loupan_area_range"][0].replace("建面", "").replace("㎡", "").replace(" ", "").split("-") if len(item_data["loupan_area_range"]) > 0 else ""
            item_clean_data["loupan_mean_price"] = item_data["loupan_mean_price"][0] if len(item_data["loupan_mean_price"]) > 0 else ""
            item_clean_data["loupan_mean_unit"] = item_data["loupan_mean_unit"][0].replace("\xa0", "") if len(item_data["loupan_mean_unit"]) > 0 else ""
            item_clean_data["loupan_start_price"] = item_data["loupan_start_price"][0] if len(item_data["loupan_start_price"]) > 0 else ""
        elif spider_name == "LianJiaErShouFang":
            # 设置 es 类型
            doc_type = "ershoufang"

            # 清洗数据
            item_clean_data["ef_region"] = item_data["ef_region"][0].replace(" ", "")
            item_clean_data["ef_house_info"] = [x.replace(" ", "") for x in item_data["ef_house_info"][0].replace(" ", "").split("|") if x]
            item_clean_data["ef_house_type"] = item_data["ef_house_type"][0].replace("-", "").replace(" ", "").split("|")
            item_clean_data["ef_position"] = item_data["ef_position"][0].replace(" ", "")
            item_clean_data["ef_total_price"] = item_data["ef_total_price"][0].replace(" ", "")
            item_clean_data["ef_total_price_unit"] = item_data["ef_total_price_unit"][0].replace(" ", "")
            item_clean_data["ef_unit_price"] = item_data["ef_unit_price"][0].replace(" ", "")
        print(item_clean_data)
        return doc_type, item_clean_data

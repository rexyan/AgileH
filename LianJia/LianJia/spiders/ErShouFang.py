import json

from .LianJIaBaseSpider import LianJiaBaseSpider, Request
from ..settings import *


class LianJiaLouPanSpider(LianJiaBaseSpider):
    name = "LianJiaErShouFang"
    ef_suffix = "/ershoufang/"

    # 获取二手房城市信息
    start_urls = 'https://www.lianjia.com/city/'
    ef = "ef_url"

    def start_requests(self):
        """
        这是一个重载函数，它的作用是发出第一个Request请求
        :return:
        """
        yield Request(self.start_urls)

    def parse(self, response):
        """
        获取二手房城市
        :param response:
        :return:
        """
        # 获取城市名称
        city_name = response.xpath(XPATH_ERSHOUFANG_CITY_NAME).extract()

        # 城市主页
        city_urls = response.xpath(XPATH_ERSHOUFANG_CITY_URLS).extract()

        city_data = dict(zip(city_name, city_urls))
        for name, urls in city_data.items():
            ef = urls + self.ef_suffix
            yield Request(ef, callback=self.get_ef_city_detail_info, meta={self.ef: ef})

    def get_ef_city_detail_info(self, response):
        """
        获取某个城市二手房数据页码，并循环调用
        :param response:
        :return:
        """
        max_num = 0
        page_info = response.xpath(XPATH_ERSHOUFANG_PAGE_INFO).extract()
        if page_info:
            max_num = json.loads(page_info[0]).get("totalPage", 0)
        for i in range(1, max_num):
            url = response.meta[self.ef] + 'pg' + str(i)
            yield Request(url, callback=self.get_ef_detail_info, priority=max_num - i)

    @staticmethod
    def get_ef_detail_info(response):
        """
        获取二手房详细信息
        :param response:
        :return:
        """
        ef_dom = response.xpath(XPATH_ERSHOUFANG_ERSHOUFANG_DOM)
        for ef_dom_item in ef_dom:
            _result = {}
            for ITEM_NAME, VALUE_ITEM in XPATH_ERSHOUFANG_VALUE_ITEM.items():
                _result.update({ITEM_NAME: ef_dom_item.xpath(VALUE_ITEM).extract()})
            print(_result)

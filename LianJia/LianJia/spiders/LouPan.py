from scrapy.http import Request
import scrapy

from ..settings import *


class LianJiaLouPanSpider(scrapy.Spider):
    name = "LianJiaLouPan"
    allowed_domains = ["lianjia.com"]
    protocol = "https:"
    loupan_suffix = "/loupan/"

    # 从某个城市入手，获取楼盘信息，如果从 https://www.lianjia.com/city/ 获取，有些城市没有楼盘，会出现异常
    start_urls = 'https://bj.fang.lianjia.com' + loupan_suffix

    def start_requests(self):
        """
        这是一个重载函数，它的作用是发出第一个Request请求
        :return:
        """
        yield Request(self.start_urls)

    def parse(self, response):
        """
        获取所有有楼盘的城市
        :param response:
        :return:
        """
        # 获取城市名称
        city_name = response.xpath(XPATH_CITY_NAME).extract()

        # 城市主页
        city_urls = response.xpath(XPATH_CITY_URLS).extract()

        city_data = dict(zip(city_name, city_urls))
        for name, urls in city_data.items():
            loupan_url = self.protocol + urls + self.loupan_suffix
            yield Request(loupan_url, callback=self.get_city_detail_info, meta={'loupan_url': loupan_url})

    def get_city_detail_info(self, response):
        """
        获取某个城市楼盘分页信息，进行遍历请求
        :param response:
        :return:
        """
        max_page = response.xpath(XPATH_MAX_PAGE).extract()
        max_num = int(max_page[0])
        for i in range(1, max_num):
            url = response.meta['loupan_url'] + 'pg' + str(i)
            yield Request(url, callback=self.get_loupan_detail_info, priority=max_num - i)

    @staticmethod
    def get_loupan_detail_info(response):
        """
        获取某个城市某页楼盘具体数据
        :param response:
        :return:
        """
        loupan_dom = response.xpath(XPATH_LOUPAN_DETAIL)

        # 判断是否有楼盘信息（防止出现真实数据只有一页，但是获取的最大页数为5页，这样会抓取到推荐楼盘信息）
        null_data = response.xpath(XPATH_LOUPAN_NULL_DATA)
        if null_data:
            return

        print("null_data", null_data)
        for loupan_dom_item in loupan_dom:
            _result = dict()
            for ITEM_NAME, VALUE_ITEM in XPATH_LOUPAN_VALUE_ITEM.items():
                _result.update({ITEM_NAME: loupan_dom_item.xpath(VALUE_ITEM).extract()})
            print(_result)

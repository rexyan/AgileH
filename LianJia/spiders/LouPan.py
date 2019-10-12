import datetime

from .LianJIaBaseSpider import LianJiaBaseSpider, Request
from ..settings import *
from ..items import LianjiaLouPanItem


class LianJiaLouPanSpider(LianJiaBaseSpider):
    name = "LianJiaLouPan"
    loupan_suffix = "/loupan/"

    # 从某个城市入手，获取楼盘信息，如果从 https://www.lianjia.com/city/ 获取，有些城市没有楼盘，会出现异常
    start_urls = 'https://bj.fang.lianjia.com' + loupan_suffix
    data_item = LianjiaLouPanItem()

    def start_requests(self):
        """
        这是一个重载函数，它的作用是发出第一个请求
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
        city_name = response.xpath(XPATH_LOUPAN_CITY_NAME).extract()

        # 城市主页
        city_urls = response.xpath(XPATH_LOUPAN_CITY_URLS).extract()

        city_data = dict(zip(city_name, city_urls))
        for name, urls in city_data.items():
            loupan_url = self.protocol + urls + self.loupan_suffix
            yield Request(
                loupan_url,
                callback=self.get_loupan_city_detail_info,
                meta={
                    'loupan_url': loupan_url,
                    "spider_city": name
                }
            )

    def get_loupan_city_detail_info(self, response):
        """
        获取某个城市楼盘分页信息，进行遍历请求
        :param response:
        :return:
        """
        max_page = response.xpath(XPATH_LOUPAN_MAX_PAGE).extract()
        max_num = int(max_page[0])
        for i in range(1, max_num):
            url = response.meta['loupan_url'] + 'pg' + str(i)
            yield Request(
                url,
                callback=self.get_loupan_detail_info,
                priority=max_num - i,
                meta={
                    "spider_city": response.meta['spider_city'],
                    "spider_url": url
                }
            )

    def get_loupan_detail_info(self, response):
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

        for loupan_dom_item in loupan_dom:
            for ITEM_NAME, VALUE_ITEM in XPATH_LOUPAN_VALUE_ITEM.items():
                self.data_item[ITEM_NAME] = loupan_dom_item.xpath(VALUE_ITEM).extract()
            self.data_item["spider_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.data_item["spider_url"] = response.meta['spider_url']
            self.data_item["spider_city"] = response.meta['spider_city']
            print(self.data_item)
            yield self.data_item

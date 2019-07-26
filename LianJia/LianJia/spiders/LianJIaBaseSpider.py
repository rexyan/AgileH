import scrapy
from scrapy.http import Request


class LianJiaBaseSpider(scrapy.Spider):
    allowed_domains = ["lianjia.com"]
    protocol = "https:"

    def parse(self, response):
        pass

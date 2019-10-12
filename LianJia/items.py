# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaBaseItem(scrapy.Item):
    spider_time = scrapy.Field()
    spider_url = scrapy.Field()
    spider_city = scrapy.Field()


class LianjiaLouPanItem(LianjiaBaseItem):
    loupan_name = scrapy.Field()
    loupan_address = scrapy.Field()
    loupan_location = scrapy.Field()
    loupan_room_type = scrapy.Field()
    loupan_room_num = scrapy.Field()
    loupan_area_range = scrapy.Field()
    loupan_mean_price = scrapy.Field()
    loupan_mean_unit = scrapy.Field()
    loupan_start_price = scrapy.Field()
    loupan_tags = scrapy.Field()


class LianjiaErShouFangItem(LianjiaBaseItem):
    ef_region = scrapy.Field()
    ef_house_info = scrapy.Field()
    ef_house_type = scrapy.Field()
    ef_position = scrapy.Field()
    ef_total_price = scrapy.Field()
    ef_total_price_unit = scrapy.Field()
    ef_unit_price = scrapy.Field()

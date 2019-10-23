# -*- coding: utf-8 -*-

# Scrapy settings for LianJia project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'LianJia'

SPIDER_MODULES = ['LianJia.spiders']
NEWSPIDER_MODULE = 'LianJia.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'LianJia (+http://www.yourdomain.com)'

# Obey robots.txt rules 不遵循 robots.txt
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# 模拟浏览器
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'LianJia.middlewares.LianjiaSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'LianJia.middlewares.LianjiaDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# 启用 pipeline
ITEM_PIPELINES = {
    'LianJia.pipelines.ElasticSearchPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# 用户自定义设置
# loupan xpath 解析规则设置

XPATH_LOUPAN_CITY_NAME = '//div[contains(@class,"city-enum") and contains(@class,"fl")]/a/text()'
XPATH_LOUPAN_CITY_URLS = '//div[contains(@class,"city-enum") and contains(@class,"fl")]/a/@href'
XPATH_LOUPAN_MAX_PAGE = '//div[@class="page-box"]/@data-total-count'
# XPATH_LOUPAN_MAX_PAGE = '//div[@class="page-box"]//a[][last()]/text()'
XPATH_LOUPAN_DETAIL = '//ul[@class="resblock-list-wrapper"]/li'
XPATH_LOUPAN_NULL_DATA = '//div[contains(@class,"no-result-wrapper") and contains(@class,"show")]'

XPATH_LOUPAN_NAME = 'div/div[@class="resblock-name"]/a/text()'
XPATH_LOUPAN_ADDRESS = 'div/div[@class="resblock-location"]/span/text()'
XPATH_LOUPAN_LOCATION = 'div/div[@class="resblock-location"]/a/text()'
XPATH_LOUPAN_ROOM_TYPE = 'div/div[@class="resblock-name"]/span[@class="resblock-type"]/text()'
XPATH_LOUPAN_ROOM_NUM = 'div/a[@class="resblock-room"]/span/text()'
XPATH_LOUPAN_AREA_RANGE = 'div/div[@class="resblock-area"]/span/text()'
XPATH_LOUPAN_MEAN_PRICE = 'div/div[@class="resblock-price"]/div[@class="main-price"]/span[@class="number"]/text()'
XPATH_LOUPAN_MEAN_UNIT = 'div/div[@class="resblock-price"]/div[@class="main-price"]/span[@class="desc"]/text()'
XPATH_LOUPAN_START_PRICE = 'div/div[@class="resblock-price"]/div[@class="second"]/text()'
XPATH_LOUPAN_TAGS = 'div/div[@class="resblock-tag"]/span/text()'

XPATH_LOUPAN_VALUE_ITEM = {
    "loupan_name": XPATH_LOUPAN_NAME,  # 楼盘名称
    "loupan_address": XPATH_LOUPAN_ADDRESS,  # 楼盘地址
    "loupan_location": XPATH_LOUPAN_LOCATION,  # 楼盘详细地址
    "loupan_room_type": XPATH_LOUPAN_ROOM_TYPE,  # 楼盘类型
    "loupan_room_num": XPATH_LOUPAN_ROOM_NUM,  # 房间数
    "loupan_area_range": XPATH_LOUPAN_AREA_RANGE,  # 楼盘价格范围
    "loupan_mean_price": XPATH_LOUPAN_MEAN_PRICE,  # 楼盘平均价格
    "loupan_mean_unit": XPATH_LOUPAN_MEAN_UNIT,  # 楼盘价格单位
    "loupan_start_price": XPATH_LOUPAN_START_PRICE,  # 楼盘起始价格
    "loupan_tags": XPATH_LOUPAN_TAGS  # 楼盘标签
}

# ershoufang xpath 解析规则设置

XPATH_ERSHOUFANG_CITY_NAME = '//div[@class="city_province"]/ul/li/a/text()'
XPATH_ERSHOUFANG_CITY_URLS = '//div[@class="city_province"]/ul/li/a/@href'
XPATH_ERSHOUFANG_PAGE_INFO = '//div[contains(@class,"page-box") and contains(@class,"house-lst-page-box")]/@page-data'
XPATH_ERSHOUFANG_ERSHOUFANG_DOM = '//ul[@class="sellListContent"]/li'

XPATH_ERSHOUFANG_ERSHOUFANG_REGION = 'div/div[@class="address"]/div[@class="houseInfo"]/a/text()'
XPATH_ERSHOUFANG_ERSHOUFANG_HOUSE_INFO = 'div/div[@class="address"]/div[@class="houseInfo"]/text()'
XPATH_ERSHOUFANG_ERSHOUFANG_HOUSU_TYPE = 'div/div[@class="flood"]/div[@class="positionInfo"]/text()'
XPATH_ERSHOUFANG_ERSHOUFANG_POSITION = 'div/div[@class="flood"]/div[@class="positionInfo"]/a/text()'
XPATH_ERSHOUFANG_ERSHOUFANG_TOTALPRICE = 'div/div[@class="priceInfo"]/div[@class="totalPrice"]/span/text()'
XPATH_ERSHOUFANG_ERSHOUFANG_TOTALPRICE_UNIT = 'div/div[@class="priceInfo"]/div[@class="totalPrice"]/text()'
XPATH_ERSHOUFANG_ERSHOUFANG_UNITPRICE = 'div/div[@class="priceInfo"]/div[@class="unitPrice"]/span/text()'

XPATH_ERSHOUFANG_VALUE_ITEM = {
    "ef_region": XPATH_ERSHOUFANG_ERSHOUFANG_REGION,  # 地区
    "ef_house_info": XPATH_ERSHOUFANG_ERSHOUFANG_HOUSE_INFO,  # 二手房信息
    "ef_house_type": XPATH_ERSHOUFANG_ERSHOUFANG_HOUSU_TYPE,  # 二手房类型
    "ef_position": XPATH_ERSHOUFANG_ERSHOUFANG_POSITION,  # 二手房位置
    "ef_total_price": XPATH_ERSHOUFANG_ERSHOUFANG_TOTALPRICE,  # 二手房总价
    "ef_total_price_unit": XPATH_ERSHOUFANG_ERSHOUFANG_TOTALPRICE_UNIT,  # 二手房总价单位
    "ef_unit_price": XPATH_ERSHOUFANG_ERSHOUFANG_UNITPRICE,  # 二手房单价
}

ES_LOUPAN_MAPPING = {
    "mappings": {
        "lou_pan": {
            "properties": {
                "loupan_name": {
                    "type": "keyword",
                    "index": False,
                },
                "loupan_address": {
                    "type": "keyword",
                    "index": False
                },
                "loupan_location": {
                    "type": "keyword",
                    "index": True,
                    "fields": {
                        "non_pollution": {
                            "type": "keyword",
                            "index": False,
                        }
                    }
                },
                "loupan_room_type": {
                    "type": "keyword",
                },
                "loupan_room_num": {
                    "type": "keyword",
                },
                "loupan_area_range": {
                    "type": "keyword",
                },
                "loupan_mean_price": {
                    "type": "keyword",
                },
                "loupan_mean_unit": {
                    "type": "keyword",
                    "index": False
                },
                "loupan_start_price": {
                    "type": "keyword",
                    "index": False
                },
                "loupan_tags": {
                    "type": "keyword",
                },
                "spider_city": {
                    "type": "keyword"
                },
                "spider_time": {
                    "type": "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd"
                },
                "spider_url": {
                    "type": "keyword",
                    "index": False
                }
            }
        }
    }
}

ES_ERSHOUFANG_MAPPING = {
    "mappings": {
        "ershoufang": {
            "properties": {
                "ef_region": {
                    "type": "keyword",
                    "index": False
                },
                "ef_house_info": {
                    "type": "keyword",
                    "index": False
                },
                "ef_house_type": {
                    "type": "keyword",
                    "index": False
                },
                "ef_position": {
                    "type": "keyword",
                    "index": False
                },
                "ef_total_price": {
                    "type": "keyword",
                    "index": False
                },
                "ef_total_price_unit": {
                    "type": "keyword",
                    "index": False
                },
                "ef_unit_price": {
                    "type": "keyword",
                    "index": False
                },
                "spider_city": {
                    "type": "keyword",
                    "index": False
                },
                "spider_time": {
                    "type": "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd"
                },
                "spider_url": {
                    "type": "keyword",
                    "index": False
                }
            }
        }
    }
}

# ES 信息
ES_CONFIG = {
    "port": "9200",
    "address": "192.168.16.161",
    "password": "",
    "username": ""
}

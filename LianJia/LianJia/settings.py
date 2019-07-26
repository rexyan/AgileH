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
# ITEM_PIPELINES = {
#    'LianJia.pipelines.LianjiaPipeline': 300,
# }

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
## xpath 解析规则设置
XPATH_CITY_NAME = '//div[contains(@class,"city-enum") and contains(@class,"fl")]/a/text()'
XPATH_CITY_URLS = '//div[contains(@class,"city-enum") and contains(@class,"fl")]/a/@href'
XPATH_MAX_PAGE = '//div[@class="page-box"]/@data-total-count'
# XPATH_MAX_PAGE = '//div[@class="page-box"]//a[][last()]/text()'
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

from scrapy import cmdline


spider_name = 'LianJiaLouPan'
cmd = f'scrapy crawl {spider_name}'
cmdline.execute(cmd.split())
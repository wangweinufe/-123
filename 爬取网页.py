import scrapy
from script_2.items import Script2Item
from scrapy.http import Request
class src2Spider(scrapy.Spider):
        name = 'script_2'
        redis_key = 'script:start_urls'
        start_urls= ['http://www.jb51.net/article/80000.htm']
        url = 'http://www.jb51.net/article/'
        pageNum = 80000
#####
BOT_NAME = 'script_2'
SPIDER_MODULES = ['script_2.spiders']
NEWSPIDER_MODULE = 'script_2.spiders'
ITEM_PIPELINES = ['script_2.pipelines.Script2Pipeline']
#mongodb config
MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'script'
MONGODB_DOCNAME = 'script_8'
# The initial download delay
AUTOTHROTTLE_START_DELAY=5
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG=Ture
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY=60

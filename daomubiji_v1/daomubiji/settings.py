# -*- coding: utf-8 -*-

# Scrapy settings for daomubiji project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'daomubiji'

SPIDER_MODULES = ['daomubiji.spiders']
NEWSPIDER_MODULE = 'daomubiji.spiders'

#ITEM_PIPELINES = {
#    'daomubiji.pipelines.DaomubijiPipeline': 300 # 数字代表这个管道的优先级，取0-1000之间的任意一个数即可
#}

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
COOKIES_ENABLED = True

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
SCHEDULER_PERSIST = True
REDIS_HOST = '192.168.1.13'
REDIS_PORT = 6379

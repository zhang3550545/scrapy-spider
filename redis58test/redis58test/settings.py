# -*- coding: utf-8 -*-

# Scrapy settings for redis58test project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'redis58test'

SPIDER_MODULES = ['redis58test.spiders']
NEWSPIDER_MODULE = 'redis58test.spiders'

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True

ITEM_PIPELINES = {
    'redis58test.pipelines.Redis58TestPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}
REDIS_HOST = '192.168.108.20'
REDIS_PORT = 6379


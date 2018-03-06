# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    # 标题
    title = scrapy.Field()
    # 图片的url链接，可以没有
    image_url = scrapy.Field()
    # 新闻来源
    source = scrapy.Field()
    # 点击的url
    action_url = scrapy.Field()


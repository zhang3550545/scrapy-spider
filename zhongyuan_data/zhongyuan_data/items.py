# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhongyuanDataItem(scrapy.Item):
    # 小区名称
    name = scrapy.Field()
    # 房屋格局
    room = scrapy.Field()
    # 面积
    square = scrapy.Field()
    # 成交时间
    date = scrapy.Field()
    # 总价
    total = scrapy.Field()
    # 单价
    price = scrapy.Field()
    # 区域
    zone = scrapy.Field()
    # 版块
    area = scrapy.Field()

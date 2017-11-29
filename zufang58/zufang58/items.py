# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Zufang58Item(scrapy.Item):
    # 标题
    title = scrapy.Field()
    # 房间
    room = scrapy.Field()
    # 区域
    zone = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 价格
    money = scrapy.Field()
    # 发布信息的类型，品牌公寓，经纪人，个人
    type = scrapy.Field()
    pass

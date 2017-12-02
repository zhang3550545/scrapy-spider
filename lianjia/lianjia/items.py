# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # 标题
    title = scrapy.Field()
    # 房子编号
    code = scrapy.Field()
    # 房间    几房几厅
    room = scrapy.Field()
    # 房子    面积
    size = scrapy.Field()
    # 房子    位置
    position = scrapy.Field()
    # 房子    朝向
    orientation = scrapy.Field()
    # 地址    小区地址
    address = scrapy.Field()
    # 区域    闵行
    zone = scrapy.Field()
    # 子区域  浦江
    area = scrapy.Field()
    # 建造时间
    buildTime = scrapy.Field()
    # 总价
    money = scrapy.Field()
    # 单价
    priceUnit = scrapy.Field()
    # 标签
    label = scrapy.Field()

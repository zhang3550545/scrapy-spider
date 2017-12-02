#!/usr/bin/env python
# encoding: utf-8

"""
__author__: Widsom Zhang
__time__: 2017/12/1 21:11
"""

from scrapy.spider import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from lianjia.items import LianjiaItem


class LianJiaSpider(CrawlSpider):
    name = 'lianjia'
    roominfoow_domains = ['sh.lianjia.com']
    start_urls = ['http://sh.lianjia.com/ershoufang']

    pageLink = LinkExtractor(allow='/ershoufang/d\d+')

    rules = [Rule(link_extractor=pageLink, callback='page_parse', follow=True)]

    def page_parse(self, response):
        # 根节点     //ul[@class="js_fang_list"]/li
        # title     .//div[@class="prop-title"]/a/text()
        # code      .//div[@class="prop-title"]/a/@key
        # room  size position orientation    .//span[@class="info-col row1-text"]/text()     [room,size,position,or] 可能没有数据
        # address                            .//span[@class="info-col row2-text"]/a/span/text()
        # zone  area                         .//span[@class="info-col row2-text"]/a/text()   [zone,area]
        # buildTime                          .//span[@class="info-col row2-text"]/text()         需要清除数据（\d+）
        # money     .//div[@class="info-col price-item main"]/span/text()    [390,万] 需要拼接
        # priceUnit                         .//span[@class="info-col price-item minor"]/text()
        # label     .//div[@class="property-tag-container"]/span/text()  [标签1，标签2，标签3]

        for element in response.xpath('//ul[@class="js_fang_list"]/li'):
            title = element.xpath('.//div[@class="prop-title"]/a/text()').extract_first()
            code = element.xpath('.//div[@class="prop-title"]/a/@key').extract_first()

            roominfo = element.xpath('.//span[@class="info-col row1-text"]/text()').extract()[-1].split('|')
            length = len(roominfo)
            room = ''
            size = ''
            position = ''
            orientation = ''
            if length > 0:
                room = roominfo[0].strip()
            if length > 1:
                size = roominfo[1].strip()
            if length > 2:
                position = roominfo[2].strip()
            if length > 3:
                orientation = roominfo[3].strip()

            address = element.xpath('.//span[@class="info-col row2-text"]/a/span/text()').extract_first()

            zones = element.xpath('.//span[@class="info-col row2-text"]/a/text()').extract()
            zone = ''
            area = ''
            if len(zones) > 0:
                zone = zones[0]
            if len(zones) > 1:
                area = zones[1]

            buildTime = element.xpath('.//span[@class="info-col row2-text"]/text()').extract()[-1].replace('|', '').strip()

            money = ''
            for item in element.xpath('.//div[@class="info-col price-item main"]/span/text()').extract():
                money = money + item

            priceUnit = element.xpath('.//span[@class="info-col price-item minor"]/text()').extract_first().strip()

            label = ''
            for item in element.xpath('.//div[@class="property-tag-container"]/span/text()').extract():
                label = label + item + ","

            item = LianjiaItem()
            item['title'] = title
            item['code'] = code
            item['room'] = room
            item['size'] = size
            item['position'] = position
            item['orientation'] = orientation
            item['address'] = address
            item['zone'] = zone
            item['area'] = area
            item['buildTime'] = buildTime
            item['money'] = money
            item['priceUnit'] = priceUnit
            item['label'] = label

            yield item

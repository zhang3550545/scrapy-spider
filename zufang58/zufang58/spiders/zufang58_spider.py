#!/usr/bin/env python
# encoding: utf-8

"""
__author__: Widsom Zhang
__time__: 2017/11/29 9:44
"""

from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor
from zufang58.items import Zufang58Item


class ZuFang58Spider(CrawlSpider):
    # spider的唯一名称
    name = 'zufang58'
    # 开始爬取的url
    start_urls = ["http://sh.58.com/chuzu/"]
    # 从页面需要提取的url 链接(link)
    links = LinkExtractor(allow="sh.58.com/chuzu/pn\d+")
    # 设置解析link的规则，callback是指解析link返回的响应数据的的方法
    rules = [Rule(link_extractor=links, callback="parseContent", follow=True)]

    def parseContent(self, response):
        """
        解析响应的数据，获取需要的数据字段
        :param response: 响应的数据
        :return:
        """
        # 根节点 //ul[@class="listUl"]/li[@logr]
        # title: .//div[@class="des"]/h2/a/text()
        # room: .//div[@class="des"]/p[@class="room"]/text()
        # zone: .//div[@class="des"]/p[@class="add"]/a[1]/text()
        # address: .//div[@class="des"]/p[@class="add"]/a[last()]/text()
        # money: .//div[@class="money"]/b/text()
        # type: # .//div[@class="des"]/p[last()]/@class     # 如果是add,room  .//div[@class="des"]/div[@class="jjr"]/@class

        for element in response.xpath('//ul[@class="listUl"]/li[@logr]'):
            title = element.xpath('.//div[@class="des"]/h2/a/text()')[0].extract().strip()
            room = element.xpath('.//div[@class="des"]/p[@class="room"]')[0].extract()
            zone = element.xpath('.//div[@class="des"]/p[@class="add"]/a[1]/text()')[0].extract()
            address = element.xpath('.//div[@class="des"]/p[@class="add"]/a[last()]/text()')[0].extract()
            money = element.xpath('.//div[@class="money"]/b/text()')[0].extract()
            type = element.xpath('.//div[@class="des"]/p[last()]/@class')[0].extract()
            if type == "add" or type == "room":
                type = element.xpath('.//div[@class="des"]/div[@class="jjr"]/@class')[0].extract()

            item = Zufang58Item()

            item['title'] = title
            item['room'] = room
            item['zone'] = zone
            item['address'] = address
            item['money'] = money
            item['type'] = type

            yield item

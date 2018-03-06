#!/usr/bin/env python
# encoding: utf-8

"""
__author__: Widsom Zhang
__time__: 2018/3/5 16:35
"""

from scrapy import Spider
from scrapy_splash import SplashRequest
from news.items import NewsItem


class GoolgeNewsSpider(Spider):
    name = "google_news"

    start_urls = ["https://news.google.com/news/headlines?ned=cn&gl=CN&hl=zh-CN"]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 1})

    def parse(self, response):
        for element in response.xpath('//div[@class="qx0yFc"]'):
            actionUrl = element.xpath('.//a[@class="nuEeue hzdq5d ME7ew"]/@href').extract_first()
            title = element.xpath('.//a[@class="nuEeue hzdq5d ME7ew"]/text()').extract_first()
            source = element.xpath('.//span[@class="IH8C7b Pc0Wt"]/text()').extract_first()
            imageUrl = element.xpath('.//img[@class="lmFAjc"]/@src').extract_first()

            item = NewsItem()
            item['title'] = title
            item['image_url'] = imageUrl
            item['action_url'] = actionUrl
            item['source'] = source

            yield item

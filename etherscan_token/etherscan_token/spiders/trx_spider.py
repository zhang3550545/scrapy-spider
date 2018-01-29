#!/usr/bin/env python
# encoding: utf-8

"""
__author__: Widsom Zhang
__time__: 2018/1/29 11:59
"""
from scrapy import Request
from scrapy.spider import Spider

from etherscan_token.items import EtherscanTokenItem


class TRXSpider(Spider):
    name = "trx"  # 0xf230b790e05390fc8295f4d3f60332c93bed42e2
    url = "https://etherscan.io/token/generic-tokenholders2?a=0xf230b790e05390fc8295f4d3f60332c93bed42e2&s=1E%2b27&p="
    page = 2000  # start page
    start_urls = [url + str(page)]

    def parse(self, response):
        for ele in response.xpath("//tr"):
            results = ele.xpath("./td/span/a/text()").extract()
            if len(results) > 0:
                token = results[0]
                item = EtherscanTokenItem()
                item['token'] = token
                yield item

        self.page += 1
        print("request url: %s" % (self.url + str(self.page)))
        yield Request(self.url + str(self.page))

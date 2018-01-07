#!/usr/bin/env python
# encoding: utf-8

"""
__author__: Widsom Zhang
__time__: 2018/1/5 16:51
"""

from scrapy.spider import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor, re
from zhongyuan_data.items import ZhongyuanDataItem


class ZhongYuanSpider(CrawlSpider):
    name = 'zhongyuan'
    start_urls = ['http://sh.centanet.com/chengjiao/pudongxinqu/',
                  'http://sh.centanet.com/chengjiao/minxingqu/',
                  'http://sh.centanet.com/chengjiao/baoshanqu/',
                  'http://sh.centanet.com/chengjiao/putuoqu/',
                  'http://sh.centanet.com/chengjiao/xuhuiqu/',
                  'http://sh.centanet.com/chengjiao/changningqu/',
                  'http://sh.centanet.com/chengjiao/jinganqu/',
                  'http://sh.centanet.com/chengjiao/huangpuqu/',
                  'http://sh.centanet.com/chengjiao/zhabeiqu/',
                  'http://sh.centanet.com/chengjiao/hongkouqu/',
                  'http://sh.centanet.com/chengjiao/yangpuqu/',
                  'http://sh.centanet.com/chengjiao/songjiang/',
                  'http://sh.centanet.com/chengjiao/jiadingqu/',
                  'http://sh.centanet.com/chengjiao/qingpuqu/',
                  'http://sh.centanet.com/chengjiao/jinshanqu/',
                  'http://sh.centanet.com/chengjiao/fengxianqu/',
                  'http://sh.centanet.com/chengjiao/chongmingqu/']

    # 区域的链接提取
    zone_links = LinkExtractor(allow="/chengjiao/[a-z]+/",
                               deny=("/chengjiao/contrast/", "/chengjiao/[a-z]+qu/", "/chengjiao/songjiang/"))
    # 页面的链接获取
    page_links = LinkExtractor(allow="/chengjiao/[a-z]+/g[0-9]+/")
    # 解析规则
    rules = [Rule(zone_links, process_links="deal_link", follow=True),
             Rule(page_links, callback="page_parse", follow=True)]

    def deal_link(self, links):
        for link in links:
            link.url = link.url + "g1/"
            print(link.url)
        return links

    def page_parse(self, response):
        lists = response.xpath('//label[@class="btn-condi"]/text()').extract()
        for element in response.xpath('//table[@class="table-record"]/tr'):
            results = element.xpath('./td').extract()
            if len(results) > 0:
                item = ZhongyuanDataItem()
                item['name'] = self.deal_tag(results[0])
                item['room'] = self.deal_tag(results[1])
                item['square'] = self.deal_tag2(results[3])
                item['date'] = self.deal_tag2(results[4])
                item['total'] = self.deal_tag2(results[5])
                item['price'] = self.deal_tag2(results[6])
                if len(lists) > 1:
                    item['zone'] = lists[0]
                    item['area'] = lists[1]
                    print(item)
                    yield item

    def deal_tag(self, source):
        return re.findall('>.+</', source.replace('\r\n', ''))[0].replace(">", "").replace("</", "").strip()

    def deal_tag2(self, source):
        return re.findall('>.+</', source)[0].replace(">", "").replace("</", "").strip()

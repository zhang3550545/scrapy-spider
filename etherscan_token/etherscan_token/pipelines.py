# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from scrapy.conf import settings
from etherscan_token.spiders.bnb_spider import BnbSpider
from etherscan_token.spiders.eos_spider import EOSSpider
from etherscan_token.spiders.omg_spider import OMGSpider
from etherscan_token.spiders.qtm_spider import QTMSpider
from etherscan_token.spiders.trx_spider import TRXSpider
from etherscan_token.spiders.snt_spider import SNTSpider
from etherscan_token.spiders.zrx_spider import ZRXSpider
from etherscan_token.spiders.rep_spider import RepSpider



class EtherscanTokenPipeline(object):
    def __init__(self):
        host = settings['MONGODN_HOST']
        port = settings['MONGODB_PORT']
        db_name = settings['MONGODB_DB_NAME']

        self.tb_eos = settings['MONGODB_COLLECTION_EOS']
        self.tb_bnb = settings['MONGODB_COLLECTION_BNB']
        self.tb_omg = settings['MONGODB_COLLECTION_OMG']
        self.tb_qtm = settings['MONGODB_COLLECTION_QTM']
        self.tb_trx = settings['MONGODB_COLLECTION_TRX']
        self.tb_snt = settings['MONGODB_COLLECTION_SNT']
        self.tb_zrx = settings['MONGODB_COLLECTION_ZRX']
        self.tb_rep = settings['MONGODB_COLLECTION_REP']

        self.client = pymongo.MongoClient(host=host, port=port)
        self.mydb = self.client[db_name]

    def process_item(self, item, spider):
        if isinstance(spider, BnbSpider):
            # 插入tb_bnb表中
            self.mydb[self.tb_bnb].insert(dict(item))
        elif isinstance(spider, EOSSpider):
            self.mydb[self.tb_eos].insert(dict(item))
        elif isinstance(spider, OMGSpider):
            self.mydb[self.tb_omg].insert(dict(item))
        elif isinstance(spider, QTMSpider):
            self.mydb[self.tb_qtm].insert(dict(item))
        elif isinstance(spider, TRXSpider):
            self.mydb[self.tb_trx].insert(dict(item))
        elif isinstance(spider, SNTSpider):
            self.mydb[self.tb_snt].insert(dict(item))
        elif isinstance(spider, ZRXSpider):
            self.mydb[self.tb_zrx].insert(dict(item))
        elif isinstance(spider, RepSpider):
            self.mydb[self.tb_zrx].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
        pass

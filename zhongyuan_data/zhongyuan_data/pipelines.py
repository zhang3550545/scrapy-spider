# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo

from scrapy.conf import settings


class ZhongyuanDataPipeline(object):
    def __init__(self):
        host = settings['MONGODN_HOST']
        port = settings['MONGODB_PORT']
        db_name = settings['MONGODB_DB_NAME']
        collection_name = settings['MONGODB_COLLECTION_NAME']

        self.client = pymongo.MongoClient(host=host, port=port)
        mydb = self.client[db_name]
        self.collection = mydb[collection_name]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
        pass

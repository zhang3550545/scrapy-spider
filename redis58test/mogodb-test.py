#!/usr/bin/env python
# encoding: utf-8

"""
__author__: Widsom Zhang
__time__: 2018/3/14 13:50
"""

import json
import redis
import pymongo


def main():
    # 指定Redis数据库信息
    rediscli = redis.StrictRedis(host='192.168.108.20', port=6379, db=0)
    # 指定MongoDB数据库信息
    mongocli = pymongo.MongoClient(host='localhost', port=27017)

    # 创建数据库名
    db = mongocli['redis58test']
    # 创建表名
    sheet = db['redis58_sheet2']

    while True:
        # FIFO模式为 blpop，LIFO模式为 brpop，获取键值
        source, data = rediscli.blpop(["redis58spider_redis:items"])

        item = json.loads(data)
        sheet.insert(item)

        try:
            print(u"Processing: %(name)s <%(link)s>" % item)
        except KeyError:
            print(u"Error procesing: %r" % item)


if __name__ == '__main__':
    main()

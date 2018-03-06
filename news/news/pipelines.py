# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class NewsPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='db_news',
                                    charset='utf8')
        self.cursor = self.conn.cursor()
        pass

    def process_item(self, item, spider):
        sql = '''insert into tb_google_news (title,image_url,action_url,source) values(%s,%s,%s,%s)'''
        self.cursor.execute(sql, (item["title"], item["image_url"], item["action_url"], item["source"]))
        self.conn.commit()
        return item

    def close_spider(self):
        self.cursor.close()
        self.conn.close()

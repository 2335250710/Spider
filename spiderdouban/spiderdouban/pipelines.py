# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from spiderdouban import settings
import json,pymongo

class SpiderdoubanPipeline(object):
    def __init__(self):
        host = 'localhost'
        port = 27017
        dbname = 'Douban'
        dbcollection = 'DouBanMovies'
        client = pymongo.MongoClient(host=host, port=port)
        mdb = client[dbname]
        self.dbcollection = mdb[dbcollection]

    def process_item(self, item, spider):
        data = dict(item)
        self.dbcollection.insert_one(data)
        return item
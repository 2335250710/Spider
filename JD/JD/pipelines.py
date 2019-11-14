# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json, pymongo


class JdPipeline(object):
    def __init__(self):
        host = 'localhost'
        port = 27017
        client = pymongo.MongoClient(host=host, port=port)
        ndb = client['JD']
        self.dbcollection = ndb['JD_Data']

    def process_item(self, item, spider):
        data = dict(item)
        self.dbcollection.insert_one(data)
        return item

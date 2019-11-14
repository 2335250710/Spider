# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 书名
    big_category = scrapy.Field()  # 大分类
    big_category_link = scrapy.Field()  # 大分类页面url
    small_category = scrapy.Field()  # 小分类
    small_category_link = scrapy.Field()  # 小分类页面url
    cover_url = scrapy.Field()  # 封面图片链接
    detail_url = scrapy.Field()  # 详情页面url
    author = scrapy.Field()  # 作者
    publisher = scrapy.Field()  # 出版社
    pub_date = scrapy.Field()  # 出版时间
    price = scrapy.Field()  # 价格

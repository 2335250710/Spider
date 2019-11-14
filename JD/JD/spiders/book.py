# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from ..items import JdItem


class BookSpider(RedisSpider):
    name = 'book'
    allowed_domains = ['jd.com', 'p.3.cn']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        # 获取大分类的节点链接，节点名称
        big_list = response.xpath('//div[@id="booksort"]/div[2]/dl/dt/a')
        for big in big_list:
            big_list_url = 'http' + big.xpath('./@href').extract_first()
            big_category = big.xpath('./text()').extract_first()
            # 小分类的节点列表
            small_list = big.xpath('../following-sibling::dd[1]/em/a')
            for small in small_list:
                temp = {}
                temp['big_list_url'] = big_list_url
                temp['big_category'] = big_category
                temp['small_category'] = small.xpath('./text()').extract_first()
                temp['small_category_url'] = 'https:' + small.xpath('./@href').extract_first()
                # 构造请求，返回小分类url
                yield scrapy.Request(
                    temp['small_category_url'],
                    callback=self.parse_book_list,
                    meta={'meta1': temp}
                )

    # 解析书籍列表信息
    def parse_book_list(self, response):
        # 接受parse方法返回的meta数据
        temp = response.meta['meta1']
        # 获取书籍列表信息
        book_list = response.xpath('//*[@id="plist"]/ul/li/div')
        # 遍历书籍列表
        for book in book_list:
            # 实例化item
            item = JdItem()
            item['name'] = book.xpath('./div[3]/a/em/text()').extract_first().strip()
            item['big_category'] = temp['big_category']
            item['big_category_link'] = temp['big_list_url']
            item['small_category'] = temp['small_category']
            item['small_category_link'] = temp['small_category_url']
            item['cover_url'] = book.xpath('./div[1]/a/img/@src').extract_first()
            item['detail_url'] = book.xpath('./div[3]/a/@href').extract_first()
            item['author'] = book.xpath('./div[4]/span[1]/span/a/text()').extract_first()
            item['publisher'] = book.xpath('./div[4]/span[2]/a/text()').extract_first()
            item['pub_date'] = book.xpath('./div[4]/span[3]/text()').extract_first().strip()
            # 获取价格
            skuid = book.xpath('./@data-sku').extract_first()
            pduid = '&pduid=1523432585886562677791'
            if skuid:
                url = 'https://p.3.cn/prices/mgets?skuIds=J_' + skuid + pduid
                yield scrapy.Request(
                    url,
                    callback=self.parse_price,
                    meta={'meta2': item}
                )

    # 解析价格
    def parse_price(self, response):
        import json
        item = response.meta['meta2']
        data = json.loads(response.body)
        print(data)
        item['price'] = data[0]['op']
        yield item

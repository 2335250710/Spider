# -*- coding: utf-8 -*-
import scrapy
from spiderdouban.items import SpiderdoubanItem

class DoubanSpiderSpider(scrapy.Spider):
    # 继承scrapy.Spider, 这里是爬虫的名字, 不能和项目名字重复
    name = 'douban_spider'
    # 允许的域名
    allowed_domains = ['movie.douban.com']
    # 入口url，扔到调度器中
    # start_urls = ['http://movie.douban.com/']
    start_urls = ['https://movie.douban.com/top250']
    # 默认解析方法
    def parse(self, response):
        movie_list = response.xpath('//div[@id="content"]//ol/li')
        for i_item in movie_list:
            douban_item = SpiderdoubanItem()
            # 爬取序号
            douban_item['serial_number'] = i_item.xpath('./div[@class="item"]/div[@class="pic"]/em/text()').extract()[0]
            # 爬取电影名称
            douban_item['movie_name'] = i_item.xpath('./div[@class="item"]/div[@class="info"]/div[@class="hd"]/a/span[1]/text()').extract()[0]
            # 电影内容
            # 解析数据，而不是第一个
            content = i_item.xpath('.//div[@class="bd"]/p[1]/text()').extract()
            content_s = "".join(content[1].split())
            douban_item['introduce'] = content_s
            # 电影星级
            star = i_item.xpath('./div[@class="item"]/div[@class="info"]/div[@class="bd"]//span[1]/@class').extract()[0]
            a = star.replace('rating', '')
            b = a.replace('-t', '')
            c = int(b)
            if c > 10:
                c = c/10
            douban_item['star'] = c
            # 电影评分
            douban_item['rate'] = i_item.xpath('./div[@class="item"]/div[@class="info"]/div[@class="bd"]//span[2]/text()').extract_first()
            # 电影评价
            evalute = i_item.xpath('./div[@class="item"]/div[@class="info"]/div[@class="bd"]//span[4]/text()').extract_first()
            douban_item['evalute'] = evalute.replace('人评价', '')
            # 电影的描述
            douban_item['describe'] = i_item.xpath('./div[@class="item"]/div[@class="info"]/div[@class="bd"]//p[@class="quote"]/span/text()').extract_first()
            print(douban_item)
            # 不进行yeild无法进入pipelines里面, 将获取的数据交给pipelines
            yield douban_item
        # 解析下一页
        next_link = response.xpath('//span[@class="next"]/link/@href').extract_first()
        if next_link:
            yield scrapy.Request('https://movie.douban.com/top250'+next_link,callback=self.parse)
        # with open('douban.html','w',encoding='utf-8') as f:
        #     f.write(response.text)


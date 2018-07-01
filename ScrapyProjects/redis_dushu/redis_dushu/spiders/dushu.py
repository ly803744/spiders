# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import  LinkExtractor
from scrapy_redis.spiders import  RedisCrawlSpider
from scrapy.spiders import Rule
from scrapy import cmdline


# 1.可以使用命令的方式生成 Spider类
# scrapy genspider -t crawl dushu www.dushu.com

# 2.修改spider类
# 将继承的CrawlSpider类改为RedisCrawlSpider
# 声名开始请求的入口网址存在redis的key
# redis_key = 'dushu:start_urls'

class DushuSpider(RedisCrawlSpider):
    name = "dushu"
    allowed_domains = ["www.dushu.com"]

    # start_urls = ['https://www.dushu.com/']

    redis_key = 'dushu:start_urls'

    rules = (
        Rule(LinkExtractor(allow=r'/book/\d+_?\d*?.html'), callback='parse', follow=True),
    )

    def parse(self, response):

        i = {}  # 字典类型

        # 从当前的网页中获取图书的信息
        books = response.xpath('//div[@class="book-info"]')
        for book in books:
            i['name'] = book.xpath('./h3/a/text()').extract_first()      # 提取第一个结果
            i['book_url'] = book.xpath('./h3/a/@href').extract_first()
            i['author'] = book.xpath('./p/a/text()').extract()
            if i['author'] == []:
                i['author'] = book.xpath('./p/text()').extract()
                if i['author'] == []:
                    i['author'] = book.xpath('./p/em/text()').extract()
            i['author'] = ','.join(i['author'])

            i['summary'] = book.xpath('./p[last()-1]/text()').extract_first()
            i['img'] = book.xpath('.//a/img/@data-original').extract_first()


            yield i

if __name__ == '__main__':
    cmdline.execute('scrapy runspider dushu.py'.split())


# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dushu.items import DushuItem


class DsSpider(CrawlSpider):
    name = 'ds'
    allowed_domains = ['www.dushu.com','img.dushu.com']
    start_urls = ['http://www.dushu.com/']

    # 通过链接提取器，engine自动将所有的链接加入到下载对列中，
    # 当follow为True时，当下载器下载链接时，会自动提取本页的所有符合规则的链接，并加入到下载队列中，
    # 当链接请求成功后，由callback指定的解析函数来处理
    rules = (
        Rule(LinkExtractor(allow=r'/book/\d+_?\d*?.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = DushuItem()   # 字典类型
        # print('-------------获取图书信息---------------')
        # print(response.url)
        # print(response.xpath('//title/text()').extract()[0])

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

            # meta实现spider之间的数据传送，主要实现请求和响应之间的数据共享
            # meta传参时，不要使用对象的引用，需要使用常量值
            yield scrapy.Request(url = str(i['img']),
                                 meta = {'name':i['name']},
                                 callback=self.parse_img
                                 )

            yield i

    def parse_img(self,response):
        print('-----------------保存图片-----------------')
        # response.meta是读取request中的meta
        name = response.meta['name']
        print(name)
        print(response.url)

        # images目录，是相对于dushu项目的目录（参考发起命令的目录  scrapy crawl ds）
        fileName = 'images/'+name+'.'+response.url.split('.')[-1]
        with open(fileName,'wb') as f:
            f.write(response.body)



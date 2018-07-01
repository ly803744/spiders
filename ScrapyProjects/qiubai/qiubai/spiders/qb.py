# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse


class QbSpider(scrapy.Spider):
    # 在命令行中使用crawl命令，并指定qb的name名字，开始爬取站点的数据
    name = "qb"

    # 在请求站点资源的时候，只能是指定的域名下的资源
    allowed_domains = ["www.qiushibaike.com"]

    # 爬虫开始爬取资源的入口
    start_urls = ['http://www.qiushibaike.com/',
                  'https://www.qiushibaike.com/hot/',
                  'https://www.qiushibaike.com/imgrank/',
                  'https://www.qiushibaike.com/text/',
                  'https://www.qiushibaike.com/history/',
                  'https://www.qiushibaike.com/pic/',
                  'https://www.qiushibaike.com/textnew/']

    # 当请求资源成功时，会回调parse函数，进行数据解析
    # parse如果有返回数据，则返回可迭代的对象
    def parse(self, response:HtmlResponse):
        # print('*'*100)
        # # response是响应对象，包含常用的属性
        # print(response.encoding)   # 不能修改
        # print(response.headers)
        # print(response.status)
        # print(response.url)
        # print(response.request.url)
        # #  直接查询网页中的title标签，xpath()返回一个selector对象
        # print(response.xpath('//title/text()').extract())
        # print(response.selector.xpath('//title/text()').extract())
        # print(response.css('div[class="author clearfix"] a'))
        # print(response.text)   # 打印文本数据
        # print(response.body)   # 网页内容的字节码
        articles = response.xpath('//div[starts-with(@class,"article")]')
        # print(articles)
        for art in articles:
            # print(art)
            # article是Selector对象类型
            try:
                name = art.xpath('./div[1]//img/@alt').extract()[0]
                img = art.xpath('./div[1]//img/@src').extract()[0]
                content = art.xpath('.//div[@class="content"]/span[1]/text()').extract()
                # 读取下一页数据
            except:
                pass
            else:
                # print(name,img)
                # print(''.join(content).replace('\n', ''))

                from qiubai.items import QiubaiItem
                item = QiubaiItem()
                item['name'] = name
                item['img'] = 'http'+ img
                item['content'] = ''.join(content).replace('\n', '')
                # 将item的数据交给管道去处理
                # 利用协程的方式
                # yield {
                #     'name':name,
                #     'img':'http'+img,
                #     'content':''.join(content).replace('\n', '')
                #     }

                yield item

        next_url = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').extract()[0]
        next_page_url = response.urljoin(next_url)
        if next_page_url:
        # 发起下一页的请求
            yield scrapy.Request(next_page_url,callback=self.parse)
        # print(next_url)
        # print('*'*100)

        #  //div[starts-with(@class,"article")]/div[1]//img/@alt
        #  //div[starts-with(@class,"article")]/div[1]//img/@src
        #  //div[starts-with(@class,"article")]//div[@class="themb"]//img/@src

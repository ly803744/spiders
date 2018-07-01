# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import Rule
from scrapy import cmdline


class XhwSpider(RedisCrawlSpider):
    name = "mn"
    allowed_domains = ["www.meinv.hk"]

    redis_key = 'xh:start_urls'


    rules = (
        Rule(LinkExtractor(r'http://www.meinv.hk/.p=\d{4}'), callback='parse_items', follow=False),
    )


    def parse_items(self, response):
        print('---------获取的url----------')
        # print(response.url)

        # name response.xpath('//h1[@class="title"]/text()')
        # img   xpath'//div[@class="post-image"]/img/@src'


        i = {'name': response.css('h1[class="title"]::text').extract_first(),
             'content':response.css('div[class="post-content"] p::text').extract_first(),
             'images': response.css('div[class="post-image"] img::attr(src)').extract(),
             'url': response.url,
             }

        return i


if __name__ == '__main__':
    cmdline.execute('scrapy runspider xhw.py'.split())

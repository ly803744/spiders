# -*- coding: utf-8 -*-
import scrapy


class DySpider(scrapy.Spider):
    name = "dy"
    allowed_domains = ["www.ygdy8.net"]
    start_urls = ['http://www.ygdy8.net/html/gndy/dyzz/']

    def parse(self, response):
        # 解析的的电影列表页面   返回列表类型的selector对象
        links = response.xpath('//a[@class="ulink"]')
        # print(links)
        for link in links:
            try:
                name = link.xpath('./text()').extract()[0]
                # print(name)
                href = link.xpath('./@href').extract()[0]
                href = response.urljoin(href)
            except:
                pass
            else:
                # print(name,href)
                # 发起详情页面的请求
                yield scrapy.Request(href,callback=self.parse_video)
                # print("*"*100)

            # 考虑下一页
        next_page = response.xpath('//div[@class="x"]//a[last()-1]/@href').extract()[0]
        print('next_page---------------------------------------',next_page)
        next_page_url = DySpider.start_urls[0]+next_page
        print(next_page_url)
        yield scrapy.Request(next_page_url,callback=self.parse)


    def parse_video(self,response):
        with open('movie_info.html','wb') as f:
            f.write(response.body)

        # 解析详情的页面
        title =response.xpath('//h1/font/text()').extract()[0]
        video_url = response.xpath('//div[@class="co_area2"]/div[@class="co_content8"]/ul//table/tbody//a/@href').extract()[0]
        print('准备下载mkv',video_url,sep='\n')

        yield {
            'title':title,
            'video_url':video_url
        }





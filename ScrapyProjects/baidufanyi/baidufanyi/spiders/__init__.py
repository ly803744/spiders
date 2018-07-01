# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
import json

class FanyiSpider(scrapy.Spider):

    name = 'fy'
    allowed_domains = ['fanyi.baidu.com']

    # start_urls = ['http://www.fanyi.baidu.com/']

    def parse(self,response):
        print('-----------------------ok-------------------------')
        print(response.url)

        jsonTxt = json.loads(response.text)
        print(jsonTxt)


    # spider开始发起请求的函数
    def start_requests(self):
        print('开始发起请求')
        # get请求
        # yield scrapy.Request('http://www.fanyi.baidu.com/',callback=self.parse)

        url = 'http://fanyi.baidu.com/sug'

        data = {
            'kw':'apple',
            'from':'en',
            'to':'zh',
        }

        yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse)

        # 第一次请求成功后，继续发送请求
        # 在FormRequest()函数设置的参数
        # 设置url （请求的地址）
        # formdata（上传的参数）
        # headers（请求头）
        # callback
        yield scrapy.FormRequest(url = 'http://fanyi.baidu.com/v2transapi',
                                 formdata={'from':'en',
                                            'to':'zh',
                                            'query':'apple',
                                            'simple_means_flag':'3',
                                            'sign':'704513.926512',
                                            'token':'a852ae76a7d924a7e89a8fa825bfa87f'},
                                 callback=self.parse
                                 )


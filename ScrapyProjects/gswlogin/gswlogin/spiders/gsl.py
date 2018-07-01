# -*- coding: utf-8 -*-
import requests
import scrapy

from gswlogin.spiders import ydm_http


class GslSpider(scrapy.Spider):
    name = "gsl"
    allowed_domains = ["so.gushiwen.org"]
    start_urls = ['https://so.gushiwen.org/user/login.aspx']

    def parse(self, response):
        icode = response.xpath('//img[@id="imgCode"]/@src').extract()[0]
        icode = 'https://so.gushiwen.org' + icode
        print(icode)
        print("***************************************")
        s = requests.session()

        r = s.get(icode)

        if r.status_code == 200:
            with open('ccode.gif', 'wb') as f:
                f.write(r.content)
            print('验证码下载成功！！！')

            # 获取图片中的内容
            randcodeTxt = ydm_http.ydm('ccode.gif')
            print(type(randcodeTxt))
            print("获取到的验证码为：", randcodeTxt)

            yield scrapy.FormRequest(url='https://so.gushiwen.org/user/login.aspx?',
                                     formdata={
                                         # 'from': 'http://so.gushiwen.org/user/collect.aspx',
                                         'email': '610039018@qq.com',
                                         'pwd': 'disen8888',
                                         'code': randcodeTxt},
                                     callback=self.content_parse
                                     )
            print('登录成功！！！')

    def content_parse(self, response):
        title = response.xpath('//title/text()').extract_first()
        print(title)

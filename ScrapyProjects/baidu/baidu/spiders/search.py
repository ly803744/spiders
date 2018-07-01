# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy import cmdline
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapy.linkextractors import LinkExtractor


class SearchSpider(scrapy.Spider):
    name = "search"
    allowed_domains = ["www.baidu.com"]
    start_urls = ['https://www.baidu.com/']


    def  __init__(self):
        super().__init__(self.name)

        path = r'F:\qfproject\ScrapyProjects\baidu\baidu\spiders\chromedriver.exe'

        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.binary_location = path



        # /mac/linux必须将 chromdriver放在/usr/local/bin目录
        # driver = webdriver.Chrome(chrome_options=chrome_options)

        # self.brower = webdriver.Chrome(chrome_options=chrome_options)
        self.brower = webdriver.Chrome(path)




    def parse(self, response):
        print('------------------解析------------------')
        print(response.headers)
        print(response.url)
        self.brower.get(response.url)
        # 发起一个搜索（在搜索框中输入内容，点击搜索按钮）
        self.brower.find_element_by_id('kw').send_keys('python招聘')

                # 点击按钮
        self.brower.find_element_by_id('su').click()
        time.sleep(5)

        self.brower.save_screenshot('baidu01.png')

        # 通过链接提取器获取查询结果
        extractor = LinkExtractor(r'http://www.baidu.com/link\?.*')

        # 开始提取
        links = extractor.extract_links(self.brower.page_source)

        for link in links:
            print('title:',link.text)
            print('url:',link.url)

            # yield {
            #     'title':link.text,
            #     'url':link.url
            # }


    def __del__(self):
        # 关闭浏览器
        self.brower.quit()



if __name__ == '__main__':
    cmdline.execute('scrapy runspider search.py'.split())

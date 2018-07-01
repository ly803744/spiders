# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DushuItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()        #  书名 字典对象
    img = scrapy.Field()         # 图片
    author = scrapy.Field()      # 作者
    summary = scrapy.Field()     # 概要
    book_url = scrapy.Field()    # 书的详细地址


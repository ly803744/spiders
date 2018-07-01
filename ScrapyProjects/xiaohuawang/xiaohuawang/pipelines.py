# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

import scrapy
from scrapy.pipelines.images import ImagesPipeline

from xiaohuawang import settings


class DBPipeline(object):
    def process_item(self, item, spider):
        # image_urls = scrapy.Field()

        return item



class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 下载图片
        for image in item['img_url']:
            yield scrapy.Request(image,meta={'video_name':item['video_name']})


    def file_path(self, request, response=None, info=None):
        # 返回存储的文件名
        dirPath = os.path.join(settings.IMAGES_STORE,request.meta['video_name'])
        if not os.path.exists(dirPath):
            os.mkdir(dirPath)

        # 相对于IMAGES_STORE的目录
        return request.meta['video_name']+"/"+request.url.split('/')[-1]


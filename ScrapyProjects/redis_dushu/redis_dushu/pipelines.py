# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class RedisDushuPipeline(object):
    def process_item(self, item, spider):

        # 保存到数据库中

        return item
#
# class RedisPipeline(object):
#     def process_item(self,item,spider):
#
#         return item

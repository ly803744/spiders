# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class DyttPipeline(object):
    # 开始打开spider时，使用的回调函数
    def open_spider(self, spider):
        # 连接数据库
        print('打开数据库成功！！！')
        self.db = pymysql.connect(
                host='10.35.0.129',
                port=3306,
                user='root',
                password='root',
                db='dy',
                charset='utf8'
        )


        # 打开数据库操作
        self.cursor = self.db.cursor()
        print('数据库连接成功！！！')


    def close_spider(self, spider):
        print('关闭数据库')
        self.db.close()


    def process_item(self, item, spider):
        self.cursor.execute('insert dydata(title,video_url) values(%s,%s)',
                            args=(
                                item['title'],
                                item['video_url']
                            ))
        self.db.commit()  # 提交事务
        if self.cursor.rowcount >= 1:
            print(item['title'], '数据写入成功！！！')
        return item

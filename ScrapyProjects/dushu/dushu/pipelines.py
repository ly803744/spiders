# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib.request
import ssl

import pymysql

ssl._create_default_https_context =ssl._create_unverified_context


class DushuPipeline(object):

    def open_spider(self,spider):
        print('------打开数据库成功！！！---------')
        self.db = pymysql.connect(
            host = '10.35.0.129',
            port = 3306,
            user = 'root',
            password = 'root',
            db = 'ds',
            charset = 'utf8'
        )

        # 打开数据库
        print('-----------打开数据库成功！！！-----------')
        self.cursor = self.db.cursor()



    def close_spider(self,spider):
        # 关闭数据库
        self.db.close()



    def process_item(self, item, spider):
        # 向数据库写入
        print('-------item写入数据库的Pipeline------')
        sql = 'select name from ds where name =%s'
        self.cursor.execute(sql,args=(item['name'],))
        print('查询结果：',self.cursor.rowcount)
        if self.cursor.rowcount == 0:
            self.cursor.execute('insert  ds(name,book_url,author,summary,img) value(%s,%s,%s,%s,%s)',
                            args =(
                                item['name'],
                                item['book_url'],
                                item['author'],
                                item['summary'],
                                item['img']

                            ))
            print('数据写入成功！！！')

        self.db.commit()  # 提交事务
        if self.cursor.rowcount >= 1:
            print(item['name'], '数据已经存储了！！！')

        return item


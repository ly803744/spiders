# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class QiubaiPipeline(object):
    # 开始打开spider时，回调的函数
    def open_spider(self,spider):
        print('----------open spider----------------')

        # 连接数据库
        self.db = pymysql.connect(
            host = '10.35.0.129',
            port = 3306,
            user = 'root',
            password = 'root',
            db = 'qb',
            charset = 'utf8'
        )


        # 打开数据库操作对象（游标）
        self.cursor = self.db.cursor()
        print('连接数据库成功！！！')


    # 完成spider时，回调的函数
    def close_spider(self,spider):
        print('----------close spider----------------')
        self.db.close()


    # item管道在接收到蜘蛛spider返回的数据item时，由当前的item管道process_item()处理
    def process_item(self, item, spider):
        print('-----process item-----')
        # print(item['name'],item['img'])
        # 将数据写入到数据库中
        self.cursor.execute('insert content(name,img,content) value(%s,%s,%s)',
                            args = (item['name'],
                                    item['img'],
                                    item['content']))
        self.db.commit()   # 提交事务
        if self.cursor.rowcount >= 1:
            print(item['name'], '数据写入成功！！！')
        return item

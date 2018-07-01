# -*-coding:utf-8-*-
import os
import ssl
from urllib import request
from lxml import etree
import settings
from db import DBHelper
from item import UserItem
import random


class QiuBaiSpider():
    def __init__(self):
        self.db = DBHelper()
        ssl._create_default_https_context = ssl._create_unverified_context
        print('爬虫开始行动了……')

    def __del__(self):
        print('感谢有你，我要走了……')
        self.db.close()

    def request(self, url):
        # 创建opener浏览器对象,并且设置代理处理器
        opener = request.build_opener(request.ProxyHandler(proxies={'http': random.choice(settings.proxies['http'])}))
        req = request.Request(url, headers=settings.headers)
        resp = opener.open(req)
        if resp.status == 200:
            print('ok')
            html = resp.read().decode()
            # print(html)
            return html

    def parse(self, html):
        # 创建一个et对象
        et = etree.HTML(html)
        # print(et)
        authors = et.xpath(settings.author_path)
        # print(authors)
        for author in authors:  # author 的类型为 <class 'lxml.etree._Element'>
            # print(author)
            # print(type(author))
            try:
                # try不存在作用域
                home = author.xpath(settings.home_path)[0]  # './a/@href'
                id = home.split('/')[-2]  # /users/38248088/
                name = author.xpath(settings.name_path)[0]
                age = author.xpath(settings.age_path)[0]
                img = 'http:' + author.xpath(settings.src_path)[0].split('?')[0]
                # print(home)
            except:
                pass
            else:
                item = UserItem(id, name, age, img, home)
                # print(item)

                # 将数据存放到数据库
                self.db.save(item)
                self.saveImg(img, id)

        # 读取下一页的链接
        try:
            next_url = settings.start_url + et.xpath(settings.next_page_path)[0]
            print(next_url)
        except:
            pass
        else:
            return next_url

    def saveImg(self, url, id):

        filename = './head/{}.{}'.format(id, url.split('.')[-1])
        if os.path.exists(filename):
            return
        request.urlretrieve(url, filename=filename)
        print(filename, '图片下载成功！！！')

    def run(self):
        next_url = settings.start_url
        while True:
            html = self.request(next_url)

            # 解析网页并获取下一次请求的路径
            next_url = self.parse(html)

            if not next_url:
                break


if __name__ == '__main__':
    QiuBaiSpider().run()

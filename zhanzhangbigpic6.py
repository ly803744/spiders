# -*-coding:utf-8-*-

# ctrl+y   删除一行   ctrl+d  复制

import re
from urllib import request

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:60.0) Gecko/20100101 Firefox/60.0",
}

# 创建opener浏览器对象,并且设置代理处理器
opener = request.build_opener(request.ProxyHandler(proxies={'http': '218.14.115.211:3128'}))


def download(url, title):  # 下载功能
    filename = './zhandianpic/%s.jpg' % title
    request.urlretrieve(url, filename=filename)
    print(title, '图片下载完成！')


def requestHtml(url):  # 请求网页
    req = request.Request(url, headers=headers)
    resp = opener.open(req)
    if resp.status == 200:
        html = resp.read().decode()
        return html


def parseHtml(html):
    # 解析网页，获取图片地址和名称
    r1 = r'<div>.*?<a .*?href="(.*?)" .*?<img src[\d]?="(.*?)" alt="(.*?)"'
    imgs = re.findall(r1, html, flags=re.S)
    for href, img, title in imgs:
        print(href, title, img)
        # download(img, title)

        # 读取图片详情页面
        shtml = requestHtml(href)

        # 第二层网页解析
        bigImg = re.findall(r'<div class="imga">.*?<img src="(.*?)"', shtml, flags=re.S)
        download(bigImg[0], title)  # 下载大图


def main():
    url = "http://sc.chinaz.com/tupian/"
    html = requestHtml(url)
    parseHtml(html)


if __name__ == '__main__':
    main()

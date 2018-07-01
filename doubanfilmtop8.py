# -*-coding:utf-8-*-

import urllib.request
import urllib.parse
import threading
import json
import time

url = 'https://movie.douban.com/j/chart/top_list?'

# 声明请求头

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}


def spiderTop(type1=5, start=0, limit=20):
    params = {
        'type': type1,
        'interval_id': '100:90',
        'action': '',
        'start': start,  # 开始的记录数
        'limit': limit  # 每次请求记录的条数
    }

    params = urllib.parse.urlencode(params).encode()
    # 将字符串--------->字节
    # print(params)
    # 创建Response请求对象
    req = urllib.request.Request(url=url, data=params, headers=headers)
    # print(req)

    resp = urllib.request.urlopen(req)
    # print(resp)

    if resp.status == 200:
        # print('保存成功！！！')

        bytes = resp.read()
        # print(bytes)
        if bytes == b'[]':
            # print('没有可用的数据了')
            return

        with open('douban-top/douban-top-%d.json' % (start / limit + 1), 'wb') as f:
            f.write(bytes)

        # 下载图片
        # 获取图片的地址
        jsonStr = bytes.decode()  # 将byte->str
        # 从json字符串中加载json的数据，返回字典或列表
        jsonArray = json.loads(jsonStr)
        print('-------------------------', type(jsonArray), jsonArray)

        # print(type(jsonArray),jsonStr)
        for movie in jsonArray:
            url1 = movie.get('cover_url')
            title = movie.get('title')
            # print('图片的地址：',url)
            # print('图片的名称',title)

            # 启动线程来下载图片
            threading.Thread(target=downloadImg, args=(title, url1)).start()


def downloadImg(title, url):
    urllib.request.urlretrieve(url, filename='douban-image/%s.jpg' % title)
    # print('下载',title,'图片成功')


if __name__ == '__main__':
    # 生成20个线程
    ts = [threading.Thread(target=spiderTop, args=(5, i * 20)) for i in range(20)]
    for t in ts:
        t.start()

# -*-coding:utf-8-*-

# https://www.qiushibaike.com/8hr/page/1/

from urllib import request
from urllib import parse
import urllib
from multiprocessing import Pool
import threading
import re
# 爬虫的网址

# 声明请求头
import time

import math

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}


# 封装爬虫的网页地址
def spider_url(i):
    url = 'https://www.qiushibaike.com/8hr/page/'
    url = url + str(i) + '/'
    print(url)
    req = urllib.request.Request(url=url, headers=headers)
    resp = urllib.request.urlopen(req)

    if resp.status == 200:
        bytes = resp.read()
        # print(bytes.decode())
        print('******************')
        if bytes == b'[]':
            print('没有可用的数据了')
            return

        with open('qiushiwang/qiushi-top-{}.json'.format(i), 'w') as f:
            f.write(bytes.decode())

        pat1 = '<div class="article block untagged mb15 .*?".*?>.*?<img src="(.*?)" alt=.*?>.*?</div>'
        # pat1 = '<div class="thumb">.*?<img src="(.*?)" alt=.*?></div>'

        rst = re.compile(pat1, re.S).findall(bytes.decode())
        # print(rst)
        # print(rst)
        for j in range(0, len(rst)):
            # print(rst[j])
            imgurl = 'https:' + rst[j]
            print(imgurl)
            print("-------")
            # urllib.request.urlretrieve(imgurl,filename='./qiushiwang/%s.jpg'%str(math.trunc(time.time())))
            # print('保存成功！！！')
            # 启动线程来下载图片
            threading.Thread(target=downloadImg, args=(imgurl,)).start()


def downloadImg(url):
    # urllib.request.urlretrieve(url,filename='qiushiwang/%s'%(url.split('/')[-1]))   # 图片，第一个正则
    urllib.request.urlretrieve(url, filename='qiushiwang/%s' % (url.split("?")[0].split('/')[-1]))  # 头像
    print('下载图片成功')


if __name__ == '__main__':
    pool = Pool(processes=13)
    cs = [i for i in range(1, 13)]
    for i in range(12):
        pool.apply_async(spider_url, args=(cs[i],))
    pool.close()
    pool.join()
    print('已搞定')

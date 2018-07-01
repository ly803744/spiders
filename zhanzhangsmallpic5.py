#-*-coding:utf-8-*-

#-*-coding:utf-8-*-

# https://www.qiushibaike.com/8hr/page/1/
import os
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
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

# 封装爬虫的网页地址
def spider_url(i):

    url = 'http://sc.chinaz.com/tupian/index_'
    url = url+str(i)+'.html'
    print(url)
    req = urllib.request.Request(url=url,headers=headers)
    # print(req)
    resp = urllib.request.urlopen(req)
    # print(resp)

    if resp.status == 200:
        bytes = resp.read()
        # print(bytes.decode())
        print('******************')
        if bytes == b'[]':
            print('没有可用的数据了')
            return


        with open('zhanzhang/zhanzhang-top-{}.json'.format(i),'wb') as f:
            f.write(bytes)
        pat1 = r'<div>.*?<img src[\d]?="(.*?)" alt="(.*?)"'

        rst = re.findall(pat1,bytes.decode(),re.S)
        # print(rst)
        # print(rst)
        # print(rst)
        # print(len(rst))
        for j in range(0, len(rst)):
            print(rst[j][0])
            # imgurl = 'https:'+rst[j][0]
            # print(imgurl)
            print("-------")
            threading.Thread(target=downloadImg,args=(rst[j][0],rst[j][1]+".jpg")).start()


def downloadImg(url,title):
    # print('zhanzhang/'+title)
    # print(os.path.exists('zhanzhang/'+title))

    if os.path.exists('zhanzhang/'+title):
        print('已存在')
        return
    else:
        urllib.request.urlretrieve(url,filename='zhanzhang/{}'.format(title))  # 图片，第一个正则
        print('下载图片成功')






if __name__ == '__main__':
    pool = Pool(processes=13)
    cs =[i for i in range(2,14)]
    for i in range(12):
        pool.apply_async(spider_url,args=(cs[i],))
    pool.close()
    pool.join()
    print('已搞定')


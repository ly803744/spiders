import os
import threading
import urllib
from multiprocessing.pool import Pool
from urllib import request

from lxml import etree


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:60.0) Gecko/20100101 Firefox/60.0",
}

# 创建opener浏览器对象,并且设置代理处理器
opener = request.build_opener(request.ProxyHandler(proxies={'http':'218.14.115.211:3128'}))

# 请求网页：
def requestHtml(url):
    req = request.Request(url, headers=headers)
    resp = opener.open(req)
    if resp.status == 200:
        # print(resp.info())
        html = resp.read().decode()
        return (html)


# 解析网页：
def parseHtml(url,i):
    # 解析html
    et = etree.HTML(url)

    # r1 = '//img/@src2'   # 首页表情包
    # imgs = et.xpath(r1)
    # print(len(imgs))

    r2 = '//div[@class="up"]/div[@class="num_2"]/a/'   # 更多
    # titles = et.xpath('{}@title | {}@href'.format(r2, r2))
    titles = et.xpath('{}@href'.format(r2))
    # print(titles)
    # print(len(titles))

    for title in titles:
        # print(title)
        wurl = requestHtml(title)
        # print(wurl)
        et1 = etree.HTML(wurl)
        r3 = '//div/div[3]/img/@src'
        wPic = et1.xpath(r3) # 更多里面的每一个图片
        # print(wPic)

        r4 = '//h2/a[2]/text()'
        wTitle = et1.xpath(r4)[0] # 更多里面本也数据的标题
        # print(wTitle)
        # print(type(wTitle))
        for gif in wPic:
            # print(gif)
            threading.Thread(target=download,args=(i,gif,wTitle+gif.split('/')[-1])).start()



def download(i,url,title): # 下载功能
    if os.path.exists("qqsmile/第{}页".format(i)):
        if os.path.exists('qqsmile/第{}页/{}'.format(i,title)):
            print('图片已存在')
            # return
        else:
            urllib.request.urlretrieve(url,filename='qqsmile/第{}页/{}'.format(i,title))  # 图片，第一个正则
            print('下载图片成功')
    else:
        try:
            os.makedirs("qqsmile/第{}页".format(i))
            if os.path.exists('qqsmile/第{}页/{}'.format(i,title)):
                print('图片已存在')
                # return
            else:
                urllib.request.urlretrieve(url,filename='qqsmile/第{}页/{}'.format(i,title))  # 图片，第一个正则
                print('下载图片成功')
        except FileExistsError:
            print('文件存在错误----')



def main(i):
    url = 'http://sc.chinaz.com/biaoqing/index_'
    url = url+str(i)+'.html'
    parseHtml(requestHtml(url),i)




if __name__ == '__main__':
    pool = Pool(processes=10)
    for i in range(2,2501):
        pool.apply_async(main,args=(i,))
    pool.close()
    pool.join()
    print('保存成功！！！')


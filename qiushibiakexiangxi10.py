#-*-coding:utf-8-*-


import random
from urllib import request
from bs4 import BeautifulSoup

start_url = 'https://www.qiushibaike.com/'
# 创建一个头信息
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:60.0) Gecko/20100101 Firefox/60.0",
}


proxies = {
    'http':[
            '183.56.177.130:808',
            '112.115.57.20:3128',
            '114.115.182.59:3128',
            '121.42.167.160:3128'
            ],
    'https':''
}


def requestHtml(url):
    #创建opener浏览器对象，并且设置代理处理器
    opener = request.build_opener(request.ProxyHandler(proxies = {'http':random.choice(proxies['http'])}))
    req = request.Request(url,headers=headers)
    resp = opener.open(req)
    if resp.status == 200:
        html = resp.read()
        return url,html


def parse2(soup):
    try:
        # 头像的图片链接
        img_url = 'http:'+soup.select('div[class="user-header"]')[0].select('img')[0].attrs.get('src')
        # print(img_url)

        # 用户名
        username = soup.select('div[class="user-header"]')[0].select('img')[0].attrs.get('alt')
        # print(username)

        #--------------------------------------------糗百指数-------------------------------------------------------

        # 粉丝数
        number_of_fans = soup.select('div[class="user-col-left"]')[0].select('ul')[0].select('li')[0].text.split(':')[-1]
        # print(number_of_fans)

        # 关注数
        attention_number = soup.select('div[class="user-col-left"]')[0].select('ul')[0].select('li')[1].text.split(':')[-1]
        # print(attention_number)

        #糗事
        anecdote = soup.select('div[class="user-col-left"]')[0].select('ul')[0].select('li')[2].text.split(':')[-1]
        # print(anecdote)

        # 评论
        comment = soup.select('div[class="user-col-left"]')[0].select('ul')[0].select('li')[3].text.split(':')[-1]
        # print(comment)

        # 笑脸
        smiley_face = soup.select('div[class="user-col-left"]')[0].select('ul')[0].select('li')[4].text.split(':')[-1]
        # print(smiley_face)

        # 糗事精选
        highlights = soup.select('div[class="user-col-left"]')[0].select('ul')[0].select('li')[5].text.split(':')[-1]
        # print(highlights)


        # --------------------------------------------个人资料-------------------------------------------------------
        # 婚姻
        marriage = soup.select('div[class="user-col-left"]')[0].select('div')[1].select('ul')[0].select('li')[0].text.split(':')[-1]
        # print(marriage)


        # 星座
        constellation = soup.select('div[class="user-col-left"]')[0].select('div')[1].select('ul')[0].select('li')[1].text.split(':')[-1]
        # print(constellation)

        # 职业
        occupation = soup.select('div[class="user-col-left"]')[0].select('div')[1].select('ul')[0].select('li')[2].text.split(':')[-1]
        # print(occupation)

        # 故乡
        hometown = soup.select('div[class="user-col-left"]')[0].select('div')[1].select('ul')[0].select('li')[3].text.split(':')[-1]
        # print(hometown)

        # 糗龄
        age = soup.select('div[class="user-col-left"]')[0].select('div')[1].select('ul')[0].select('li')[4].text.split(':')[-1]
        # print(age)


        return (img_url,username,
                number_of_fans,attention_number,
                anecdote,comment,smiley_face,highlights,
                marriage,constellation,occupation,hometown,age)
    except:
        pass


url = 'https://www.qiushibaike.com/'
all = ['','hot/','imgrank/','text/','history/','pic/','textnew/']
all_url = [url+i for i in all]
for url in all_url:
    # print(i)
    #创建opener浏览器对象，并且设置代理处理器
    opener = request.build_opener(request.ProxyHandler(proxies = {'http':random.choice(proxies['http'])}))
    req = request.Request(url,headers=headers)
    resp = opener.open(req)
    if resp.status == 200:
        html = resp.read()

        # 解析
        soup1 = BeautifulSoup(html,'lxml')
        a = []
        start_href = soup1.select('div[class="author clearfix"]')
        for i in start_href:
            s2 = i.select('a[rel="nofollow"]')
            for j in s2:
                a.append(j.attrs.get('href'))
    # print(a)
    all_href = [start_url+x[1:] for x in a]
    # print(type(all_href))
    print(all_href)  # 为导航条的所有数据
    for y in all_href:
        print(y)
        # print(type(y))
        user_x = requestHtml(y)[1]   # 表示每一用户的详细页面代码
        # print(user_x)
        soup2 = BeautifulSoup(user_x,'lxml')
        all_data = parse2(soup2)
        print(all_data)     # 返回的每条数据


    #










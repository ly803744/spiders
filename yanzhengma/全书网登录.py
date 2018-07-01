# -*-coding:utf-8-*-
import requests
from lxml import etree
url = 'http://www.quanshuwang.com/login.php'

data = {
    'username': 'disen',
    'password': 'disen8888',
    'action': 'login'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
}

# 创建请求的session对象
s = requests.session()

# 通过session对象发起get或post请求
r = s.post(url,data,headers=headers)
r.encoding = 'gb2312'
if r.status_code == 200:
    print(r.encoding)
    parse = etree.HTML(r.text)
    title = parse.xpath('//title/text()')[0]
    if title == '登录成功':
        print('登录成功！！！')
        # 会自动的将cookie信息保存到session中

        # 发起查看用户藏书架的请求信息
        r = s.get('http://www.quanshuwang.com/modules/article/bookcase.php',headers=headers)
        r.encoding = 'gbk'
        if r.status_code == 200:

            parser = etree.HTML(r.text)
            trs = parser.xpath('//tr')[1:-1]
            print(trs,'gfcgfsddfssgggfs')
            for tr in trs:
                links = tr.xpath('.//a/text()')[:-1]
                print(links)
                print('-------------------------------------------')
        print(r.cookies)
    else:
        print('登录失败')
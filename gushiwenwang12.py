#-*-coding:utf-8-*-
import requests as rq
from lxml import etree
url = 'http://so.gushiwen.org/search.aspx'

params = {
    'value':'离骚'
}

headers = {
    'User-Agent':'Android5.0-OPPO'
}
r = rq.get(url,params=params,headers=headers)  # 关键参数传值

if r.status_code == 200:
    print('请求成功！！！')
    sons_path ='//div[@class="sons"]'
    sons_title = './/p//b/span/text()'
    sons_title2_path = './/p//b/text()'

    sons_author_path = './/p[@class="source"]/a/text()'
    content_son_path = './/div[@class="contson"]/text()'
    content2_son_path = './/div[@class="contson"]/p/text()'

    # 获取所有的诗词的div
    parse = etree.HTML(r.text)
    sons = parse.xpath(sons_path)
    for son in sons:
        title = son.xpath(sons_title)
        if  not title:
            title = son.xpath(sons_title2_path)
        print(title)
        author = son.xpath(sons_author_path)
        print(author)
        son_content =son.xpath(content_son_path)
        if not ''.join(son_content).replace('\n','').strip():
            son_content = son.xpath(content2_son_path)
        print(son_content)






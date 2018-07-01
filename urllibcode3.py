# -*-coding:utf-8-*-

from urllib import request, parse

# url = 'http://www.baidu.com/s'
# s = {'wd': '太空视频', 'user': 'qq'}
# query = parse.urlencode(s)
# print(url + query)
# # urlopen(url,data=b'')
# resp = request.urlopen(url, data=query.encode())  # 是一个字节类型
# # resp = request.urlopen(url+'?'+query)  # 是一个字节类型
# # print(resp.getcode())
# print(resp.read().decode())


# -------------------------------------------------------------------------------

url = 'http://www.baidu.com/s?wd=男神'
print(parse.quote(url))

# 网络请求的编码格式，浏览器专用，和其他的不一样
query = parse.quote('天空旅行')  # url编码
print(query)
print(parse.unquote(query))  # url解码

request.urlretrieve('http://www.baidu.com/s?wd=' + query, './html/太空旅行.html')

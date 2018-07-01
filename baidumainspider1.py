#-*-coding:utf-8-*-

from urllib import request

# 爬取百度的首页
# 1.确定baidu首页的地址(url)


url = 'http://www.baidu.com'

# 2.开始请求url获取网页内容
req = request.urlopen(url)    # 返回一个响应数据对象

# 3.判断请求是否成功(响应中是否存在数据)
print(req.status)
print(req.getcode())

# 4.从响应中读取网页内容

# print(req.readlines())
# print((b''.join(req.readlines())).decode())   # 连接后解码
print(req.read().decode())   # 读取字节码数据

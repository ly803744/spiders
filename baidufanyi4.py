# -*-coding:utf-8-*-

# http://fanyi.baidu.com/sug
from urllib.request import Request, urlopen
from urllib import parse

params = {
    'kw': '李'
}

params = parse.urlencode(params)
url = 'http://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
}

# 生成请求对象
# Request(url=,data=,headers=)
# data 的数据要求是byte类型,存在data时，说明是post请求

req = Request(url,
              params.encode(),
              headers)

# 发起请求
resp = urlopen(req)
if resp.status == 200:
    print('请求成功！！！')
    # print('---数据---',resp.read().decode())

    # 保存数据
    with open('baidufanyi.json', 'wb') as f:
        f.write(resp.read())

    print('保存数据成功')

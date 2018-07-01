# -*-coding:utf-8-*-

from urllib.request import Request, urlopen

import urllib.parse


#
# # 解决 error[SSL:CERTIFICATE_VERIFY_FAILED]的问题
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context


# 设置请求头的信息

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50  '
}

req = Request(url='https://www.baidu.com',
              headers=headers)

# 发起网络请求

resp = urlopen(req)
print(resp.status)
if resp.status == 200:
    print(resp.getheaders())  # 打印响应头的数据
    print(resp.read().decode())

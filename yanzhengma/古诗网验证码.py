# -*-coding:utf-8-*-

import requests

import ydm_http

randcode_url = 'https://so.gushiwen.org/RandCode.ashx'

# 创建session对象
s = requests.session()
r = s.get(randcode_url)
if r.status_code == 200:
    # 下载图片
    with open('randcode.gif', 'wb') as f:
        f.write(r.content)
    print('验证码图片下载成功')
    print('验证码请求之后的cookie: ',r.cookies)

    # 获取图片中的内容
    randCodeTxt = ydm_http.ydm("randcode.gif")
    print(type(randCodeTxt))
    print('获取到的验证码: ', randCodeTxt)

    # 用户登录
    login_url = 'https://so.gushiwen.org/user/login.aspx'
    login_data = {
        'from': 'http://so.gushiwen.org/user/collect.aspx',
        'email': '610039018@qq.com',
        'pwd': 'disen8888',
        'code': randCodeTxt.strip()
    }

    r = s.post(login_url, data=login_data)
    print(r.status_code)
    print(r.text)
    print(r.url)

# -*-coding:utf-8-*-

from urllib import request, parse
import hashlib

# ------------------------------读取百度百科的首页信息-----------------------------------------
# 将网页存入到当前的html文件下

# url = "https://baike.baidu.com/"
#
# req = request.urlopen(url)
#
# a = req.read().decode()
#
# print(req.status)

# with open('F:/DjangPro/Spider01/day02/html/a.txt', "w", encoding="utf-8") as f:
#     f.write(a)
# 将url网页的数据存储

# request.urlretrieve(url,'./html/baike.html')
# print('网页保存成功！！！')

# --------------------------------------------------下载图片------------------------------------
# img_url ='http://b.hiphotos.baidu.com/baike/pic/item/0823dd54564e925838cd08189c82d158cdbf4e4f.jpg'

# 基于md5生成一个新的文件名
# m = hashlib.md5()
# m.update('aaa'.encode())
# token = m.hexdigest()
# print(type(token))
#
#
# request.urlretrieve(img_url,'./images/'+token+'.jpg')
# print('图片保存成功！')

# -------------------------------------下载视频---------------------------------------------
# mp4_url = 'http://vali.cp31.ott.cibntv.net/youku/6572ea18f04337143fe436c7e/03000801005B19E55028BA1552FA5BD04B1B70-4A58-05E0-BA20-96EEA48A8F86.mp4?sid=052879182900010002577_00_A4eb29018e2c491b8a6684e99c125b82d&sign=51bd10b8cd652e07d1fceff35d7f73a8&ctype=50'
# request.urlretrieve(mp4_url,'./images/youku.mp4')



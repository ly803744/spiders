# -*-coding:utf-8-*-
# ----------------------配置----------------------------------
# 配置请求头

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
}

# 配置代理

proxies = {
    # 'http':'host:123,host:123',   # 切换代理ip
    'http': [
        '183.56.177.130:808',
        '112.115.57.20:3128',
        '114.115.182.59:3128',
        '121.42.167.160:3128'
    ],
    'https': '',
}

# 配置爬虫的起始位置

start_url = 'https://www.qiushibaike.com'

# 配置xpath路径

author_path = '//div[starts-with(@class,"author")]'

home_path = './a/@href'

src_path = './a/img/@src'

name_path = './a/h2/text()'

age_path = './div/text()'

next_page_path = '//ul[@class="pagination"]/li[last()]/a/@href'

DATABASE = {
    # 属性参考pymysql connection
    'default': {
        'host': '10.35.0.129',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'db': 'qiubai',
        'charset': 'utf8'
    }

}

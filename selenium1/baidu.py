# -*-coding:utf-8-*-
import time
from selenium import webdriver
from lxml import etree

url = 'http://www.baidu.com'

# 如果使用handless,则配置chrome的options
path = r'.\chromedriver.exe'
brower = webdriver.Chrome(path)

# 打开百度链接
brower.get(url)

# 发起一个搜索（在搜索框中输入内容，点击搜索按钮）
brower.find_element_by_id('kw').send_keys('python招聘')

# 点击按钮
brower.find_element_by_id('su').click()
time.sleep(5)

# 获取搜索之后的网页内容
html = brower.page_source  # 网页源码
print(type(html))
#
with open('baidu.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 获取所有搜索结果
links = brower.find_elements_by_xpath('//div[@id="content_left"]/div//h3/a')
print(links)
for link in links:
    print(link.text)
    print(link.get_attribute('href'))  # 获取web

# 保存网页快照，截屏
brower.save_screenshot('baidu.png')

# 模拟浏览器的滚动事件向下滚动
js = "var q=document.documentElement.scrollTop=10000"
brower.execute_script(js)

# brower.execute_script("window.scrollTo(0,11000)")
# brower.execute_script("window.scrollBy(0,10000)")
# brower.quit()
print('搞定')

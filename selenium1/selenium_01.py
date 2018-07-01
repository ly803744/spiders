# -*-coding:utf-8-*-
import time
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

path = r'.\chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.binary_location = path

# /mac/linux必须将 chromdriver放在/usr/local/bin目录
# driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome(path)

driver.get('http://www.baidu.com')

# 查找网页中的文本输入框，并且输入内容
driver.find_element_by_id('kw').send_keys('西安小吃')

# 执行网页上的搜索按钮，发起点击
driver.find_element_by_id('su').click()

time.sleep(5)
# 截屏
driver.save_screenshot('xa_xc.png')

driver.quit()  # 退出

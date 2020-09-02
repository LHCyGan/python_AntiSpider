# -*- encoding:utf-8 -*-
# author: liuheng

from selenium import webdriver
from parsel import Selector
import re

url = "http://www.porters.vip/captcha/jigsaw.html"

browser = webdriver.Chrome("D://chromedriver.exe")
browser.get(url)

html = browser.page_source

"定位获取计算滑动距离"
soup = Selector(html)
style1 = soup.css('#missblock::attr("style")').get()
print(style1)
style2 = soup.css('#targetblock::attr("style")').get()
# 编写提取函数
extract = lambda x: ''.join(re.findall('left: (\d+|\d+.\d+)px', x))
# 获取初始和结束为止
start = extract(style1)
end = extract(style2)
distance = float(end) - float(start)
print(distance)

# 定位滑块
jigsawCircle = browser.find_element_by_css_selector('#jigsawCircle')
action = webdriver.ActionChains(browser)
# 点击保持不松开
action.click_and_hold(jigsawCircle).perform()
# 设置滑动距离
action.move_by_offset(xoffset=distance, yoffset=0)
# 松开mouse
action.release().perform()


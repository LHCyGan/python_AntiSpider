# -*- encoding:utf-8 -*-
# author: liuheng

# 1. 定位滑块位置
# 2. 获取滑动距离

from selenium import webdriver

url = "http://www.porters.vip/captcha/sliders.html"

browser = webdriver.Chrome("D://chromedriver.exe")
browser.get(url)
# 定位滑块
hover = browser.find_element_by_css_selector(".hover")

action = webdriver.ActionChains(browser)
action.click_and_hold(hover).perform()
action.move_by_offset(xoffset=340, yoffset=0)
action.release().perform()






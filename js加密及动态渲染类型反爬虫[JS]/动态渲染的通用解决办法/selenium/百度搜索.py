from selenium import webdriver

# 初始化 Chrome浏览器对象
browser = webdriver.Chrome("D:\\chromedriver.exe")
# 向指定网址发起GET请求
browser.get("http://www.baidu.com")
# 使用CSS选择器定位输入框
input = browser.find_element_by_css_selector("input#kw")
# 输入要搜索的值
input.send_keys("python")
# 点击搜索按钮
browser.find_element_by_css_selector("input#su").click()



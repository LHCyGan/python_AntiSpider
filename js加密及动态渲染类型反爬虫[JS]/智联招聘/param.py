import random
import time
import math
import execjs
from selenium import webdriver

# 构造必要参数
# 1.
_v = str(random.random())[0:10]

# 2.
def get_param(e):
    str = "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx"
    t = (math.floor(time.time()*1000) + 16*random.random()) % 16 | 0
    # print(x_zp_page_request_id)
    for i in str:
        if str[i] == 'x' or str[i] == 'y':
            s = hex(t) if "x" == str[i] else hex(7 & t | 8)
            str.replace(str[i], s)
        else:
            continue
    x_zp_client_id = str
    return x_zp_client_id

#3. 编译js
x_zp_page_request_id =  """window.zpPageRequestId;"""


# from selenium import webdriver
# # 要想调用键盘按键操作需要引入keys包
#
# # 调用环境变量指定的PhantomJS浏览器创建浏览器对象
# driver = webdriver.PhantomJS("D:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
# # 如果没有在环境变量指定PhantomJS位置# driver = webdriver.PhantomJS(executable_path="./phantomjs"))
# # get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
# driver.get("https://sou.zhaopin.com/?p=2&jl=530&kw=python&kt=3")
# print(driver.execute_script(x_zp_page_request_id))
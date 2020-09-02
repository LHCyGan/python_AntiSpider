# -*- encoding:utf-8 -*-
# author: liuheng

import requests
from hashlib import md5
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By
from PIL import Image
from io import BytesIO


class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):

        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()

EMAIL = ""
PASSWORD = ""
# .login-hd-account a

class Click12306:
    def __init__(self):
        self.url = "https://kyfw.12306.cn/otn/resources/login.html"
        self.browser = webdriver.Chrome("d://chromedriver.exe")
        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMAIL
        self.password = PASSWORD
        self.chaojiying = Chaojiying_Client('liu007', 'iu111111', '907668')

    def open(self):
        self.browser.get(self.url)
        time.sleep(2)
        self.browser.find_element_by_css_selector(".login-hd-account a").click()
        time.sleep(1)
        # 等待图片加载
        self.wait.until(
            EC.presence_of_element_located((By.ID, "J-loginImg"))
        )
        time.sleep(1)
        email = self.wait.until(EC.presence_of_element_located((By.ID, "J-userName")))
        password = self.wait.until(EC.presence_of_element_located((By.ID, "J-password")))
        email.send_keys(self.email)
        password.send_keys(self.password)

    def get_touchClickElement(self):
        """获取验证码图片元素"""
        img_element = self.wait.until(EC.presence_of_element_located((By.ID, "J-loginImg")))
        return img_element

    def get_position(self):
        """获取验证码位置"""
        element = self.get_touchClickElement()
        time.sleep(2)
        location = element.location
        size = element.size
        top, bottom, left, right = location['y'], location['y'] + location['weight'],\
            location['x'], location['x'] + location['width']
        return top, bottom, left, right

    def get_screenShot(self):
        """获取网页截图"""
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))

    def get_touchClickImg(self):
        """获取验证码图片"""
        top, bottom, left, right = self.get_position()
        print('验证码位置:  ', top, bottom, left, right)
        screenshot = self.get_screenShot()
        captcha = screenshot.crop((left, top, right, bottom))
        return captcha

    def get_points(self):
        image = self.get_touchClickImg()
        bytes_array = BytesIO()
        image.save(bytes_array, format='PNG')
        # 识别验证码
        result = self.chaojiying.post_pic(bytes_array.getvalue(), "9005")
        print(result)
        groups = result.get('pic_str').split('|')
        locations = [[int(number) for number in group.split(',')] for group in groups]
        return locations

    def touch_captchaImg(self):
        """点击验证码图片"""
        locations = self.get_points()
        for location in locations:
            print(location)
            ActionChains(self.browser).move_to_element_with_offset(self.get_touchClickElement(), location[0],
                                                                   location[1]).click().perform()
            time.sleep(1)




if __name__ == '__main__':
	# chaojiying = Chaojiying_Client('liu007', 'iu111111', '907668')	#用户中心>>软件ID 生成一个替换 96001
	# im = open('a.jpg', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
	# print(chaojiying.PostPic(im, 1902))	#1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    test = Click12306()
    test.touch_captchaImg()
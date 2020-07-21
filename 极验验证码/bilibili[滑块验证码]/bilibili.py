# -*- encoding:utf-8 -*-
# author: liuheng

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from io import BytesIO
import io
from PIL import Image
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

EMAIL = "你的邮箱"
PASSWORD = "你的密码"

class BilibiliLogin:

    def __init__(self):
        self.url = 'https://passport.bilibili.com/login'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMAIL
        self.password = PASSWORD
        self.browser.get(self.url)
        email = self.wait.util(EC.presence_of_element_located(By.ID, 'login-username'))
        password = self.wait.utils(EC.presence_of_element_located(By.ID, 'login-passwd'))
        email.send_keys(self.email)
        password.send_keys(self.password)

    def get_button(self):
        button = self.wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR, '.gt_silder_knob'))
        return button

    def get_position(self):
        # 获得截图中图片的位置
        action = ActionChains(self.browser)
        action.move_to_element(self.button)
        self.buttton.click()
        img = self.wait.until(EC.presence_of_element_located(By.CSS_SELECTOR, '.gt_cut_fullbg.gt_show'))
        location = img.location
        size = img.size
        top = location['y']
        bottom = location['y'] + size['height']
        left = location['x']
        right = location['x'] + size['width']
        return (top, bottom, left, right)

    def get_image(self):
        # 获取图片
        top, bottom, left, right = self.get_position()
        time.sleep(1)
        screenshot = self.get_screenshot()
        # 浏览器缩放，所以要乘1.25
        img1 = screenshot.crop((left*1.25,top*1.25,right*1.25,bottom*1.25))
        time.sleep(1)
        ActionChains(self.browser).click_and_hold(self.button).perform()
        time.sleep(1)
        screenshot = self.get_screenshot()
        img2 = screenshot.crop((left*1.25,top*1.25,right*1.25,bottom*1.25))
        return img1, img2

    def get_screenshot(self):
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def is_pixel_equal(self, img1, img2, x, y):
        # 对比像素点是否一致
        pixel1 = img1.load()[x, y]
        pixel2 = img2.load()[x, y]
        # 副本图片中常有干扰的灰块，与原图像素不一致但差距小，用threshold变量排除干扰
        threshold = 80
        if abs(pixel1[0] - pixel2[0]) < threshold and \
                abs(pixel1[1] - pixel2[1]) < threshold and \
                abs(pixel1[2] - pixel2[2]) < threshold:
            return True
        else:
            return False

    def get_gap(self, img1, img2):
        # 对比各像素点是否一致
        left = 80
        for i in range(left, img1.size[0]):
            for j in range(img1.size[1]-30):
                if not self.is_pixel_equal((img1, img2, i, j)):
                    left = i
                    return left
        return left

    def get_track(self, distance):
        """利用牛顿第二定律模拟人的移动速度获取滑块移动轨迹"""
        # 移动轨迹
        track = []
        current = 0
        mid = (distance - 30) * 5 / 9
        mid2 = (distance - 30) * 7 / 9
        t = 0.2
        # 初速度
        v = 3
        # 初始加速度为2
        a = 2
        # 初始加速度增量
        aa = 0.3

        while current < distance - 25:
            if current < mid:
                a += aa
            elif current < mid2:
                a += aa
            else:
                if a < 0:
                    a -= aa
                else:
                    a = -a + 1
            # 初速度v0
            v0 = v
            # 当前速度v = v0 + at
            v = v0 + a * t
            # 移动距离x = v0t + 1/2 * a * t^2
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += round(move)
            # 加入轨迹
            track.append(round(move))

        track.append(0)
        track.append(-3)
        track.append(-2)
        print("distance:" + str(distance) + "track:")
        print(track)
        return track

    def move_to_gap(self, button, tracks):
        ActionChains(self.browser).click_and_hold(button).perform()
        for x in tracks:
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.3)
        ActionChains(self.browser).release().perform()

    def login(self):
        distance = self.get_gap(self.img1, self.img2)
        track = self.get_track(distance)
        self.move_to_gap(self.button, track)
        time.sleep(10)


def main(args):
    bilibili = BilibiliLogin()
    bilibili.login()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
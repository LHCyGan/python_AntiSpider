# -*- encoding:utf-8 -*-
# author: liuheng

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pwd import pwd
import time

url = "https://i.qq.com/"


def get_track(distance):
    """
    根据偏移量获取移动轨迹
    :param distance: 偏移量
    :return: 移动轨迹
    """
    # 移动轨迹
    track = []
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 4 / 5
    # 计算间隔
    t = 1
    # 初速度
    # v = 0
    v = 0
    while current < distance:
        if current < mid:
            # 加速度为正2
            # a_b = 8
            a = 10
        else:
            # 加速度为负3
            a = -3
        # 初速度v0
        v0 = v
        # 当前速度v = v0 + at
        v = v0 + a * t
        # 移动距离x = v0t + 1/2 * a_b * t^2
        move = v0 * t + 1 / 2 * a * t * t
        # 当前位移
        current += move
        # 加入轨迹
        track.append(round(move))
    return track

def slove_captcha(browser):

    # 尝试切换iframe
    try:
        iframe_ = browser.find_element_by_xpath("//iframe")
    except Exception as e:
        pass
    # 等待资源加载
    time.sleep(2)
    browser.switch_to.frame(iframe_)
    # 等待图片加载
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "tcaptcha_drag_button"))
    )
    try:
        button = browser.find_element_by_id("tcaptcha_drag_button")
    except Exception as e:
        pass
    time.sleep(1)

    # 开始拖动 perform()用来执行ActionChains中存储的行为
    # distance 代表的是滑块移动的距离，我们这里直接写死
    distance = 180
    times = 0
    while True:
        try:
            action = ActionChains(browser)
            # 点击并拖拽
            action.click_and_hold(button).perform()
            # 清除之前的action
            action.reset_actions()
            # 模拟轨迹方程
            track = get_track(distance)
            # 开始模拟拖拽
            for i in track:
                # y坐标不动，持续移动x坐标
                action.move_by_offset(xoffset=i, yoffset=0).perform()
                action.reset_actions()
            time.sleep(0.5)
            # 释放鼠标
            action.release().perform()
            time.sleep(5)
            times += 1
            print('这是第{}次'.format(times))
        except:
            print('登录成功')
            break


def login():
    browser = webdriver.Chrome("d://chromedriver.exe")
    browser.get(url)
    # 切换frame
    browser.switch_to.frame("login_frame")
    # 点击账号密码登录
    browser.find_element_by_css_selector("a#switcher_plogin").click()
    # 定位账号和密码
    browser.find_element_by_css_selector("input#u").clear()
    browser.find_element_by_css_selector("input#u").send_keys("2644078712@qq.com")
    browser.find_element_by_css_selector("input#p").clear()
    browser.find_element_by_css_selector("input#p").send_keys(pwd)
    # 点击登录
    browser.find_element_by_id("login_button").click()
    # 破解滑块验证码
    slove_captcha(browser)

    print(browser.title)

    time.sleep(2)
    browser.quit()
    print("finish~~")

if __name__ == '__main__':
    login()





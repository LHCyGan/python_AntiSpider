# -*- encoding:utf-8 -*-
# author: liuheng

"""打开网页，然后通过执行如下 JavaScript 语句来隐藏window.navigator.webdriver的值"""
"""1.后执行：先执行网站的js,在执行代码块中的"""
from selenium import webdriver
from pyppeteer import launch
import asyncio

async def crawl1():
    url = "http://www.taobao.com"
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto(url)
    await page.evaluate(
        """
        Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined 
        })
        """
    )
    await browser.close()

"""2.先执行：使用 Google 的Chrome Devtools-Protocol（Chrome 开发工具协议）简称CDP。"""
"""特点： 在每个Frame 刚刚打开，还没有运行 Frame 的脚本前，运行给定的脚本。"""
def crawl2():
    browser = webdriver.Chrome("D:\\chromedriver.exe")
    browser.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        """
            Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
               })
        """
    )
    browser.get("http://www.taobao.com")

def crawl2_2():
    """为了实现更好的隐藏效果，可以继续加入两个实验选项"""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options, executable_path='./chromedriver')
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
      """
    })
    driver.get('http://www.taobao.com')

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(crawl1())

    crawl2()
    crawl2_2()
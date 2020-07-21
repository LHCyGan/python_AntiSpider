import asyncio
from pyquery import PyQuery
from pyppeteer import launch


# 1. 实例1
# async def main():
#     # 初始化浏览器对象
#     browser = await launch()
#     # 在浏览器上下文中创建新页面
#     page = await browser.newPage()
#     # 打开目标网址
#     await page.goto("http://quotes.toscrape.com/js/")
#     # 获取页面内容
#     doc = PyQuery(await page.content())
#     print('Quotes:', doc('.quote').length)
#     # 关闭浏览器对象
#     await browser.close()

# 2. 实例2
# async def main():
#     """模拟网页截图，保存PDF"""
#     # headless: False打开浏览器,True/不设置默认不打开浏览器
#     # devtools: 是否打开调试窗口 。这个参数如果设置为了 True，那么 headless 就会被关闭了，界面始终会显现出来。
#     """
#     "Chrome 正受到自动测试软件的控制"，这个提示条有点烦，那咋关闭呢？这时候就需要用到 args 参数了，禁用操作如下：
#     browser = await launch(headless=False, args=['--disable-infobars'])
#     这里就不再写完整代码了，就是在 launch 方法中，args 参数通过 list 形式传入即可，这里使用的是 --disable-infobars 的参数。
#     另外有人就说了，这里你只是把提示关闭了，有些网站还是会检测到是 webdriver 吧，比如淘宝检测到是 webdriver 就会禁止登录了
#     """
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.goto('http://quotes.toscrape.com/js/')
#     # 截图保存
#     await page.screenshot(path='./example.png')
#     # 保存网页pdf
#     await page.pdf(path='./example.pdf')
#     # 执行js代码
#     dimensions = await page.evaluate(
#         '''() => {
#         return {
#             width: document.documentElement.clientWidth,
#             height: document.documentElement.clientHeight,
#             deviceScaleFactor: window.devicePixelRatio,
#         }
#     }''')
#     print(dimensions)
#     await browser.close()
#

width, height = 1366, 768

async def main():
    """
    爬虫的时候看到这界面是很让人崩溃的吧，而且这时候我们还发现了页面的 bug，整个浏览器窗口比显示的内容窗口要大，
    这个是某些页面会出现的情况，让人看起来很不爽。我们可以先解决一下这个显示的 bug，需要设置下 window-size 还有 viewport
    """
    browser = await launch(headless=False,
                           args=[f'--window-size={width},{height}'])
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.goto('https://www.taobao.com')
    await asyncio.sleep(100)

asyncio.get_event_loop().run_until_complete(main())

if __name__ == '__main__':
    # 开启异步事件循环，直到main函数执行结束
    asyncio.get_event_loop().run_until_complete(main())
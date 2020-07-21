import asyncio
from pyppeteer import launch

url = "http://www.ituring.com.cn"
async def main():
    # 初始化浏览器对象
    browser = await launch()
    # 创建新页面
    page = await browser.newPage()
    # 打开目标网址
    await page.goto(url)
    # 在指定位置输入文本
    await page.type('.key', 'Python')
    # 截图并保存
    # await page.screenshot(path="./turing.png")
    await page.screenshot({'path': "turing.png"})
    # 关闭浏览器对象
    await browser.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
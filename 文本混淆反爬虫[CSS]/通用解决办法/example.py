# -*- encoding:utf-8 -*-
# author: liuheng
"""利用自动化测试工具，对字体截图，再利用OCR文字识别"""
import asyncio
from pyppeteer import launch
import pytesseract
from PIL import Image

async def crawl():
    url = "http://www.porters.vip/confusion/movie.html"
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto(url)
    font = await page.screenshot({'path': './font.png', 'clip':
        {'x': 820, 'y': 400, 'width': 75, 'height': 40}})
    await browser.close()



if __name__ == '__main__':
    # asyncio.get_event_loop().run_until_complete(crawl())
    pytesseract.pytesseract.tesseract_cmd = r'S:\\Tesseract\\tesseract.exe'
    content = pytesseract.image_to_string(Image.open('./font.png'))
    print(content)
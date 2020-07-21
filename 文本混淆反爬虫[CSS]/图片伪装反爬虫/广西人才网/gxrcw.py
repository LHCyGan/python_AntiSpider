import requests
from parsel import Selector
import pytesseract
from PIL import Image
import io
from urllib.parse import urljoin


def get_html(url):

    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    if res.status_code == 200:
        print("[SUCCESS]Success......")
        get_info(res.text, url)
    else:
        print("[ERROR]Error......")

def get_info(html, url):
    soup = Selector(html)
    p = soup.css("div.contact-info-con.con p").extract()
    print(p)
    for i, sinfo in enumerate(p):
        soup_ = Selector(sinfo)
        print(soup_.css("p::text").extract()[0], end='\t')
        if i != 1:
            print(soup_.css("label::text").extract()[0])
        else:
            img_url = soup_.css("img::attr(src)").extract()[0]
            # img_url 为 主url中的content部分，所以必须要凭借才能访问
            img_url = urljoin(url, img_url)
            print(img_url)
            img_io = requests.get(url).content
            # 打开图片字节流，得到图片对象
            str = pytesseract.image_to_string(Image.open(io.BytesIO(img_io)))
            print(str)



if __name__ == '__main__':
    headers = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"}
    url = "https://www.gxrc.com/company/60056"
    get_html(url)
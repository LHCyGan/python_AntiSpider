import requests
from uuid import uuid1

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
}
font_url = {
    "font1": "http://s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/81ebaa4c.woff",
    "font2": "http://s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/d0b77af9.woff",
    "font3": "http://s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/dcf273b0.woff"
}

def get_html(url, i):
    resp = requests.get(url)
    if resp.status_code == 200:
        with open(f"{i}.wwof", 'wb') as f:
            f.write(resp.content)
    else:
        print("Error!")


if __name__ == '__main__':
    # 下载字体文件
    for key, i in enumerate(font_url.keys()):
        get_html(font_url[key], i)
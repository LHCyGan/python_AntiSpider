import re
import requests
from urllib.parse import urljoin
from uuid import uuid1

url = "http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/3f2beac95aee35757de0c7fca607c2b9.css"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
}
resp = requests.get(url, headers=headers)
print(resp.status_code)
# print(resp.text)
woff_urls = re.findall(',url\("(.*?)"\)', resp.text)
print(woff_urls)
for woff in woff_urls:
    w_url = urljoin("http:", woff)
    print(w_url)
    res = requests.get(w_url, headers=headers)
    with open(f"./{uuid1()}.woff", 'wb') as f:
        f.write(res.content)

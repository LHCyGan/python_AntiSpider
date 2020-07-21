import requests
import re

# url = "https:\\\/\\\/wkbjcloudbos.bdimg.com\\\/v1\\\/docconvert4305\\\/wk\\\/ea69fb38e3350b886ba30ffd3ddf7ef4\\\/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Thu%2C%2021%20May%202020%2009%3A24%3A06%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2020-04-06T01%3A24%3A06Z%2F3600%2Fhost%2Fe53ecb3dc15187d7267aeaa38313176defe5f4c692412c508dc48d28379ff923&x-bce-range=0-13298&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU4NjEzOTg0NiwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.ceEHL%2Fi29ddHz7t84rkt848rFmTHH1U5oTN6Qo94ZW8%3D.1586139846\x22"
# https://wenku.baidu.com/view/3828fb6eff00bed5b8f31d62.html?from=search
# print(url.replace('\\\/', '/'))
# print("\u4e2d\uff0c\u5141\u8bb8\u6211\u4eec\u66f4\u968f\u5fc3\u6240\u6b32\u66f4\u81ea\u7136\u7684\u4f7f\u7528\u6574\u6570\uff0c\u53ea\u6709\u4e00\u79cd\u7c7b\u578b\uff0c\u6ca1\u6709\u957f\u5ea6\u9650\u5236\u3002".encode("utf?").decode("utf?"))

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

session = requests.session()
session.headers = headers

def preprocess(html):
    result = ''
    doc_url = re.findall('(https.*?0.json.*?)\\\\x22}', html)
    # print(len(doc_url))
    doc_url = [url.replace('\\\\\/', '/') for url in doc_url[:-5]]
    # print(doc_url)
    with open("python.txt", 'w', encoding='utf8') as f:
        for url in doc_url[:-5]:
            html = session.get(url).text
            # print(url)
            txtlist = re.findall('"c":"(.*?)".*?"y":(.*?),', html)
            # print(txtlist)
            y = 0
            for item in txtlist:
                if not y == item[1]:  # 判断文本是否在一行
                    y = item[1]
                    n = '\n'
                else:
                    n = ''

                result += n
                result += item[0].encode("utf?").decode("unicode_escape", 'ignore')
                f.write(result)
                result = ''




def get_html(url):
    try:
        response = session.get(url)
        response.encoding = response.apparent_encoding
        response.raise_for_status()
        preprocess(response.text)
    except:
        print("Error")



if __name__ == '__main__':
	
    url = input("请输入要下载的文档的URL:")
    get_html(url)


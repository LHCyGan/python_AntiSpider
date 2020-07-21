import requests
import json
import math
import time
import websocket

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
}

def getToken(url):
    """获取加密串"""
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        # print(json.loads(r.text))
        return json.loads(r.text)['Data']
    else:
        print("Error!")
        return ""

def get_message():
    """构造websocket验证信息"""
    _time = math.floor(time.time() * 1000)
    info = {"chrome": 'true', "version": "80.0.3987.163", "webkit": 'true'}
    message1 = {
        'command': "RegisterInfo",
        'action': "Web",
        'ids': [],
        'UserInfo': {
            'Version': str([_time]) + json.dumps(info),
            'Url': "https://live.611.com/zq"
        }
    }
    message2 = {
        'command': "JoinGroup",
        'action': "SoccerLiveOdd",
        'ids': []
    }

    return json.dumps(message1), json.dumps(message2)

def download_info(url):
    """抓取数据"""
    token = getToken(url)
    message1, message2 = get_message()
    url_ = f"wss://push.611.com:6119/{token}"
    # 创建连接
    ws = websocket.create_connection(url_, timeout=10)
    # 发送验证信息
    ws.send(message1)
    ws.send(message2)
    with open("jsondata.json", 'a+', encoding='utf-8') as f:

        while True:
            # 接收服务器发送的数据
            result = ws.recv()
            json.dump(result, f, ensure_ascii=False)
            print(result)


if __name__ == '__main__':
    url = "https://live.611.com/Live/GetToken"
    # print(getToken(url))
    # print(1586685434000)
    # print(math.floor(time.time() * 1000))
    download_info(url)

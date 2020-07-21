# -*- encoding:utf-8 -*-
# author: liuheng
import requests
import execjs

class Login:
    headers = {
        'Origin': 'https://passport.fang.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'Referer': 'https://passport.fang.com/?backurl=https%3A%2F%2Fwww.fang.com%2F'
    }
    url = 'https://passport.fang.com/login.api'
    def __init__(self, username, password):
        self._username = username
        self._password = password

    def getPwd(self):
        with open('./pwd.js', 'r', encoding='utf8') as f:
            js = f.read()
        js_data = execjs.compile(js)
        self.pwd = js_data.call('getpwd', self._password)

    def __call__(self):
        self.getPwd()
        _data = {
            'uid': str(self._username),
            'pwd': str(self.pwd),
            'Service': 'soufun - passport - web',
            'AutoLogin': '1'
        }
        session = requests.session()
        resp = session.post(self.url, headers=self.headers,
                            data=_data)
        if resp.status_code == 200:
            print('请求成功！')
            print(resp.text)
        else:
            raise Exception

if __name__ == '__main__':
    user1 = Login('15591730713', 'iu111111')
    user1()


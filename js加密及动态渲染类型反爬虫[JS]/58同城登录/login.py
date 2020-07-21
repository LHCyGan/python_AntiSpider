# -*- encoding:utf-8 -*-
# author: liuheng

import requests
import execjs


class Login:
    def __init__(self, username, password):
        self._username = username
        self._password = password

    def getPwd(self):
        with open('./login.js', 'r', encoding='utf8') as f:
            data = f.read()
        js = execjs.compile(data)
        self._password = js.call('getpws', self._password)

    def __call__(self):
        self.getPwd()
        data = {
            "username": str(self._username),
            "password": self._password,
            "token": "hrYztRannTTB4fhHcrg2BljT8_6OHOg1",
            "source": "58-default-pc",
            "path": "https%3A%2F%2Fquanguo.58.com%2F%3Fpts%3D1595293904950",
            "validcode": "cjdm",
            "vcodekey": "-NMM3RV-dlZuqNeK-YmVGl4QT1gypV9Z",
            "domain": "58.com",
            "finger2": "zh-CN|24|1.25|8|1536_864|1536_824|-480|1|1|1|undefined|1|unknown|Win32|unknown|3|false|false|false|false|false|0_false_false|d41d8cd98f00b204e9800998ecf8427e|681e690b3a258ec98c7c5fd46fd9c4e6",
            "isremember": "false",
            "autologin": "false",
            "psdk-d": "jsdk",
            "psdk-v": "1.0.4",
            "fingerprint": "VaxFyUeQyup6lrqOb9uUFtIQEQ-ym4ew",
            "callback": "SDK_CALLBACK_FUN.successFun"
        }

        headers = {
            "referer": "https://passport.58.com/login/?path=https%3A//quanguo.58.com/&PGTID=0d100000-0221-881f-1840-0f9c4ec81616&ClickID=2",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4181.9 Safari/537.36",
            "origin": "https://passport.58.com",
            "cookie": "id58=c5/nfF8WQLN6jnpfEmJYAg==; city=quanguo; 58home=quanguo; 58tj_uuid=4171071d-d1be-4ac6-bc9a-8ffffcdfc8be; new_session=1; new_uv=1; utm_source=; spm=; init_refer=https%253A%252F%252Fwww.google.com%252F; wmda_uuid=eb3201b7aa1fc6c1eecb44c341a193bb; wmda_new_uuid=1; wmda_session_id_11187958619315=1595293883565-3591aa7f-39bd-cbb3; xxzl_cid=4d16d5288e71453aad7e1d88cfb29d9e; xzuid=617bad62-f3a4-4bbe-9505-7819b2f60a8e; xxzl_deviceid=lR3BhK6xsTvw1%2FWyEP1e%2BRbhlCrp3ozw4RX2ujAPnbihiLNEtrWMDSMwdICzA6zL; als=0; wmda_session_id_10104579731767=1595293906393-42d55ec0-2c21-cf07; wmda_visited_projects=%3B11187958619315%3B10104579731767; ppStore_fingerprint=55FCA6747EFF9D47020724E341CE7689DF414916C88CE5A3; finger_session=VaxFyUeQyup6lrqOb9uUFtIQEQ-ym4ew"
        }

        session = requests.session()
        session.headers = headers

        resp = session.post(data=data)
        if resp.status_code == 200:
            print("登陆成功！")

if __name__ == '__main__':
    user = Login("你的用户名", "你的密码")
    user()
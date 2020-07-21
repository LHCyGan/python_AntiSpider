# -*- encoding:utf-8 -*-
# author: liuheng

import hashlib
import requests
import json

USERNAME = "你的用户名"
PASSWORD = "你的密码"

password = hashlib.sha1(PASSWORD.encode('utf8')).hexdigest()
print(password)


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
}

data = {
    'login_type': 'default',
    'username': USERNAME,
    'password': password
}

url = "https://sso.jingoal.com/oauth/authorize?client_id=jmbmgtweb&response_type=code&state=%7Baccess_count%3A1%7D&locale=zh_CN&redirect_uri=https%3A%2F%2Fweb.jingoal.com%2F"
resp = requests.post(url, headers=headers, json=json.loads(data))
print(resp.text)
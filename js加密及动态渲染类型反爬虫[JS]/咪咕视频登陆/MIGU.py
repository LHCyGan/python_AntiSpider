# -*- encoding:utf-8 -*-
# author: liuheng

import requests
import execjs
import traceback


class MiGuLogin:

    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.url = "https://passport.migu.cn/authn"
        self.headers = {
            "Referer": "https://passport.migu.cn/login?sourceid=203021&apptype=2&forceAuthn=true&isPassive=false&authType=&display=&nodeId=70027513&relayState=login&weibo=1&callbackURL=https%3A%2F%2Fwww.miguvideo.com%2Fmgs%2Fwebsite%2Fprd%2Findex.html%3FisIframe%3Dweb",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4181.9 Safari/537.36"
        }

    def get_isFunc(self):
        """调用js加密文件"""
        js = execjs.compile("./migu.js")
        return js

    def encodeUN(self):
        """加密用户名"""
        js = self.get_isFunc()
        return js.call("getAccount", self.username)

    def encodePwd(self):
        """加密密码"""
        js = self.get_isFunc()
        return js.call("getPwd", self.password)

    def encodefingerPrint(self):
        """获取fingerPrint"""
        js = self.get_isFunc()
        return js.call("getfingerresult")

    def encodefingerprintDetails(self):
        """获取fingerPrintDetails"""
        js = self.get_isFunc()
        return js.call("getfingerdetails")

    def __call__(self):
        """模拟登录"""
        # 构造post 数据
        data = {
            "sourceID": "203021",
            "appType": "2",
            "relayState": "login",
            "loginID": self.encodeUN(),
            "enpassword": self.encodePwd(),
            "imgcodeType": "1",
            "fingerPrint": self.encodefingerPrint(),
            "fingerPrintDetail": self.encodefingerprintDetails(),
            "isAsync": "true"
        }
        # post 请求
        resp = requests.post(self.url, headers=self.headers, data=self.data)
        try:
            if resp.status_code == 200 :
                print("登陆成功！")
            else:
                resp.raise_for_status()
        except:
            traceback.print_exc()


if __name__ == '__main__':
    user = MiGuLogin("你的用户名", "你的密码")
    # 登录
    user()





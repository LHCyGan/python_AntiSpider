# -*- encoding:utf-8 -*-
# author: liuheng
import execjs


class Netease:

    def __init__(self, usename, password):
        self.username = usename
        self.pw = password

    def _getPw(self):
        with open("./netease.js", 'r', encoding='utf8') as f:
            content = f.read()

        jsdata = execjs.compile(content)
        self.pw = jsdata.call("getpw", self.pw)
        print("加密后的password:  " + self.pw)

        return self.username, self.pw

    def _getRtid(self):
        with open("./rtid.js", 'r', encoding='utf8') as f:
            content = f.read()
        jsdata = execjs.compile(content)
        rtid = jsdata.call("getrtid")
        print("rtid:  " + rtid)
        return rtid

if __name__ == '__main__':
    login = Netease("2644078712@qq.com", "123456")
    login._getPw()
    login._getRtid()
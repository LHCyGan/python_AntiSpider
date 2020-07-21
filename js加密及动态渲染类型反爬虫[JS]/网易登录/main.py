# -*- encoding:utf-8 -*-
# author: liuheng
import requests
from netease import Netease
import time


class Login:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
            "Host": "dl.reg.163.com",
            "Cookie": "hb_MA-BFF5-63705950A31C_source=www.google.com; _ntes_nuid=1bbd49cf34871cae4a9d89f7eefe37e7; NTES_hp_textlink1=old; BAIDU_SSP_lcr=https://www.google.com/; _ntes_nnid=9126e1f118ac8ceed21b0c046a5b0c84,1590291651307; JSESSIONID-WYTXZDL=dttiQ%5CO9en%2Fe%2Fh5z%2F0OkglnusFfethMqdVwarEgQN0IEQxiHvwhQf%5CkfbZHuq8yj%2BeHyfurL0sZLHInlAgoww6U%5CseZMOeMDEBqWNFMWZnYXxcqaUxH48tW19BPwPwtz7GnGKzyyrj1pGYhhuZ0lO7dDB3WdIvOp8AFktrSdq5XnY8Dj%3A1590292251475; _ihtxzdilxldP8_=30; NNSSPID=11d888c2df8e4b26aa35b2fcd6013c64; UM_distinctid=17244c4dde8657-0f73ae4b1b85c1-c373667-144000-17244c4dde9ab; utid=LOjwtey3fBMPz7biO9A4xwNMC1irKou8; l_s_163MODXOXd=5B4AE6BFF238CE247A553C01A50AC3901D5C136F4EA6C969DF9E5AC7B4691485B4EE8224B511271C3F68377F61BEC1E332F32B18156F84211894513E1F89E99AB8AB28821E11C7C39E5B19EB161E8D4556B27853FCCE640C00DB2246D09337A0B23DBFC4E22D141D4C2384CD2A7061C2"
        }

        self.url1 = f"https://dl.reg.163.com/dl/gt?un=2644078712%40qq.com&pkid=MODXOXd&pd=163&channel=0&topURL=https%3A%2F%2Fwww.163.com%2F&rtid={rtid}&nocache={nocache}"

        self.session = requests.session()
        self.session.headers = self.headers
    def __call__(self, *args, **kwargs):
        resp1 = self.session.get(self.url1)
        # print(resp1.json())
        self.tk = resp1.json()['tk']
        print('tk:  ' + self.tk)
        self.postdata = {"un": "2644078712@qq.com", "pw": pw, "pd": "163", "l": 0, "d": 10, "t": nocache,
                         "pkid": "MODXOXd", "domains": "qq.com", "tk": self.tk, "pwdKeyUp": 1, "channel": 0,
                         "topURL": "https://www.163.com/", "rtid": rtid}
        resp2 = self.session.post("https://dl.reg.163.com/dl/l", data=self.postdata)
        print(resp2.text)



if __name__ == '__main__':
    NE = Netease("2644078712@qq.com", "123456")
    username, pw = NE._getPw()
    rtid = NE._getRtid()
    nocache = round(time.time() * 1000)
    print(1590291714343)
    print(nocache)
    login = Login()
    login()
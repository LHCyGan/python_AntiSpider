# -*- encoding:utf-8 -*-
# author: liuheng

import requests
import execjs

headers = {
    'cookie': 'UM_distinctid=17236202c1e2-0e083b71b9f442-c373667-144000-17236202c1f722; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; _fbp=fb.1.1592637350019.741552080; t=522353cf5d5cbc5bd0f2d48b4377a43e; cookie2=1a6fe8f9a4280ecfab6c7d0512230c98; _tb_token_=e6eee5577eab; XSRF-TOKEN=f3123820-fd35-4b33-98ce-df971459daa7; _samesite_flag_=true; mt=ci=0_0; tracknick=; uc1=cookie14=UoTV75UhMVKV0w%3D%3D; cna=yBmnFpHslhcCAXGG6MHnxosj; sgcookie=E0ZiYiVRZa94fdlRX0zss; l=eBIFasy7QUeVV6fvBO5wlurza77tuIOfGsPzaNbMiInca61FTFWOFNQDRWuB7dtjgtfXLUtyOvlFRRFvPSULRx1Hrt7APlUOr_96-; isg=BJSUQJq9troZsSLMbTAI0z7aZdIG7bjXSsKhgS50OZ-6GTBjXvm3Z-zfGRGB4fAv; tfstk=cCScBPZuRZ8bsM8lRotfQ3wK3VPRaGU2GGSP4iLp9GYBQbj63svjz28Gq8AAiG31.',
    'referer': 'https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fi.taobao.com%2Fmy_taobao.htm%3Fspm%3Da21bo.2017.1997525045.1.118711d9L40wU1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}

def get_pw(pw):
    with open('./taobao.js', 'r', encoding='utf-8') as f:
        content = f.read()

    jscontent = execjs.compile(content)
    pw = jscontent.call("getPwd", pw)
    return pw


data = {
    "loginId": "15591730713",
    "password2": get_pw('iu111111'),
    "keepLogin": "false",
    "ua": '125#cQ7castWcW2vXuqc+NoExfdSuDf2r14YEXzdh0wkDDIBKkorpRxavD+jgMXBpWBEsaOOilE+OnoF21ntZFZyCevngHTxmSrfOhEolPt6ogGGr8lmFL9uPWuYlKbZWEqrxmYQXOduN1prwJQoUxt5UNGmSWnAZ2EpOVSv+vu8RCLLXXTa5Xflugh1350pB07c2wLc268stM1aNXZdrN3wqqYk0pKNCNNI6yxTX9wPWQv/LJ33X9AqZP0JC67NYs5/vvsxmCRhWXp+e/qeFWvPwyMdg8ArCkE+oWg4qz9EC/J6QwDhu31lfYSbccscKJsScUHUcNwSNgshCU2hLBsXIj4OoghhnGUrVy/CcNDy/Ny3UmEravUXaaV4bas0KMiScDHURhhai/sTJo9doBJHto5YORu5Ga1FAr+ZIC8NvIlZ327b2tZJB+rgt5ptySDLD21shihRCE/P3EJfHuUbGThNzdIVKJ7qtt8hwuuOmTreRdC4No1ksfOp8l5lAc/dypFVPUiVGdyc+6ccTxgnnSkyR5oIyFaSxr2DFWblnJPwMS+7woK/zrSTNmxNyEkgxzSpefJJstJxd9HVWu+VRnTYUG0tL9WXsYK4WaJQyrbtjO5FfNRcGAzgPpaMS+CnA+OeeUhS/LoHPorJQ4JLqrv0AqG/1AtCRDyXjq7ZB2qo+fnrJuxDtGmlSzlufECE4oexkYzu8hb1ayjO3HP8/Tw3fuLkf/ZssOk+2mtAgXp1PlRfVC2tKzsgxiSRTjTftnia7LYTw2UQyPsuhH7tcRosl2y8oQu9aubxRvcsRYyT/rrdQTiPs7fuR70Y5snlw4QFnggZaOYs5XdMBAlcGydspZsAlSWgjI4+jwR8SUjBvoXCw85TlBgAUpM2itTXU8aJzhA9mQUyMNdVIPLBNzo2wtkBhOsP0hQ26/xyIHc+6kPfjgFr4MfAcKqrE+62fs2vKsMakOJz0cjiNAjXETsf6ZwrL49GmrHqj1RXlkoDEscNrhSpAA9V6+TfT+mWoYE9AC9ZRhed1+YCTqlu2aWBZR1Wk+FU9+7EH052oEfTsSt8DKe1yPFDfYxfisaUXj87LK4fr4G6Xu/lKqGq1OfTDc4pI2fGxw4u2LWGVgxAQEBSp04rvCLmSHZWVAW5ahhR2gE4FHYqC5dsWVo90r5WR93OYYGxFZUs6EJCj23Dqq4fPyz7BUL6',
    "umidGetStatusVal": "255",
    "screenPixel": "1536x864",
    "navlanguage": "zh-CN",
    "navUserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    "navPlatform": "Win32",
    "appName": "taobao",
    "appEntrance": "taobao_pc",
    "_csrf_token": "JwLx7DtlywcKrhgfaLV134",
    'umidToken': 'e4e8d548be4b793bb6b60935bd48c7199b71b47d',
    'hsiz': '1a6fe8f9a4280ecfab6c7d0512230c98',
    'style': 'default',
    'appkey': '00000000',
    'from': 'tb',
    'isMobile': 'false',
    'lang': 'zh_CN',
    'returnUrl':'http://i.taobao.com/my_taobao.htm?spm=a21bo.2017.1997525045.1.118711d9L40wU1',
    'fromSite': '0'
}


if __name__ == '__main__':
    login_url = "https://login.taobao.com/newlogin/login.do?appName=taobao&fromSite=0"
    resp = requests.post(login_url, headers=headers, data=data, verify=False)
    if resp.status_code == 200:
        print("login Success...")
        print(get_pw('你的密码'))
        print(resp.text)
    else:
        print("ERROR!")
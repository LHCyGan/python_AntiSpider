import requests
from urllib.parse import quote, unquote
import random
import time
import math

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "cookie": "x-zp-client-id=47ca7d97-158f-4a9e-973f-ce183ffc3003; urlfrom=121114584; urlfrom2=121114584; adfcid=www.google.com; adfcid2=www.google.com; adfbid=0; adfbid2=0; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1586496268; __utma=269921210.1127270814.1586496268.1586496268.1586496268.1; __utmc=269921210; __utmz=269921210.1586496268.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=269921210.1.10.1586496268; sts_deviceid=171628be56f4d5-02f6904f1bbbcf-5313f6f-1327104-171628be570a43; dywea=95841923.2144117642476986600.1586496268.1586496268.1586496268.1; dywec=95841923; dywez=95841923.1586496268.1.1.dywecsr=google.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/; dyweb=95841923.1.10.1586496268; acw_tc=2760825015864962681355056ec3c361e3fec169f3b7241b42265138643fc9; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22171628be5868d4-0bfc0608bb1b99-5313f6f-1327104-171628be5879f8%22%2C%22%24device_id%22%3A%22171628be5868d4-0bfc0608bb1b99-5313f6f-1327104-171628be5879f8%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%7D; sts_sg=1; sts_sid=171628be5a416e-0192504de6096d-5313f6f-1327104-171628be5a5a8b; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fwww.google.com%2F; jobRiskWarning=true; ZP_OLD_FLAG=false; POSSPORTLOGIN=1; CANCELALL=1; LastCity=%E5%8C%97%E4%BA%AC; LastCity%5Fid=530; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1586496447; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%22e4267bff-7916-4f3f-8a14-911023933a0e-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22jobs%22:{%22recommandActionidShare%22:%220ba246e9-33fd-4ea4-986e-6330171eabd0-job%22}}; sts_evtseq=9"
}



def get_html(url):
    r = requests.post(url, headers=headers)
    if r.status_code == 200:
        print("OK!")
        print(r.text)
    else:
        r.raise_for_status()




if __name__ == '__main__':
    # # url = "https://sou.zhaopin.com/?p=2&jl=530&kw=python&kt=3"
    # url = "https://fe-api.zhaopin.com/c/i/sou?_v=0.78579323&x-zp-page-request-id=0843886f4f244f8286f01435199caadd-1586496445877-460228&x-zp-client-id=47ca7d97-158f-4a9e-973f-ce183ffc3003&MmEwMD=5YNCSEUGOSQcqwoi07LBq0PgW2rkYn9RycR.Hs6Qf785WYgJo82wl1Z1kW2nlyyN1Y7gVk7nRBUmhTVHyU5wG9T9JXz8X3iULEeUUF_0HurnJdlckduE1Stbtz7imK15UiJ8tm8HsqBXMLZeMpG0RM6vPiaVCYPo0AQG_LF117uOUwrbZltch5KBsahoEYKCa5MBP0zrvP7uEqPHKix3iuwc7gRy0T7Am_xaQDmWZmgIocvOSPLErRqOyGYFGHyBBikVoxagnyVuadS3snMITsXBKP32fyWmG_u6TIyQofoUngb3tnt4VZVD9sAX4Ko1eucQ4T2d5HU.WcQ8CjXAodfkmXFrntJqRUKvD4TJwzFZMp3oi0PU.nYf2tYQjqglqXV0afcg99r3_4HUXcnMbvlWg"
    # get_html(url)
    # print(unquote("_v=0.52755090&x-zp-page-request-id=0843886f4f244f8286f01435199caadd-1586496445877-460228&x-zp-client-id=47ca7d97-158f-4a9e-973f-ce183ffc3003&MmEwMD=55uqQOJKiFD0zCwgRonRzIgifiMTgR5BVNkwPgzjWolEf5P4jTd.Nyb9XvdlN1OId5CiyLCl0lJub8iyVZ9.JHB1Gkmuzv9.WRnIPSx2odESoZPyZF_lIwnG_tleDq8P9.KakGt5RArbivAhI96sWI0sDsq_DSfFeimCGiduYk21jxJJyXqLGZsi_dTOOWPizN83lsRW7SjWE.n0EyD_Szd4aPgUBD.qYXEDOgdoOxxIpBoCmeNapAf.orJteyhsYvJCAxZYlt5wnQM9K7oeFaLKdNjRoFwQ1CwIVO7imT_M8G_PP6yC._3bwmyDRWke83z.F7BOjvQ.WWw9njkUEJNOMIWP1c2PDWwwe3I5I7UKoBbwnMZPkxTAmxWuVES43V8EyP8u1xmuVUMFADmR.QWouVNzHPKcfXSv8MiPOkRZxWclyCmw0.6ZRQRStfx6gDVk"))
    # print(str(random.random())[0:10])
    # print((math.floor(time.time()*1000) + 16*random.random()) % 16 | 0)
    pass

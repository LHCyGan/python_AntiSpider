import requests
import time
import math
import json

from requests.packages import urllib3
urllib3.disable_warnings()

"""
GET /aweme/v1/aweme/post/?source=0&publish_video_strategy_type=2&max_cursor=1575283685000&sec_user_id=MS4wLjABAAAAcgaq_KjumFI7eZRHe2PqQd7sXP6wCsjc2lpl9HL_5PA&count=10&ts=1585361954&_rticket=1585361954714&mcc_mnc=46007& HTTP/1.1
'Host': 'api3-core-c-hl.amemv.com',
'Connection': 'keep-alive',
'Cookie': 'install_id=109261918808; ttreq=1$3b82209729989e1b0f9447c345bf5f3909ec56e3; odin_tt=1b2a0ed5be49e8487b9bab1bfbf98115ef0a108c129e23ccb68f607c7acc220ee958457cbdae072a97fb0e88b55d2169fdb17d13852b84e0cfa14116901a43c5',
'X-SS-REQ-TICKET': '1585361954713',
'sdk-version': '1',
'X-SS-DP': '1128',
'x-tt-trace-id': '00-1eefa90e0a10984ccbf42759b23f0468-1eefa90e0a10984c-01',
'User-Agent': 'com.ss.android.ugc.aweme/100401 (Linux; U; Android 5.1.1; zh_CN; SM-N960F; Build/JLS36C; Cronet/TTNetVersion:3154e555 2020-03-04 QuicVersion:8fc8a2f3 2020-03-02)',
'Accept-Encoding': 'gzip, deflate, br',
'X-Gorgon': '040100374000bbbafd1aee2335dd95386652aeb65203043dfd24',
'X-Khronos': '1585361954',
'x-common-params-v2': 'os_api=22&device_platform=android&device_type=SM-N960F&iid=109261918808&version_code=100400&app_name=aweme&openudid=9c305b3c7fff6412&device_id=71274646516&os_version=5.1.1&aid=1128&channel=tengxun_new&ssmix=a&manifest_version_code=100401&dpi=320&cdid=1243eaa2-5ea1-4c20-8191-d47f4f8dd3f1&version_name=10.4.0&resolution=1600*900&language=zh&device_brand=samsung&app_type=normal&ac=wifi&update_version_code=10409900&uuid=355757648012728',
"""




def download_video(url, title):
    """下载视频"""
    with open('{}.mp4'.format(title), 'wb') as f:
        with requests.get(url) as r:
            f.write(r.content)
    print(title + "下载视频成功！")


def get_url():
    headers = {
        'User-Agent': 'com.ss.android.ugc.aweme/100401 (Linux; U; Android 5.1.1; zh_CN; SM-N960F; Build/JLS36C; Cronet/TTNetVersion:3154e555 2020-03-04 QuicVersion:8fc8a2f3 2020-03-02)',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Host': 'api3-core-c-hl.amemv.com',
        'Cookie': 'install_id=109261918808; ttreq=1$3b82209729989e1b0f9447c345bf5f3909ec56e3; odin_tt=1b2a0ed5be49e8487b9bab1bfbf98115ef0a108c129e23ccb68f607c7acc220ee958457cbdae072a97fb0e88b55d2169fdb17d13852b84e0cfa14116901a43c5',
        'X-SS-REQ-TICKET': '1585361954713',
        'sdk-version': '1',
        'X-SS-DP': '1128',
        'x-tt-trace-id': '00-1eefa90e0a10984ccbf42759b23f0468-1eefa90e0a10984c-01',
        'X-Gorgon': '040100374000bbbafd1aee2335dd95386652aeb65203043dfd24',
        'X-Khronos': '1585361954',
        'x-common-params-v2': 'os_api=22&device_platform=android&device_type=SM-N960F&iid=109261918808&version_code=100400&app_name=aweme&openudid=9c305b3c7fff6412&device_id=71274646516&os_version=5.1.1&aid=1128&channel=tengxun_new&ssmix=a&manifest_version_code=100401&dpi=320&cdid=1243eaa2-5ea1-4c20-8191-d47f4f8dd3f1&version_name=10.4.0&resolution=1600*900&language=zh&device_brand=samsung&app_type=normal&ac=wifi&update_version_code=10409900&uuid=355757648012728'
    }
    url = 'https://api3-core-c-hl.amemv.com/aweme/v1/aweme/post/?source=0&publish_video_strategy_type=2&max_cursor=1575283685000&sec_user_id=MS4wLjABAAAAcgaq_KjumFI7eZRHe2PqQd7sXP6wCsjc2lpl9HL_5PA&count=10&ts=1585369989&_rticket=1585369990716&mcc_mnc=46007&'
    r = requests.get(url,
        headers=headers,
        verify=False)

    # print(r.content)
    print(r.status_code)
    print(r.text)
    json_data = r.json()['aweme_list']
    for j in json_data:
        title = j['desc']
        print(title)
        print(j['video']['play_addr']['url_list'][0])
        download_video(j['video']['play_addr']['url_list'][0], title)
        break


if __name__ == '__main__':
    # print(math.floor(time.time() * 1000))
    # print(1585314598672)
    # print(math.floor(time.time()))
    # print(1585314598)
    get_url()


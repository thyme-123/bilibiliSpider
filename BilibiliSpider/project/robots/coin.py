import requests
import re
from .. import Setting


class Coin():
    def __init__(self,aid):
        self.aid=aid

    def coin(self):
        headers = {'authority': 'api.bilibili.com',
                   'method': 'POST',
                   'path': '/x/web-interface/coin/add',
                   'scheme': 'https',
                   'accept': '*/*',
                   'accept-encoding': 'gzip, deflate',
                   'accept-language': 'zh-CN,zh;q=0.8',
                   'cache-control': 'no-cache',
                   'content-length': '93',
                   'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                   'cookie': Setting.Cookie,
                   'origin': 'https://www.bilibili.com',
                   'pragma': 'no-cache',
                   'referer': 'https://www.bilibili.com/video/av' + str(self.aid),
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36', }
        csrf=re.findall("bili_jct\=(.*?)\;", Setting.Cookie)[0]
        data = {'aid': str(self.aid),
                'multiply': Setting.coin,
                'select_like': Setting.select_like,
                'cross_domain': 'true',
                'csrf': csrf, }
        url = "https://api.bilibili.com/x/web-interface/coin/add"
        r = requests.post(url=url, headers=headers, data=data)
        if r.status_code==200:
            print("%s投币%i个,成功" % (self.aid, Setting.coin))
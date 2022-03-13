import requests
import re
from .. import Setting


class Like():
    def __init__(self,aid):
        self.url="https://api.bilibili.com/x/web-interface/archive/like"
        self.aid=aid

    def like(self):
        headers = {'authority': 'api.bilibili.com',
                   'method': 'POST',
                   'path': '/x/web-interface/archive/like',
                   'scheme': 'https',
                   'accept': 'application/json, text/plain, */*',
                   'accept-encoding': 'gzip, deflate',
                   'accept-language': 'zh-CN,zh;q=0.8',
                   'cache-control': 'no-cache',
                   'content-length': '57',
                   'content-type': 'application/x-www-form-urlencoded',
                   'cookie': Setting.Cookie,
                   'origin': 'https://www.bilibili.com',
                   'pragma': 'no-cache',
                   'referer': 'https://www.bilibili.com/video/av' + str(self.aid),
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36', }
        csrf = re.findall("bili_jct\= (.*?)\;", Setting.Cookie)[0]
        print(csrf)
        data = {'aid': self.aid,
                'like': '1',
                'csrf': csrf, }
        r = requests.post(url=self.url, headers=headers, data=data)
        print(r.text)
        if r.status_code==200:
            print("%s点赞成功"%(self.aid))

    def unlike(self):
        headers = {'authority': 'api.bilibili.com',
                   'method': 'POST',
                   'path': '/x/web-interface/archive/like',
                   'scheme': 'https',
                   'accept': 'application/json, text/plain, */*',
                   'accept-encoding': 'gzip, deflate',
                   'accept-language': 'zh-CN,zh;q=0.8',
                   'cache-control': 'no-cache',
                   'content-length': '57',
                   'content-type': 'application/x-www-form-urlencoded',
                   'cookie': Setting.Cookie,
                   'origin': 'https://www.bilibili.com',
                   'pragma': 'no-cache',
                   'referer': 'https://www.bilibili.com/video/av' + str(self.aid),
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36', }
        csrf = re.findall("bili_jct\=(.*?)\;", Setting.Cookie)
        data = {'aid': self.aid,
                'like': '2',
                'csrf': csrf, }
        r = requests.post(url=self.url, headers=headers, data=data)
        if r.status_code==200:
            print("%s取消点赞成功"%(self.aid))
